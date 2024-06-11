from marshmallow import fields
from schemas import ma

# Define the Employee schema
class EmployeeSchema(ma.Schema):
    id = fields.Integer(required=False) # id is autogenerated
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)

    # class Meta:
    #     fields = ("id", "name", "email", "phone", "username")

# Create instances of the schema
employee_input_schema = EmployeeSchema()
employee_output_schema = EmployeeSchema(exclude=["password"])
employees_schema = EmployeeSchema(many=True, exclude=["password"])
employee_login_schema = EmployeeSchema(only=["username", "password"])