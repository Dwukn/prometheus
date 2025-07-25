document.addEventListener('DOMContentLoaded', function () {
    const siteInput = document.getElementById('siteInput');
    const addButton = document.getElementById('addSite');
    const siteList = document.getElementById('siteList');
    const fileInput = document.getElementById('fileInput');
    const importButton = document.getElementById('importSites');
    const manageButton = document.getElementById('manageSites');

    loadBlockedSites();

    // Add new blocked site
    addButton.addEventListener('click', () => {
        const site = siteInput.value.trim().toLowerCase();
        if (site) {
            addBlockedSite(site);
            siteInput.value = '';
        }
    });

    // Handle file input dialog
    fileInput.addEventListener('change', handleFileUpload);
    importButton.addEventListener('click', () => {
        fileInput.click();  // Trigger the file input dialog
    });

    // Open the manage sites page in a new tab
    manageButton.addEventListener('click', () => {
        chrome.tabs.create({
            url: 'manage.html'
        });
    });

    // Load the list of blocked sites from storage
    async function loadBlockedSites() {
        const { blockedSites = [] } = await chrome.storage.local.get('blockedSites');
        siteList.innerHTML = '';

        if (blockedSites.length === 0) {
            siteList.innerHTML = '<p>No blocked sites yet.</p>';
        } else {
            // Show only the 5 most recent entries in popup
            blockedSites.slice(-5).forEach(site => {
                const div = document.createElement('div');
                div.className = 'site-item';
                div.innerHTML = `<span>${site}</span>`;
                siteList.appendChild(div);
            });

            if (blockedSites.length > 5) {
                const more = document.createElement('div');
                more.textContent = `... and ${blockedSites.length - 5} more`;
                more.style.textAlign = 'center';
                more.style.fontStyle = 'italic';
                siteList.appendChild(more);
            }
        }
    }

    // Add a new blocked site to storage
    async function addBlockedSite(site) {
        const { blockedSites = [] } = await chrome.storage.local.get('blockedSites');
        if (!blockedSites.includes(site)) {
            blockedSites.push(site);
            await chrome.storage.local.set({ blockedSites });
            loadBlockedSites();
        }
    }

    // Handle file upload for importing sites
    async function handleFileUpload(event) {
        const file = event.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = async (e) => {
            try {
                if (file.name.endsWith('.json')) {
                    await handleJsonFile(e.target.result);
                } else if (file.name.endsWith('.txt')) {
                    await handleTxtFile(e.target.result);
                } else {
                    alert('Unsupported file type.');
                }

                loadBlockedSites();
                fileInput.value = ''; // Reset the file input field
            } catch (error) {
                console.error('Error importing sites:', error);
                alert('Error importing sites. Please check the file format.');
            }
        };
        reader.readAsText(file); // Read the file as text
    }

    // Handle JSON file import
    async function handleJsonFile(content) {
        const importData = JSON.parse(content);
        if (importData.blockedSites) {
            const { blockedSites: existingSites = [] } = await chrome.storage.local.get('blockedSites');
            const newSites = [...new Set([...existingSites, ...importData.blockedSites])];
            await chrome.storage.local.set({ blockedSites: newSites });
        }
    }

    // Handle TXT file import
    async function handleTxtFile(content) {
        const lines = content.split(/[\r\n]+/); // Split the file into lines
        const sites = lines
            .map(line => {
                const parts = line.split(/\s+/); // Split each line by whitespace
                return parts.length > 1 ? parts[1].trim().toLowerCase() : null; // Extract the domain
            })
            .filter(site => site && !site.startsWith('#')); // Ignore comments or empty lines

        const { blockedSites = [] } = await chrome.storage.local.get('blockedSites');
        const newSites = [...new Set([...blockedSites, ...sites])];
        await chrome.storage.local.set({ blockedSites: newSites });
    }
});
