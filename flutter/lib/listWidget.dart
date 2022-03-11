import 'package:flutter/material.dart';

Row createTitleRow(List<String> titles) { 
  //list = <Widget>[];

  return Row(
    children: titles.map((String s) =>
      Container(
        color: Colors.grey, width: s.length * 2.0, height: 40.0,
        child: Text("id", style: TextStyle(fontSize:16.0, color: const Color(0xff000000), fontWeight: FontWeight.w400, fontFamily: "Roboto"))
      )
    ).toList()
  );
}
