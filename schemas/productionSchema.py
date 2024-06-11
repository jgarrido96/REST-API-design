from marshmallow import fields, validate
from schemas import ma


# For Creating a new Production
class ProductionSchema(ma.Schema):
    id = fields.Integer(required=False) # id is autogenerated
    name = fields.String(required=True, validate=validate.Length(min=5, max=20)) # Production Name must be between 5 and 20 characters
    price = fields.Float(required=True, validate=validate.Range(min=0)) # Production Price must be >= 0

    class Meta:
        fields = ("id", "name", "price")

# For adding productions to Order
class ProductionIdSchema(ma.Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=False)
    price = fields.String(required=False)


# Create an instance of the ProductionSchema
production_schema = ProductionSchema()
productions_schema = ProductionSchema(many=True) # For handling multiple productions