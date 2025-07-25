// add_link_form.dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/link.dart';
import '../providers/link_provider.dart';

class AddLinkDialog extends StatefulWidget {
  final bool isEditing;
  final Link? link;

  const AddLinkDialog({
    Key? key,
    this.isEditing = false,
    this.link,
  }) : super(key: key);

  @override
  State<AddLinkDialog> createState() => _AddLinkDialogState();
}

class _AddLinkDialogState extends State<AddLinkDialog> {
  final _formKey = GlobalKey<FormState>();
  late TextEditingController _titleController;
  late TextEditingController _urlController;
  late TextEditingController _descriptionController;
  late TextEditingController _tagsController;
  String _selectedFolderId = '1';

  @override
  void initState() {
    super.initState();
    _titleController = TextEditingController(text: widget.link?.title ?? '');
    _urlController = TextEditingController(text: widget.link?.url ?? '');
    _descriptionController =
        TextEditingController(text: widget.link?.description ?? '');
    _tagsController = TextEditingController(
        text: widget.link?.tags.join(', ') ?? '');
    _selectedFolderId = widget.link?.folderId ??
        Provider.of<LinkProvider>(context, listen: false).currentFolderId;
  }

  @override
  void dispose() {
    _titleController.dispose();
    _urlController.dispose();
    _descriptionController.dispose();
    _tagsController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      elevation: 10,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12), // Rounded corners for dialog
      ),
      title: Text(
        widget.isEditing ? 'Edit Link' : 'Add Link',
        style: TextStyle(
          fontSize: 18,
          fontWeight: FontWeight.bold,
          color: Colors.blueAccent,
        ),
      ),
      content: SingleChildScrollView(
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              _buildTextField(
                controller: _titleController,
                label: 'Title',
                validator: (value) => value?.isEmpty ?? true
                    ? 'Please enter a title'
                    : null,
              ),
              const SizedBox(height: 16),
              _buildTextField(
                controller: _urlController,
                label: 'URL',
                validator: (value) {
                  if (value?.isEmpty ?? true) {
                    return 'Please enter a URL';
                  }
                  if (!Uri.parse(value!).isAbsolute) {
                    return 'Please enter a valid URL';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              _buildTextField(
                controller: _descriptionController,
                label: 'Description (optional)',
                maxLines: 3,
              ),
              const SizedBox(height: 16),
              _buildTextField(
                controller: _tagsController,
                label: 'Tags (comma separated)',
                hintText: 'e.g. work, reference, tutorial',
              ),
              const SizedBox(height: 16),
              Consumer<LinkProvider>(
                builder: (context, provider, child) {
                  return DropdownButtonFormField<String>(
                    decoration: const InputDecoration(
                      labelText: 'Folder',
                      border: OutlineInputBorder(),
                    ),
                    value: _selectedFolderId,
                    items: provider.folders.map((folder) {
                      return DropdownMenuItem<String>(
                        value: folder.id.toString(),
                        child: Text(folder.name),
                      );
                    }).toList(),
                    onChanged: (value) {
                      setState(() {
                        _selectedFolderId = value!;
                      });
                    },
                  );
                },
              ),
            ],
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

              final tags = _tagsController.text
                  .split(',')
                  .map((tag) => tag.trim())
                  .where((tag) => tag.isNotEmpty)
                  .toList();

              if (widget.isEditing && widget.link != null) {
                final updatedLink = Link(
                  id: widget.link!.id,
                  title: _titleController.text,
                  url: _urlController.text,
                  description: _descriptionController.text,
                  folderId: _selectedFolderId,
                  tags: tags,
                  dateAdded: widget.link!.dateAdded,
                );
                provider.updateLink(updatedLink);
              } else {
                final newLink = Link(
                  title: _titleController.text,
                  url: _urlController.text,
                  description: _descriptionController.text,
                  folderId: _selectedFolderId,
                  tags: tags,
                  dateAdded: DateTime.now(),
                );
                provider.addLink(newLink);
              }

              // Show a SnackBar for success
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(content: Text(widget.isEditing ? 'Link updated!' : 'Link added!')),
              );

              Navigator.pop(context);
            }
          },
          child: Text(widget.isEditing ? 'UPDATE' : 'ADD'),
          style: ElevatedButton.styleFrom(
    backgroundColor: Colors.blueAccent, // This is the correct way now
                shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(8),
            ),
            padding: EdgeInsets.symmetric(vertical: 12, horizontal: 20),
          ),
        ),
      ],
    );
  }

  Widget _buildTextField({
    required TextEditingController controller,
    required String label,
    int maxLines = 1,
    String? hintText,
    String? Function(String?)? validator,
  }) {
    return TextFormField(
      controller: controller,
      decoration: InputDecoration(
        labelText: label,
        hintText: hintText,
        border: OutlineInputBorder(),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
          borderSide: BorderSide(color: Colors.blueAccent),
        ),
      ),
      maxLines: maxLines,
      validator: validator,
    );
  }
}
