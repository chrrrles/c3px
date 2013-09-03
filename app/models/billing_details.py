from schematics.models import Model
from schematics.types import EmailType

# just paypal for now
class BillingDetailsModel(Model):
  paypal_id = EmailType(
    required = True,
    serialized_name = "Paypal ID")
