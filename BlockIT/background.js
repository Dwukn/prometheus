// Initialize data when extension is installed or updated
chrome.runtime.onInstalled.addListener(async () => {
    const { blockedSites, archivedSites } = await chrome.storage.local.get([
      'blockedSites',
      'archivedSites'
    ]);

    // Initialize storage if empty
    if (!blockedSites || blockedSites.length === 0) {
      await chrome.storage.local.set({ blockedSites: [] });
    }
    if (!archivedSites || Object.keys(archivedSites).length === 0) {
      await chrome.storage.local.set({ archivedSites: {} });
    }
  });

  // Handle site blocking
  chrome.webNavigation.onBeforeNavigate.addListener(async function (details) {
    if (details.frameId !== 0) return; // Only handle top-level navigations

    const url = new URL(details.url);
    const domain = normalize(url.hostname.toLowerCase());

    const { blockedSites = [], archivedSites = {} } = await chrome.storage.local.get([
      'blockedSites',
      'archivedSites'
    ]);

    // Clean up expired archived sites only if there are any changes
    const now = Date.now();
    let archiveUpdated = false;
    for (const [site, data] of Object.entries(archivedSites)) {
      if (now >= data.endTime) {
        // If archived site expired, move it back to blocked sites
        if (!blockedSites.includes(site)) {
          blockedSites.push(site);
        }
        delete archivedSites[site];
        archiveUpdated = true;
      }
    }

    // Update storage if any archives were updated
    if (archiveUpdated) {
      await chrome.storage.local.set({
        blockedSites,
        archivedSites
      });
    }

    // Check if site is archived (allowed) or blocked
    const isArchived = Object.keys(archivedSites).some(site => domain.includes(normalize(site)));
    if (isArchived) {
      return; // Allow access to archived sites
    }

    if (blockedSites.some(site => domain.includes(normalize(site)))) {
      chrome.tabs.update(details.tabId, {
        url: chrome.runtime.getURL('blocked.html')
      });
    }
  });

  // Helper function to normalize domains
  const normalize = (str) => {
    let normalizedStr = str.replace(/^https?:\/\//, '').replace(/^www\./, '');
    return normalizedStr.replace(/\/$/, '').toLowerCase();
  };

  // Listen for storage changes to keep blocking rules up to date
  chrome.storage.onChanged.addListener((changes, namespace) => {
    if (namespace === 'local') {
      if (changes.blockedSites) {
        console.log('Blocked sites updated:', changes.blockedSites.newValue);
      }
      if (changes.archivedSites) {
        console.log('Archived sites updated:', changes.archivedSites.newValue);
      }
    }
  });
