import 'package:flutter/material.dart';
import 'account_list.dart';
import 'listWidget.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

late Row account1 = Row(
    children: <Widget> [
      Container(
        color: Colors.grey, width: 50.0, height: 40.0,
        child: Text("id", style: TextStyle(fontSize:16.0, color: const Color(0xff000000), fontWeight: FontWeight.w400, fontFamily: "Roboto"))
      ),
      Container(
          color: Colors.grey, width: 150.0, height: 40.0,
        child: Text("name", style: TextStyle(fontSize:16.0, color: const Color(0xff000000), fontWeight: FontWeight.w400, fontFamily: "Roboto"))
      ),
      Container(
          color: Colors.grey, width: 150.0, height: 40.0,
          child: Text("name", style: TextStyle(fontSize:16.0, color: const Color(0xff000000), fontWeight: FontWeight.w400, fontFamily: "Roboto"))
      )
    ]
);

class _MyHomePageState extends State<MyHomePage> with TickerProviderStateMixin {
  late TabController _tabController;



  final ListView account_area =
    ListView(
      shrinkWrap: true,
      padding: const EdgeInsets.all(20.0),
          children: <Widget>[
            createTitleRow(account_title),
            new Container(
              child: Text('account', style: TextStyle(fontSize: 50)),
              padding: const EdgeInsets.all(10.0),
              alignment: Alignment.bottomCenter,
            ),
            new Container(
              child: Text('account2', style: TextStyle(fontSize: 50)),
              padding: const EdgeInsets.all(10.0),
              alignment: Alignment.bottomCenter,
            ),
            new Container(
              //alignment: Aligment.bottomCenter,
              child: account1,
              padding: const EdgeInsets.all(10.0),
            )
          ],
    );
//  Text account_area = Text('account', style: TextStyle(fontSize: 50));


  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 3, vsync: this);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('flask_sv'),
        bottom: TabBar(
          controller: _tabController,
          tabs: const <Widget>[
            Tab(icon: Icon(Icons.account_box_rounded)),
            Tab(icon: Icon(Icons.beach_access_sharp)),
            Tab(icon: Icon(Icons.account_balance_outlined)),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: <Widget>[
          Center(child: account_area),
          Center(child: Text('group', style: TextStyle(fontSize: 50))),
          Center(child: Text('晴れ', style: TextStyle(fontSize: 50))),
        ],
      ),
    );
  }
}