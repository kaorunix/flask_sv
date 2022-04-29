// import 'package:curl/curl.dart';
import 'package:http/http.dart';
import 'dart:convert';
import 'package:intl/intl.dart';
import 'package:intl/date_symbol_data_local.dart';
import 'dart:core';
import 'dart:math';
import 'package:json_annotation/json_annotation.dart';
part 'account_model.g.dart';

//final req1 = new Request("GET", "http://localhost:5000/api/account/search/");

//{
//print(toCurl(req1));
//}

/*
var response_sample = '''
{
  "body": [
    {
      "account_name": "accountA1", 
      "created_at": "2021-10-27 10:58:46", 
      "created_by": 999, 
      "end_on": "2021-12-31 00:00:00", 
      "id": "1470", 
      "start_on": "2021-09-01 00:00:00", 
      "status": "NEW", 
      "updated_at": "2022-02-11 16:43:16", 
      "updated_by": 50
    }, 
    {
      "account_name": "account121", 
      "created_at": "2021-10-27 20:14:48", 
      "created_by": 38, 
      "end_on": "2021-10-30 00:00:00", 
      "id": "1471", 
      "name": "account", 
      "start_on": "2021-10-06 00:00:00", 
      "status": "NEW", 
      "updated_at": "2022-02-11 23:25:18", 
      "updated_by": 50
    }, 
    {
      "account_name": "abc", 
      "created_at": "2022-02-11 23:25:54", 
      "created_by": 34, 
      "end_on": "2022-02-04 00:00:00", 
      "id": "1472", 
      "name": "account", 
      "start_on": "2022-02-05 00:00:00", 
      "status": "NEW", 
      "updated_at": "2022-02-11 23:25:54", 
      "updated_by": 34
    }
  ], 
  "status": {
    "code": "I0001", 
    "detail": "", 
    "message": "Found (3) records."
  }
}

''';

var response = jsonDecode(response_sample);

var accounts = response['body'];
*/

// List<Account> toListfromSearch(Map<String, dynamic> accountsOfSearch) {
//   var accountList = [];
//   var ac_json = json.decode(accountsOfSearch['body']);
//   ac_json.forEach((ac) =>
//     accountList.add(
//       Account(id: int.tryParse(ac['id'] ?? '0'),
//         account_name: (ac['account_name'] ?? 'no name'),
//         start_on: DateTime.tryParse(ac['start_on'] ?? '2022/01/01/00:00:00'),
//         end_on: DateTime.tryParse(ac['end_on'] ?? '2022/01/01/00:00:00'),
//         created_by: int.tryParse(ac['created_by'] ?? '0'),
//         created_at: DateTime.tryParse(ac['created_at'] ?? '2022/01/01/00:00:00'),
//         updated_by: int.tryParse(ac['updated_by'] ?? '0'),
//         updated_at: DateTime.tryParse(ac['updated_at'] ?? '2022/01/01/00:00:00'),
//         status: int.tryParse(ac['status'] ?? '0')
//       )
//     )
//   );
//   return accountList as List<Account>;

// }

@JsonSerializable(nullable: false)
class Account {
  final int id;
  final String account_name;
  final DateTime start_on;
  final DateTime end_on;
  final int created_by;
  final DateTime created_at;
  final int updated_by;
  final DateTime updated_at;
  final int status;

  Account({
      required this.id,
      required this.account_name,
      required this.start_on,
      required this.end_on,
      required this.created_by,
      required this.created_at,
      required this.updated_by,
      required this.updated_at,
      required this.status
  });
  factory Account.fromJson(Map<String, dynamic> json) => _$AccountFromJson(json);
  Map<String, dynamic> toJson() => _$AccountToJson(this);

  @override
  String toString() => json.encode(toJson());

}
