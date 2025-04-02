class Link {
  int? id;
  String title;
  String url;
  String? description;
  String folderId;
  List<String> tags;
  DateTime dateAdded;

  Link({
    this.id,
    required this.title,
    required this.url,
    this.description,
    required this.folderId,
    required this.tags,
    required this.dateAdded,
  });

  factory Link.fromMap(Map<String, dynamic> map) {
    return Link(
      id: map['id'],
      title: map['title'],
      url: map['url'],
      description: map['description'],
      folderId: map['folderId'],
      tags: (map['tags'] as String).split(',').where((tag) => tag.isNotEmpty).toList(),
      dateAdded: DateTime.parse(map['dateAdded']),
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'title': title,
      'url': url,
      'description': description,
      'folderId': folderId,
      'tags': tags.join(','),
      'dateAdded': dateAdded.toIso8601String(),
    };
  }
}
