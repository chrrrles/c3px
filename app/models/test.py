from schematics.models import Model
from schematics.types import StringType

class TestModel(Model): 
  content = StringType()
