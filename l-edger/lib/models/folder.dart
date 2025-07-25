class Folder {
  int? id;
  String name;
  DateTime dateCreated;

  Folder({
    this.id,
    required this.name,
    required this.dateCreated,
  });

  factory Folder.fromMap(Map<String, dynamic> map) {
    return Folder(
      id: map['id'],
      name: map['name'],
      dateCreated: DateTime.parse(map['dateCreated']),
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'name': name,
      'dateCreated': dateCreated.toIso8601String(),
    };
  }
}
