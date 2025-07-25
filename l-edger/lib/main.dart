import 'package:flutter/material.dart';
import 'package:l_edger/screens/home_screen.dart';
import 'package:l_edger/providers/link_provider.dart';
import 'package:provider/provider.dart';
import 'package:l_edger/utils/db_helper.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await DBHelper.initDB();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => LinkProvider(),
      child: MaterialApp(
        title: 'Link Manager',
        theme: ThemeData(
          primarySwatch: Colors.blue,
          visualDensity: VisualDensity.adaptivePlatformDensity,
        ),
        home: const HomeScreen(),
      ),
    );
  }
}
