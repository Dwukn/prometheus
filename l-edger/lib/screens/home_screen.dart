// home_screen.dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../providers/link_provider.dart';
import '../models/link.dart';
import '../models/folder.dart';
import '../widgets/folder_card.dart';
import '../widgets/link_list.dart';
import '../widgets/add_link_form.dart';
import '../widgets/add_folder_form.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  // Use a special string value to indicate home screen view instead of null
  static const String HOME_VIEW = "home_view";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Padding(
          padding: EdgeInsets.symmetric(horizontal: 16.0),
          child: Text('Link Manager'),
        ),
        actions: [
          IconButton(
            icon: const Icon(Icons.search),
            onPressed: () {
              showSearch(
                context: context,
                delegate: LinkSearchDelegate(context),
              );
            },
          ),
        ],
      ),
      drawer: Drawer(
        child: Column(
          children: [
            const DrawerHeader(
              decoration: BoxDecoration(
                color: Colors.blue,
              ),
              child: Center(
                child: Text(
                  'Navigation',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 24,
                  ),
                ),
              ),
            ),
            ListTile(
              leading: const Icon(Icons.home),
              title: const Text('Home'),
              onTap: () {
                final provider = Provider.of<LinkProvider>(context, listen: false);
                provider.setCurrentFolder(HOME_VIEW); // Using special value for home view
                Navigator.pop(context);
              },
            ),
            const Divider(),
            const Padding(
              padding: EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
              child: Text(
                'FOLDERS',
                style: TextStyle(
                  color: Colors.grey,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            Expanded(
              child: Consumer<LinkProvider>(
                builder: (context, provider, child) {
                  return ListView.builder(
                    itemCount: provider.folders.length,
                    itemBuilder: (context, index) {
                      final folder = provider.folders[index];
                      bool isSelected = folder.id.toString() == provider.currentFolderId;

                      return ListTile(
                        contentPadding: const EdgeInsets.symmetric(horizontal: 16.0),
                        title: Text(
                          folder.name,
                          style: TextStyle(
                            fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                            color: isSelected ? Colors.blueAccent : Colors.black,
                          ),
                        ),
                        tileColor: isSelected ? Colors.blue.withOpacity(0.1) : null,
                        selected: isSelected,
                        onTap: () {
                          provider.setCurrentFolder(folder.id.toString());
                          Navigator.pop(context);
                        },
                        leading: Icon(
                          Icons.folder,
                          color: isSelected ? Colors.blueAccent : Colors.grey,
                        ),
                      );
                    },
                  );
                },
              ),
            ),
            ListTile(
              leading: const Icon(Icons.create_new_folder),
              title: const Text('Add Folder'),
              onTap: () {
                Navigator.pop(context);
                showDialog(
                  context: context,
                  builder: (context) => const AddFolderDialog(),
                );
              },
            ),
          ],
        ),
      ),
      body: Consumer<LinkProvider>(
        builder: (context, provider, child) {
          // Show folders grid when in home view
          if (provider.currentFolderId == HOME_VIEW) {
            return Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Padding(
                  padding: EdgeInsets.all(16.0),
                  child: Text(
                    'My Folders',
                    style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                Expanded(
                  child: GridView.builder(
                    padding: const EdgeInsets.all(16.0),
                    gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                      crossAxisCount: 2,
                      childAspectRatio: 1.2,
                      crossAxisSpacing: 16,
                      mainAxisSpacing: 16,
                    ),
                    itemCount: provider.folders.length,
                    itemBuilder: (context, index) {
                      final folder = provider.folders[index];
                      // Count links in this folder
                      final linkCount = provider.links.where(
                        (link) => link.folderId == folder.id.toString()
                      ).length;

                      return FolderCard(
                        folder: folder,
                        linkCount: linkCount,
                        onTap: () {
                          provider.setCurrentFolder(folder.id.toString());
                        },
                        onDelete: folder.id != 1 ? () {
                          _showDeleteFolderDialog(context, folder);
                        } : null,
                      );
                    },
                  ),
                ),
              ],
            );
          } else {
            // Show links in the selected folder
            final currentFolder = provider.folders.firstWhere(
              (folder) => folder.id.toString() == provider.currentFolderId,
              orElse: () => Folder(
                id: 1,
                name: 'Default',
                dateCreated: DateTime.now(),
              ),
            );

            return Column(
              children: [
                Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Row(
                    children: [
                      IconButton(
                        icon: const Icon(Icons.arrow_back),
                        onPressed: () {
                          provider.setCurrentFolder(HOME_VIEW);
                        },
                      ),
                      const SizedBox(width: 8),
                      const Icon(Icons.folder),
                      const SizedBox(width: 8),
                      Text(
                        currentFolder.name,
                        style: const TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
                const Divider(),
                Expanded(
                  child: LinkList(
                    links: provider.links.where(
                      (link) => link.folderId == provider.currentFolderId
                    ).toList(),
                    onDelete: (id) => provider.deleteLink(id),
                    onEdit: (link) {
                      showDialog(
                        context: context,
                        builder: (context) => AddLinkDialog(
                          isEditing: true,
                          link: link,
                        ),
                      );
                    },
                    onDoubleTap: (link) {
                      _copyLinkToClipboard(context, link);
                    },
                  ),
                ),
              ],
            );
          }
        },
      ),
      floatingActionButton: Consumer<LinkProvider>(
        builder: (context, provider, child) {
          return FloatingActionButton(
            onPressed: () {
              if (provider.currentFolderId == HOME_VIEW) {
                // On home screen, add folder
                showDialog(
                  context: context,
                  builder: (context) => const AddFolderDialog(),
                );
              } else {
                // In a folder, add link
                showDialog(
                  context: context,
                  builder: (context) => const AddLinkDialog(),
                );
              }
            },
            child: Icon(provider.currentFolderId == HOME_VIEW ? Icons.create_new_folder : Icons.add_link),
            tooltip: provider.currentFolderId == HOME_VIEW ? 'Add a new folder' : 'Add a new link',
          );
        },
      ),
    );
  }

  void _showDeleteFolderDialog(BuildContext context, Folder folder) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Delete Folder'),
        content: Text(
          'Are you sure you want to delete "${folder.name}"? All links will be moved to the Default folder.',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('CANCEL'),
          ),
          TextButton(
            onPressed: () {
              Provider.of<LinkProvider>(context, listen: false)
                  .deleteFolder(folder.id!);
              Navigator.pop(context);
            },
            child: const Text('DELETE'),
          ),
        ],
      ),
    );
  }

  void _copyLinkToClipboard(BuildContext context, Link link) {
    Clipboard.setData(ClipboardData(text: link.url));
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('Link copied to clipboard: ${link.url}'),
        duration: const Duration(seconds: 2),
        action: SnackBarAction(
          label: 'DISMISS',
          onPressed: () {},
        ),
      ),
    );
  }
}

