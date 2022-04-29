// import 'package:curl/curl.dart';
import 'package:http/http.dart';
import 'dart:convert';
import 'package:intl/intl.dart';
import 'package:intl/date_symbol_data_local.dart';
import 'dart:core';
import 'dart:math';
import 'package:json_annotation/json_annotation.dart';
part 'status.g.dart';

@JsonSerializable(nullable: false)
class RequestStatus {
  final String code;
  final String detail;
  final String message;

  RequestStatus({
      required this.code,
      required this.detail,
      required this.message
  });
  factory RequestStatus.fromJson(Map<String, dynamic> json) => _$RequestStatusFromJson(json);
  Map<String, dynamic> toJson() => _$RequestStatusToJson(this);

  @override
  String toString() => json.encode(toJson());
}
