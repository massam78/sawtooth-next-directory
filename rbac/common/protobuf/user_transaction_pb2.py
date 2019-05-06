# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_transaction.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16user_transaction.proto\"\xef\x01\n\x18ProposeUpdateUserManager\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07next_id\x18\x02 \x01(\t\x12\x16\n\x0enew_manager_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x39\n\x08metadata\x18\x05 \x03(\x0b\x32\'.ProposeUpdateUserManager.MetadataEntry\x12\x19\n\x11\x61ssigned_approver\x18\x06 \x03(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xfd\x01\n\nCreateUser\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0f\n\x07next_id\x18\x03 \x01(\t\x12\x12\n\nmanager_id\x18\x04 \x01(\t\x12+\n\x08metadata\x18\x05 \x03(\x0b\x32\x19.CreateUser.MetadataEntry\x12\r\n\x05\x65mail\x18\x06 \x01(\t\x12\x0b\n\x03key\x18\x07 \x01(\t\x12\x14\n\x0c\x63reated_date\x18\x08 \x01(\x03\x12\x1a\n\x12\x64istinguished_name\x18\t \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x92\x02\n\x0bImportsUser\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0f\n\x07next_id\x18\x03 \x01(\t\x12\x12\n\nmanager_id\x18\x04 \x01(\t\x12,\n\x08metadata\x18\x05 \x03(\x0b\x32\x1a.ImportsUser.MetadataEntry\x12\r\n\x05\x65mail\x18\x06 \x01(\t\x12\x11\n\tremote_id\x18\x07 \x01(\t\x12\x0b\n\x03key\x18\x08 \x01(\t\x12\x14\n\x0c\x63reated_date\x18\t \x01(\x03\x12\x1a\n\x12\x64istinguished_name\x18\n \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xbe\x01\n\nUpdateUser\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0f\n\x07next_id\x18\x03 \x01(\t\x12\x12\n\nmanager_id\x18\x04 \x01(\t\x12+\n\x08metadata\x18\x05 \x03(\x0b\x32\x19.UpdateUser.MetadataEntry\x12\r\n\x05\x65mail\x18\x06 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1d\n\nDeleteUser\x12\x0f\n\x07next_id\x18\x01 \x01(\tb\x06proto3')
)




_PROPOSEUPDATEUSERMANAGER_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='ProposeUpdateUserManager.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ProposeUpdateUserManager.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ProposeUpdateUserManager.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=266,
)

_PROPOSEUPDATEUSERMANAGER = _descriptor.Descriptor(
  name='ProposeUpdateUserManager',
  full_name='ProposeUpdateUserManager',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='ProposeUpdateUserManager.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_id', full_name='ProposeUpdateUserManager.next_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_manager_id', full_name='ProposeUpdateUserManager.new_manager_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ProposeUpdateUserManager.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ProposeUpdateUserManager.metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assigned_approver', full_name='ProposeUpdateUserManager.assigned_approver', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PROPOSEUPDATEUSERMANAGER_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=266,
)


_CREATEUSER_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='CreateUser.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='CreateUser.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='CreateUser.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=266,
)

_CREATEUSER = _descriptor.Descriptor(
  name='CreateUser',
  full_name='CreateUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CreateUser.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='CreateUser.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_id', full_name='CreateUser.next_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manager_id', full_name='CreateUser.manager_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='CreateUser.metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='CreateUser.email', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='CreateUser.key', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_date', full_name='CreateUser.created_date', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distinguished_name', full_name='CreateUser.distinguished_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATEUSER_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=522,
)


_IMPORTSUSER_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='ImportsUser.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ImportsUser.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ImportsUser.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=266,
)

_IMPORTSUSER = _descriptor.Descriptor(
  name='ImportsUser',
  full_name='ImportsUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ImportsUser.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='ImportsUser.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_id', full_name='ImportsUser.next_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manager_id', full_name='ImportsUser.manager_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ImportsUser.metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='ImportsUser.email', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_id', full_name='ImportsUser.remote_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='ImportsUser.key', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_date', full_name='ImportsUser.created_date', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distinguished_name', full_name='ImportsUser.distinguished_name', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_IMPORTSUSER_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=525,
  serialized_end=799,
)


_UPDATEUSER_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='UpdateUser.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='UpdateUser.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='UpdateUser.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=266,
)

_UPDATEUSER = _descriptor.Descriptor(
  name='UpdateUser',
  full_name='UpdateUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='UpdateUser.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='UpdateUser.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_id', full_name='UpdateUser.next_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manager_id', full_name='UpdateUser.manager_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='UpdateUser.metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='UpdateUser.email', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEUSER_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=802,
  serialized_end=992,
)


