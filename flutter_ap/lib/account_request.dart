// import 'package:curl/curl.dart';
import 'package:http/http.dart';
import 'dart:convert';
import 'package:intl/intl.dart';
import 'package:intl/date_symbol_data_local.dart';
import 'dart:core';
import 'dart:math';
import 'package:json_annotation/json_annotation.dart';
import 'package:flutter_ap/account_model.dart';
import 'package:flutter_ap/status.dart';
part 'account_request.g.dart';

/*
List<Account> toListfromSearch(List<Map<String, Map<String, String>>> accountsOfSearch) {
  var accountList = [];
  var ac_json = accountsOfSearch['body'];
  ac_json.forEach((ac) =>
    accountList.add(
      Account(id: int.tryParse(ac['id'] ?? '0'),
        account_name: (ac['account_name'] ?? 'no name'),
        start_on: DateTime.tryParse(ac['start_on'] ?? '2022/01/01/00:00:00'),
        end_on: DateTime.tryParse(ac['end_on'] ?? '2022/01/01/00:00:00'),
        created_by: int.tryParse(ac['created_by'] ?? '0'),
        created_at: DateTime.tryParse(ac['created_at'] ?? '2022/01/01/00:00:00'),
        updated_by: int.tryParse(ac['updated_by'] ?? '0'),
        updated_at: DateTime.tryParse(ac['updated_at'] ?? '2022/01/01/00:00:00'),
        status: int.tryParse(ac['status'] ?? '0')
      )
    )
  );
  return accountList as List<Account>;

}
*/

@JsonSerializable(nullable: false)
class AccountRequest {
  final List<Account> body;
  final RequestStatus status;

  AccountRequest({
      required this.body,
      required this.status
  });
  factory AccountRequest.fromJson(Map<String, dynamic> json) => _$AccountRequestFromJson(json);
  Map<String, dynamic> toJson() => _$AccountRequestToJson(this);

  @override
  String toString() => json.encode(toJson());

}
