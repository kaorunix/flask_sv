// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'account_request.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AccountRequest _$AccountRequestFromJson(Map<String, dynamic> json) =>
    AccountRequest(
      body: (json['body'] as List<dynamic>)
          .map((e) => Account.fromJson(e as Map<String, dynamic>))
          .toList(),
      status: RequestStatus.fromJson(json['status'] as Map<String, dynamic>),
    );

Map<String, dynamic> _$AccountRequestToJson(AccountRequest instance) =>
    <String, dynamic>{
      'body': instance.body,
      'status': instance.status,
    };
