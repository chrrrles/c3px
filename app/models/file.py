from schematics.models import Model
from schematics.types import StringType, IntType, UUIDType, EmailType, BooleanType

from .. lib.mongo import ObjectIdType


class FileModel(Model):
  filename = StringType(
    serialized_name = "File Name",
    max_length=255)

  size = IntType( 
    serialized_name = "File Size" ) 

  content_type = StringType(
    serialized_name = "File Type" )

  public_id = UUIDType(
    serialized_name = "Published Object ID" )

  object_id = ObjectIdType(
    serialized_name = 'Internal Object ID')

  owner = EmailType(
    serialized_name = "Owner ID")

  public = BooleanType (  
    default=True, 
    serialized_name = "Publicly Visible")

