from schematics.models import Model
from schematics.types.compound import ModelType

from address import AddressModel
from user import UserModel

class AdminModel(Model):
  user = ModelType(
    UserModel,
    required=True,
    serialized_name= "Admin Details")
