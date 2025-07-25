// folder_list.dart
import 'package:flutter/material.dart';
import '../models/folder.dart';
import '../providers/link_provider.dart';
import 'package:provider/provider.dart';

class FolderList extends StatelessWidget {
  final List<Folder> folders;
  final String currentFolderId;
  final Function(String) onFolderTap;

  const FolderList({
    Key? key,
    required this.folders,
    required this.currentFolderId,
    required this.onFolderTap,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: folders.length,
      itemBuilder: (context, index) {
        final folder = folders[index];
        bool isSelected = folder.id.toString() == currentFolderId;

        return ListTile(
          contentPadding: EdgeInsets.symmetric(horizontal: 16.0),
          title: Text(
            folder.name,
            style: TextStyle(
              fontWeight: FontWeight.w500,
              color: isSelected ? Colors.blueAccent : Colors.black,
            ),
          ),
          tileColor: isSelected ? Colors.blue.withOpacity(0.1) : null,
          selected: isSelected,
          onTap: () => onFolderTap(folder.id.toString()),
          leading: Icon(
            Icons.folder,
            color: isSelected ? Colors.blueAccent : Colors.grey,
          ),
          trailing: folder.id != 1
              ? IconButton(
                  icon: const Icon(Icons.delete),
                  onPressed: () {
                    _showDeleteDialog(context, folder);
                  },
                )
              : null,
        );
      },
    );
  }

  void _showDeleteDialog(BuildContext context, Folder folder) {
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
}
