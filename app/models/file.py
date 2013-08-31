from schematics.models import Model
from schematics.types import StringType, IntType

class FileModel(Model):
  name = StringType()
  name.serialized_name = "File Name"

  size = IntType()  
  size.serialized_name = "File Size"

  content_type = StringType()
  content_type.serialized_name = "File Type"

  path = StringType()
  path.serialized_name =  "File Path"

