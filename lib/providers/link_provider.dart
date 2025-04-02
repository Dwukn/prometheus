import 'package:flutter/foundation.dart';
import '../models/link.dart';
import '../models/folder.dart';
import '../utils/db_helper.dart';

class LinkProvider with ChangeNotifier {
  List<Link> _links = [];
  List<Folder> _folders = [];
  String _currentFolderId = '1';
  String _searchQuery = '';

  List<Link> get links => _links;
  List<Folder> get folders => _folders;
  String get currentFolderId => _currentFolderId;
  String get searchQuery => _searchQuery;

  LinkProvider() {
    _fetchFolders();
    _fetchLinks();
  }
  

  Future<void> _fetchFolders() async {
    _folders = await DBHelper.getFolders();
    notifyListeners();
  }

  Future<void> _fetchLinks() async {
    if (_searchQuery.isEmpty) {
      _links = await DBHelper.getLinksByFolder(_currentFolderId);
    } else {
      _links = await DBHelper.searchLinks(_searchQuery);
    }
    notifyListeners();
  }

  void setCurrentFolder(String id) {
    _currentFolderId = id;
    _searchQuery = '';
    _fetchLinks();
  }

  void search(String query) {
    _searchQuery = query;
    _fetchLinks();
  }

  Future<void> addLink(Link link) async {
    await DBHelper.insertLink(link);
    _fetchLinks();
  }

  Future<void> updateLink(Link link) async {
    await DBHelper.updateLink(link);
    _fetchLinks();
  }

  Future<void> deleteLink(int id) async {
    await DBHelper.deleteLink(id);
    _fetchLinks();
  }

  Future<void> addFolder(Folder folder) async {
    await DBHelper.insertFolder(folder);
    _fetchFolders();
  }

  Future<void> updateFolder(Folder folder) async {
    await DBHelper.updateFolder(folder);
    _fetchFolders();
  }

  Future<void> deleteFolder(int id) async {
    await DBHelper.deleteFolder(id);
    // Move links to default folder
    final linksToMove = _links.where((link) => link.folderId == id.toString()).toList();
    for (var link in linksToMove) {
      link.folderId = '1';
      await DBHelper.updateLink(link);
    }
    _fetchFolders();
    _fetchLinks();
  }

  List<String> getAllTags() {
    Set<String> allTags = {};
    for (var link in _links) {
      allTags.addAll(link.tags);
    }
    return allTags.toList();
  }

  List<Link> getLinksByTag(String tag) {
    return _links.where((link) => link.tags.contains(tag)).toList();
  }
}
