//import 'package:test/test.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_ap/account_model.dart';
import 'package:intl/intl.dart';
import 'dart:convert';
import 'package:flutter_ap/account_request.dart';
import 'package:flutter_ap/status.dart';

void main() {
  var account_name = "account_sample";
  var created_at = "2000-10-27 10:58:46"; 
  var created_by = 9;
  var end_on = "2021-12-31 00:00:00";
  var id = 199;
  var start_on = "2021-09-01 00:00:00"; 
  var status = "NEW";
  var updated_at = "2022-02-11 16:43:16";
  var updated_by = 19;
  var status_sample = '''
{
    "code": "I0001", 
    "detail": "ABC", 
    "message": "Found (2) records."
}
''';

var status_a = RequestStatus(
  code: "I0001",
  detail: "ABC",
  message: "Found (2) records.");
  var response_sample = '''
{
  "body": [
    {
      "name": "account", 
      "account_name": "accountJ1", 
      "created_at": "2001-10-27 10:58:46", 
      "created_by": 99, 
      "end_on": "2001-12-31 00:00:00", 
      "id": "91", 
      "start_on": "2001-09-01 00:00:00", 
      "status": "NEW", 
      "updated_at": "2002-02-11 16:43:16", 
      "updated_by": 51
    }, 
    {
      "name": "account", 
      "account_name": "accountJ2", 
      "created_at": "2001-10-27 20:14:48", 
      "created_by": 38, 
      "end_on": "2001-10-30 00:00:00", 
      "id": "92", 
      "start_on": "2001-10-06 00:00:00", 
      "status": "NEW", 
      "updated_at": "2002-02-11 23:25:18", 
      "updated_by": 51
    }, 
  }
  "status": {
    "code": "I0001", 
    "detail": "", 
    "message": "Found (2) records."
  }
}

''';

   final ac1 = Account(
     account_name: "accountJ1", 
     created_at: DateTime.parse("2001-10-27 10:58:46"),
     created_by: 99, 
     end_on: DateTime.parse("2001-12-31 00:00:00"), 
     id: 91, 
     start_on: DateTime.parse("2001-09-01 00:00:00"), 
     status: 1, 
     updated_at: DateTime.parse("2002-02-11 16:43:16"), 
     updated_by: 51
   );

   final ac2 = Account(
     account_name: "accountJ2", 
     created_at: DateTime.parse("2001-10-27 20:14:48"), 
     created_by: 38, 
     end_on: DateTime.parse("2001-10-30 00:00:00"), 
     id: 92, 
     start_on: DateTime.parse("2001-10-06 00:00:00"), 
     status: 1, 
     updated_at: DateTime.parse("2002-02-11 23:25:18"), 
     updated_by: 51
   );

   setUp(() {});

   group('AccountModel test', () {
       test("status", () {
           var status = RequestStatus.fromJson(json.decode(status_sample));
           print(status);
           print(status_a);
           expect(status, equals(status_a));
       });
//       test("parametors of constructor", () {
//           var a = jsonDecode(response_sample);
//           print(a);
//           var acs = toListfromSearch(a);
           // var acs = toListfromSearch((jsonDecode(response_sample)).cast<Map<String, dynamic>>);
//           expect(acs, [ac1, ac2]);
//      });
  });
}
