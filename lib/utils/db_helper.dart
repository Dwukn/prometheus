import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../models/link.dart';
import '../models/folder.dart';

class DBHelper {
  static Database? _db;

  static Future<void> initDB() async {
    if (_db != null) {
      return;
    }

    String path = join(await getDatabasesPath(), 'l_edger.db');
    _db = await openDatabase(
      path,
      version: 1,
      onCreate: (Database db, int version) async {
        await db.execute('''
          CREATE TABLE folders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            dateCreated TEXT
          )
        ''');

        await db.execute('''
          CREATE TABLE links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT,
            description TEXT,
            folderId TEXT,
            tags TEXT,
            dateAdded TEXT
          )
        ''');

        // Create default folder
        await db.insert('folders', {
          'name': 'Default',
          'dateCreated': DateTime.now().toIso8601String(),
        });
      },
    );
  }

  // Folder methods
  static Future<int> insertFolder(Folder folder) async {
    return await _db!.insert('folders', folder.toMap());
  }

  static Future<List<Folder>> getFolders() async {
    final List<Map<String, dynamic>> maps = await _db!.query('folders');
    return List.generate(maps.length, (i) => Folder.fromMap(maps[i]));
  }

  static Future<int> updateFolder(Folder folder) async {
    return await _db!.update(
      'folders',
      folder.toMap(),
      where: 'id = ?',
      whereArgs: [folder.id],
    );
  }

  static Future<int> deleteFolder(int id) async {
    return await _db!.delete(
      'folders',
      where: 'id = ?',
      whereArgs: [id],
    );
  }

  // Link methods
  static Future<int> insertLink(Link link) async {
    return await _db!.insert('links', link.toMap());
  }

  static Future<List<Link>> getLinks() async {
    final List<Map<String, dynamic>> maps = await _db!.query('links');
    return List.generate(maps.length, (i) => Link.fromMap(maps[i]));
  }

  static Future<List<Link>> getLinksByFolder(String folderId) async {
    final List<Map<String, dynamic>> maps = await _db!.query(
      'links',
      where: 'folderId = ?',
      whereArgs: [folderId],
    );
    return List.generate(maps.length, (i) => Link.fromMap(maps[i]));
  }

  static Future<List<Link>> searchLinks(String query) async {
    final List<Map<String, dynamic>> maps = await _db!.query(
      'links',
      where: 'title LIKE ? OR url LIKE ? OR description LIKE ? OR tags LIKE ?',
      whereArgs: ['%$query%', '%$query%', '%$query%', '%$query%'],
    );
    return List.generate(maps.length, (i) => Link.fromMap(maps[i]));
  }

  static Future<int> updateLink(Link link) async {
    return await _db!.update(
      'links',
      link.toMap(),
      where: 'id = ?',
      whereArgs: [link.id],
    );
  }

  static Future<int> deleteLink(int id) async {
    return await _db!.delete(
      'links',
      where: 'id = ?',
      whereArgs: [id],
    );
  }
}