_DELETEUSER = _descriptor.Descriptor(
  name='DeleteUser',
  full_name='DeleteUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_id', full_name='DeleteUser.next_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=994,
  serialized_end=1023,
)

_PROPOSEUPDATEUSERMANAGER_METADATAENTRY.containing_type = _PROPOSEUPDATEUSERMANAGER
_PROPOSEUPDATEUSERMANAGER.fields_by_name['metadata'].message_type = _PROPOSEUPDATEUSERMANAGER_METADATAENTRY
_CREATEUSER_METADATAENTRY.containing_type = _CREATEUSER
_CREATEUSER.fields_by_name['metadata'].message_type = _CREATEUSER_METADATAENTRY
_IMPORTSUSER_METADATAENTRY.containing_type = _IMPORTSUSER
_IMPORTSUSER.fields_by_name['metadata'].message_type = _IMPORTSUSER_METADATAENTRY
_UPDATEUSER_METADATAENTRY.containing_type = _UPDATEUSER
_UPDATEUSER.fields_by_name['metadata'].message_type = _UPDATEUSER_METADATAENTRY
DESCRIPTOR.message_types_by_name['ProposeUpdateUserManager'] = _PROPOSEUPDATEUSERMANAGER
DESCRIPTOR.message_types_by_name['CreateUser'] = _CREATEUSER
DESCRIPTOR.message_types_by_name['ImportsUser'] = _IMPORTSUSER
DESCRIPTOR.message_types_by_name['UpdateUser'] = _UPDATEUSER
DESCRIPTOR.message_types_by_name['DeleteUser'] = _DELETEUSER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProposeUpdateUserManager = _reflection.GeneratedProtocolMessageType('ProposeUpdateUserManager', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _PROPOSEUPDATEUSERMANAGER_METADATAENTRY,
    __module__ = 'user_transaction_pb2'
    # @@protoc_insertion_point(class_scope:ProposeUpdateUserManager.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _PROPOSEUPDATEUSERMANAGER,
  __module__ = 'user_transaction_pb2'
  # @@protoc_insertion_point(class_scope:ProposeUpdateUserManager)
  ))
_sym_db.RegisterMessage(ProposeUpdateUserManager)
_sym_db.RegisterMessage(ProposeUpdateUserManager.MetadataEntry)

CreateUser = _reflection.GeneratedProtocolMessageType('CreateUser', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _CREATEUSER_METADATAENTRY,
    __module__ = 'user_transaction_pb2'
    # @@protoc_insertion_point(class_scope:CreateUser.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _CREATEUSER,
  __module__ = 'user_transaction_pb2'
  # @@protoc_insertion_point(class_scope:CreateUser)
  ))
_sym_db.RegisterMessage(CreateUser)
_sym_db.RegisterMessage(CreateUser.MetadataEntry)

ImportsUser = _reflection.GeneratedProtocolMessageType('ImportsUser', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _IMPORTSUSER_METADATAENTRY,
    __module__ = 'user_transaction_pb2'
    # @@protoc_insertion_point(class_scope:ImportsUser.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _IMPORTSUSER,
  __module__ = 'user_transaction_pb2'
  # @@protoc_insertion_point(class_scope:ImportsUser)
  ))
_sym_db.RegisterMessage(ImportsUser)
_sym_db.RegisterMessage(ImportsUser.MetadataEntry)

UpdateUser = _reflection.GeneratedProtocolMessageType('UpdateUser', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _UPDATEUSER_METADATAENTRY,
    __module__ = 'user_transaction_pb2'
    # @@protoc_insertion_point(class_scope:UpdateUser.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _UPDATEUSER,
  __module__ = 'user_transaction_pb2'
  # @@protoc_insertion_point(class_scope:UpdateUser)
  ))
_sym_db.RegisterMessage(UpdateUser)
_sym_db.RegisterMessage(UpdateUser.MetadataEntry)

DeleteUser = _reflection.GeneratedProtocolMessageType('DeleteUser', (_message.Message,), dict(
  DESCRIPTOR = _DELETEUSER,
  __module__ = 'user_transaction_pb2'
  # @@protoc_insertion_point(class_scope:DeleteUser)
  ))
_sym_db.RegisterMessage(DeleteUser)


_PROPOSEUPDATEUSERMANAGER_METADATAENTRY._options = None
_CREATEUSER_METADATAENTRY._options = None
_IMPORTSUSER_METADATAENTRY._options = None
_UPDATEUSER_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
