# Site Blocker Chrome Extension

A powerful and user-friendly Chrome extension designed to help users block or archive websites to improve productivity and manage internet usage. The extension allows users to add sites to a blocked list, archive sites for a set duration, and manage their blocked and archived sites efficiently.

This extension includes features for importing/exporting site lists, periodic cleanup of archived sites, and bulk management of sites, making it easy to keep track of blocked domains and limit distractions.

## Features

- **Block Websites**: Add domains to a blocked list, automatically redirecting users to a "blocked" page.
- **Archive Websites**: Archive sites temporarily for a set period. Once the time expires, they automatically return to the blocked list.
- **Import/Export Sites**: Import blocked sites from `.txt` or `.json` files and export your blocked and archived site lists.
- **Manage Sites**: View, archive, delete, or export sites using an intuitive management interface.
- **Real-Time Blocking**: Sites on the blocked list will automatically be redirected to a custom `blocked.html` page.
- **Periodic Cleanup**: Archived sites that exceed their expiration time are automatically moved back to the blocked list.

## Demo
<!-- yet to be added -->
![Site Blocker Demo](assets/demo.gif)
*Animated demo showcasing the site management and blocking features.*

## Installation

### Prerequisites
- **Google Chrome** (or any Chromium-based browser).
- A computer or device with internet access.

### Steps to Install

1. Clone or download this repository to your local machine.
   ```bash
   git clone https://github.com/your-username/site-blocker-extension.git
   ```

2. Open Chrome and navigate to `chrome://extensions/`.

3. Enable **Developer mode** (toggle at the top-right).

4. Click **Load unpacked** and select the folder where you cloned or extracted the repository.

5. The extension will now be available in your Chrome toolbar.

## Usage

### Popup Interface

- **Add Sites**: Enter a website domain in the input box and click **Add Site** to block it.
- **Import Sites**: Click **Import** to upload a `.txt` or `.json` file containing sites to block.
- **Manage Sites**: Click **Manage Sites** to open the management page, where you can view, delete, or archive sites.

### Manage Page

- **Active Sites**: Displays all currently blocked sites.
- **Archived Sites**: Displays sites that are archived and temporarily unblocked. Shows the time left before they return to the blocked list.
- **Actions**:
  - **Archive**: Temporarily unblocks a site for a set duration.
  - **Delete**: Permanently removes a site from the list.
  - **Export**: Downloads a `.json` file with the list of blocked and archived sites.
  - **Select All**: Select multiple sites for bulk deletion or archiving.

### Site Blocking

Sites added to the blocked list will be redirected to the `blocked.html` page whenever a user attempts to visit them.

### Import/Export

- **Import Sites**: Import blocked sites from a `.txt` or `.json` file.
  - `.txt` Format Example:
    ```
    example.com
    another-site.org
    ```
  - `.json` Format Example:
    ```json
    {
      "blockedSites": ["example.com", "another-site.org"]
    }
    ```

- **Export Sites**: Export the list of blocked and archived sites as a `.json` file.


### `background.js`
Handles background tasks such as:
- Initializing and cleaning up storage data on installation.
- Intercepting web navigation to check for blocked or archived sites.
- Normalizing domain names to ensure consistent comparison.

### `popup.js`
Manages the popup interface logic, such as:
- Adding sites to the blocked list.
- Importing sites from files.
- Displaying a list of blocked sites and allowing the user to manage them.

### `manage.js`
Handles the logic for the site management interface:
- Displaying and managing blocked and archived sites.
- Supporting bulk operations like deleting or archiving multiple sites.

### `manifest.json`
Defines the extension's configuration and permissions, including the background service worker and content scripts.

```json
{
  "manifest_version": 3,
  "name": "Site Blocker",
  "version": "1.0",
  "description": "Block or archive sites temporarily.",
  "permissions": ["storage", "webNavigation", "tabs"],
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_popup": "popup.html"
  },
  "host_permissions": [
    "http://*/*",
    "https://*/*"
  ],
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
}
```

## Contributing

We welcome contributions to improve the extension. Here’s how you can help:

1. **Fork the repository** and clone it to your local machine.
2. Create a **new branch** for your feature or bugfix.
3. **Make your changes** and add tests if necessary.
4. **Commit your changes** with a descriptive commit message.
5. Push your changes to your fork and submit a **Pull Request**.

Please ensure that your code adheres to the [Coding Standards](#) and passes all tests before submitting a pull request.

## Issues

If you find a bug or have a feature request, feel free to open an [issue](https://github.com/your-username/site-blocker-extension/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The extension uses **Chrome Storage API** and **Chrome Web Navigation API** to store and manage user data.
