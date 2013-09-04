from schematics.models import Model
from schematics.types import StringType, EmailType, DateTimeType, BooleanType

class UserModel(Model):
  firstname = StringType ( 
    default = '',
    serialized_name = "First Name",
    max_length = 40 )

  lastname = StringType ( 
    default='',
    serialized_name = "Last Name",
    max_length = 40 )

  email = EmailType ( 
    required=True, 
    serialized_name = "Email")
 
  password = StringType (
    required=True,
    min_length = 6,
    max_length = 30,
    serialized_name = "Password" )

  phone = StringType (  
    default = '',
    serialized_name = 'Phone Number',
    max_length=30 )

  date_create = DateTimeType(required=False)

  join_hash = StringType()

  activated = BooleanType (
    default = False,
    serialized_name = "Activated Account" )

