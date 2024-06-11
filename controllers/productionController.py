from flask import request, jsonify
from schemas.productionSchema import production_schema, productions_schema
from services import productionService
from marshmallow import ValidationError
# from auth import token_auth


# @token_auth.login_required(role="admin")
def save():
    try:
        production_data = production_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    new_production = productionService.save(production_data)

    return production_schema.jsonify(new_production), 201


def find_all():
    # Get any request query params aka args
    args = request.args
    page = args.get('page', 1, type=int)
    # print('The page arg is:', page, 'and the type is', type(page))
    per_page = args.get('per_page', 10, type=int)
    search_term = args.get('search')
    productions = productionService.find_all(page, per_page, search_term)
    return productions_schema.jsonify(productions)
