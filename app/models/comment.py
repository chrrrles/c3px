from schematics.models import Model
from schematics.types import StringType, DateTimeType, BooleanType
from schematics.types.compound import ModelType
from user import UserModel # this is the 'poster'

class CommentModel(Model):
  timestamp = DateTimeType(
    required=True, 
    serialized_name="Comment Date")

  comment = StringType(
    required=True,
    serialized_name = "Comment" )

  commenter = ModelType(
    UserModel, 
    serialized_name="Commenter" )
    
  active = BooleanType(default=True)  # so commenter or admin can soft-delete messages
