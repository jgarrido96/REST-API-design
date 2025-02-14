from marshmallow import fields
from schemas import ma

# Define the Order schema
class OrderSchema(ma.Schema):
    id = fields.Integer(required=False) # id is autogenerated
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)

    # class Meta:
    #     fields = ("id", "name", "email", "phone", "username")

# Create instances of the schema
order_schema = OrderSchema()
# order_output_schema = OrderSchema(exclude=["password"])
orders_schema = OrderSchema(many=True) # , exclude=["password"])
# order_login_schema = OrderSchema(only=["username", "password"])