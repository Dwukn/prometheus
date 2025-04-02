// add_folder_form.dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/folder.dart';
import '../providers/link_provider.dart';

class AddFolderDialog extends StatefulWidget {
  const AddFolderDialog({Key? key}) : super(key: key);

  @override
  State<AddFolderDialog> createState() => _AddFolderDialogState();
}

class _AddFolderDialogState extends State<AddFolderDialog> {
  final _formKey = GlobalKey<FormState>();
  final _nameController = TextEditingController();

  @override
  void dispose() {
    _nameController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      elevation: 10, // Elevate the dialog
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12), // Rounded corners for the dialog
      ),
      title: const Text(
        'Add Folder',
        style: TextStyle(
          fontSize: 18,
          fontWeight: FontWeight.bold,
          color: Colors.blueAccent,
        ),
      ),
      content: Padding(
        padding: const EdgeInsets.symmetric(vertical: 10),
        child: Form(
          key: _formKey,
          child: TextFormField(
            controller: _nameController,
            decoration: InputDecoration(
              labelText: 'Folder Name',
              labelStyle: TextStyle(color: Colors.blueAccent),
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(8), // Rounded corners for the text field
              ),
              focusedBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(8),
                borderSide: BorderSide(color: Colors.blueAccent, width: 2),
              ),
            ),
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter a folder name';
              }
              return null;
            },
          ),
        ),
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context),
          child: const Text(
            'CANCEL',
            style: TextStyle(color: Colors.red),
          ),
        ),
        ElevatedButton(
  onPressed: () {
    if (_formKey.currentState!.validate()) {
      final provider = Provider.of<LinkProvider>(context, listen: false);
      final newFolder = Folder(
        name: _nameController.text,
        dateCreated: DateTime.now(),
      );
      provider.addFolder(newFolder);
      Navigator.pop(context);
      // Show a snack bar for feedback
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Folder added successfully!')),
      );
    }
  },
  style: ElevatedButton.styleFrom(
    backgroundColor: Colors.blueAccent, // Corrected parameter name
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(8), // Rounded button corners
    ),
  ),
  child: const Text(
    'ADD',
    style: TextStyle(color: Colors.white),
  ),
)

      ],
    );
  }
}
