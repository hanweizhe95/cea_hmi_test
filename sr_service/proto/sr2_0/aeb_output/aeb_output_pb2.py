# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sr_service/proto/sr2_0/aeb_output/aeb_output.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2sr_service/proto/sr2_0/aeb_output/aeb_output.proto\x12\x12xpilot.sr2_0.proto\"\xd8\x01\n\x17\x41\x65\x62OutputTargetInfoType\x12\x0b\n\x03ttc\x18\x01 \x01(\x02\x12\x15\n\rtarget_dist_x\x18\x02 \x01(\x02\x12\x15\n\rtarget_dist_y\x18\x03 \x01(\x02\x12\x14\n\x0ctarget_vel_x\x18\x04 \x01(\x02\x12\x14\n\x0ctarget_vel_y\x18\x05 \x01(\x02\x12\x12\n\ntarget_yaw\x18\x06 \x01(\x02\x12\x11\n\ttarget_id\x18\x07 \x01(\x04\x12\x1a\n\x12target_object_type\x18\x08 \x01(\x04\x12\x13\n\x0bscenes_type\x18\t \x01(\x04\"o\n ActiveSafetyOutputTargetTopicMsg\x12K\n\x16\x61\x65\x62_output_target_info\x18\x01 \x01(\x0b\x32+.xpilot.sr2_0.proto.AebOutputTargetInfoTypeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sr_service.proto.sr2_0.aeb_output.aeb_output_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_AEBOUTPUTTARGETINFOTYPE']._serialized_start=75
  _globals['_AEBOUTPUTTARGETINFOTYPE']._serialized_end=291
  _globals['_ACTIVESAFETYOUTPUTTARGETTOPICMSG']._serialized_start=293
  _globals['_ACTIVESAFETYOUTPUTTARGETTOPICMSG']._serialized_end=404
# @@protoc_insertion_point(module_scope)
