import 'package:flutter/material.dart';
import '../providers/link_provider.dart';

// This extension adds functionality to the existing LinkProvider without modifying it
extension LinkProviderExtension on LinkProvider {
  // Check if the current folder ID is the home view
  bool get isHomeView => currentFolderId == "home_view";

  // Set the current folder to home view or specific folder
  void goToHomeView() {
    setCurrentFolder("home_view");
  }
}