class LinkSearchDelegate extends SearchDelegate<String> {
  final BuildContext context;

  LinkSearchDelegate(this.context);

  @override
  List<Widget> buildActions(BuildContext context) {
    return [
      IconButton(
        icon: const Icon(Icons.clear),
        onPressed: () {
          query = '';
        },
      ),
    ];
  }

  @override
  Widget buildLeading(BuildContext context) {
    return IconButton(
      icon: const Icon(Icons.arrow_back),
      onPressed: () {
        close(context, '');
      },
    );
  }

  @override
  Widget buildResults(BuildContext context) {
    final provider = Provider.of<LinkProvider>(context, listen: false);
    provider.search(query);

    return Consumer<LinkProvider>(
      builder: (context, provider, child) {
        return LinkList(
          links: provider.links,
          onDelete: (id) => provider.deleteLink(id),
          onEdit: (link) {
            showDialog(
              context: context,
              builder: (context) => AddLinkDialog(
                isEditing: true,
                link: link,
              ),
            );
          },
          onDoubleTap: (link) {
            Clipboard.setData(ClipboardData(text: link.url));
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(
                content: Text('Link copied to clipboard: ${link.url}'),
                duration: const Duration(seconds: 2),
              ),
            );
          },
        );
      },
    );
  }

  @override
  Widget buildSuggestions(BuildContext context) {
    return const Center(
      child: Text('Type to search links by title, URL, description, or tags'),
    );
  }
}
