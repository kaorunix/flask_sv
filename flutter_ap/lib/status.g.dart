// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'status.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RequestStatus _$RequestStatusFromJson(Map<String, dynamic> json) =>
    RequestStatus(
      code: json['code'] as String,
      detail: json['detail'] as String,
      message: json['message'] as String,
    );

Map<String, dynamic> _$RequestStatusToJson(RequestStatus instance) =>
    <String, dynamic>{
      'code': instance.code,
      'detail': instance.detail,
      'message': instance.message,
    };
