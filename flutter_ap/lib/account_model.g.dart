// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'account_model.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Account _$AccountFromJson(Map<String, dynamic> json) => Account(
      id: json['id'] as int,
      account_name: json['account_name'] as String,
      start_on: DateTime.parse(json['start_on'] as String),
      end_on: DateTime.parse(json['end_on'] as String),
      created_by: json['created_by'] as int,
      created_at: DateTime.parse(json['created_at'] as String),
      updated_by: json['updated_by'] as int,
      updated_at: DateTime.parse(json['updated_at'] as String),
      status: json['status'] as String,
    );

Map<String, dynamic> _$AccountToJson(Account instance) => <String, dynamic>{
      'id': instance.id,
      'account_name': instance.account_name,
      'start_on': instance.start_on.toIso8601String(),
      'end_on': instance.end_on.toIso8601String(),
      'created_by': instance.created_by,
      'created_at': instance.created_at.toIso8601String(),
      'updated_by': instance.updated_by,
      'updated_at': instance.updated_at.toIso8601String(),
      'status': instance.status,
    };
