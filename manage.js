document.addEventListener('DOMContentLoaded', async function () {
    loadSites();
    const lastCheckedKey = 'lastChecked';

    async function loadSites() {
        const { blockedSites = [], archivedSites = {} } = await chrome.storage.local.get(['blockedSites', 'archivedSites']);
        const sitesList = document.getElementById('sitesList');
        sitesList.innerHTML = '';

        // Display active sites
        blockedSites.forEach(site => {
            const div = createSiteEntry(site, false);
            sitesList.appendChild(div);
        });

        // Display archived sites
        Object.entries(archivedSites).forEach(([site, data]) => {
            const div = createSiteEntry(site, true, data.endTime);
            sitesList.appendChild(div);
        });

        try {
            const { blockedSites = [], archivedSites = {} } = await chrome.storage.local.get(['blockedSites', 'archivedSites']);
            console.log('Blocked Sites:', blockedSites);
            console.log('Archived Sites:', archivedSites);
        } catch (error) {
            console.error('Error loading sites:', error);
        }
    }

    function createSiteEntry(site, isArchived, endTime = null) {
        const div = document.createElement('div');
        div.className = `site-entry ${isArchived ? 'archived' : ''}`;

        const siteInfo = document.createElement('div');
        siteInfo.textContent = site;
        if (isArchived) {
            const timeLeft = Math.max(0, Math.floor((endTime - Date.now()) / 1000));
            const timeLeftStr = formatTimeLeft(timeLeft);
            siteInfo.textContent += ` (Archived - ${timeLeftStr} remaining)`;
        }

        const controls = document.createElement('div');
        controls.className = 'site-controls';

        // Checkbox to select individual site for deletion
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.className = 'site-checkbox';
        controls.appendChild(checkbox);

        if (!isArchived) {
            const archiveBtn = document.createElement('button');
            archiveBtn.textContent = 'Archive';
            archiveBtn.className = 'archive-btn';
            archiveBtn.onclick = () => archiveSite(site);
            controls.appendChild(archiveBtn);
        }

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.className = 'delete-btn';
        deleteBtn.onclick = () => deleteSite(site, isArchived);
        controls.appendChild(deleteBtn);

        div.appendChild(siteInfo);
        div.appendChild(controls);
        return div;
    }

    async function archiveSite(site) {
        const period = parseInt(document.getElementById('archivePeriod').value);
        const endTime = Date.now() + (period * 1000);

        const { blockedSites = [], archivedSites = {} } = await chrome.storage.local.get(['blockedSites', 'archivedSites']);

        // Remove from blocked sites
        const updatedBlockedSites = blockedSites.filter(s => s !== site);

        // Add to archived sites
        archivedSites[site] = {
            endTime: endTime
        };

        await chrome.storage.local.set({
            blockedSites: updatedBlockedSites,
            archivedSites: archivedSites
        });

        loadSites();
    }

    async function deleteSite(site, isArchived) {
        if (isArchived) {
            const { archivedSites = {} } = await chrome.storage.local.get('archivedSites');
            delete archivedSites[site];
            await chrome.storage.local.set({ archivedSites });
        } else {
            const { blockedSites = [] } = await chrome.storage.local.get('blockedSites');
            const updatedSites = blockedSites.filter(s => s !== site);
            await chrome.storage.local.set({ blockedSites: updatedSites });
        }
        loadSites();
    }

    function formatTimeLeft(seconds) {
        if (seconds < 60) return `${seconds}s`;
        if (seconds < 3600) return `${Math.floor(seconds / 60)}m`;
        if (seconds < 86400) return `${Math.floor(seconds / 3600)}h`;
        return `${Math.floor(seconds / 86400)}d`;
    }

    // Check archived sites every minute instead of every second
    setInterval(async () => {
        const { archivedSites = {} } = await chrome.storage.local.get('archivedSites');
        let updated = false;

        for (const [site, data] of Object.entries(archivedSites)) {
            if (Date.now() >= data.endTime) {
                // Archive period is over, move back to blocked sites
                const { blockedSites = [] } = await chrome.storage.local.get('blockedSites');
                if (!blockedSites.includes(site)) {
                    blockedSites.push(site);
                }
                delete archivedSites[site];
                updated = true;
            }
        }

        if (updated) {
            await chrome.storage.local.set({
                archivedSites,
                blockedSites
            });
            loadSites();
        }
    }, 60000); // Changed to 60 seconds

    

    // Select All checkbox functionality
    const selectAllCheckbox = document.getElementById('selectAllCheckbox');
    selectAllCheckbox.addEventListener('change', function () {
        const checkboxes = document.querySelectorAll('.site-checkbox');
        checkboxes.forEach(checkbox => {
            checkbox.checked = selectAllCheckbox.checked;
        });
    });

    // Delete selected sites functionality
    const deleteSelectedBtn = document.getElementById('deleteSelectedBtn');
    deleteSelectedBtn.addEventListener('click', async function () {
        const checkboxes = document.querySelectorAll('.site-checkbox:checked');
        const sitesToDelete = Array.from(checkboxes).map(checkbox => checkbox.closest('.site-entry').querySelector('div').textContent.trim());

        const { blockedSites = [], archivedSites = {} } = await chrome.storage.local.get(['blockedSites', 'archivedSites']);

        // Delete selected sites from blockedSites
        const updatedBlockedSites = blockedSites.filter(site => !sitesToDelete.includes(site));
        // Delete selected sites from archivedSites
        sitesToDelete.forEach(site => {
            delete archivedSites[site];
        });

        await chrome.storage.local.set({
            blockedSites: updatedBlockedSites,
            archivedSites: archivedSites
        });

        loadSites();
    });
});
