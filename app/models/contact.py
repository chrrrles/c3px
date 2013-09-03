from schematics.models import Model
from schematics.types import StringType, EmailType

class UserModel(Model):
  firstname = StringType ( required=True )
  firstname.serialized_name = "First Name"
  firstname.max_length = 40

  lastname = StringType ( required=True )
  lastname.serialized_name = "Last Name"
  lastname.max_length = 40

  email = EmailType ( required=True ) 
  email.serialized_name = "Email"

  phone = StringType (  
    required=False,
    serialized_name = 'Phone Number',
    max_length=30 )

