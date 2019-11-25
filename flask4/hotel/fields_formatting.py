from flask_restful import fields

rooms_structure = {
    'number': fields.Integer,
    'level': fields.Integer,
    'status': fields.String,
    'price': fields.Float
}

address_structure = {
    'city': fields.String,
    'street': fields.String
}

tenants_structure = {
    'name': fields.String,
    'passport_id': fields.String,
    'age': fields.Integer,
    'sex': fields.String,
    'address': fields.Nested(address_structure),
    'room_number': fields.Integer
}

staff_structure = {
    'name': fields.String,
    'passport_id': fields.String,
    'position': fields.String,
    'salary': fields.Float
}
