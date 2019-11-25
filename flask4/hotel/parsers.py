from flask_restful import reqparse

default_config = {
    'action': 'append',
    'location': ['args', 'form', 'json']
}

rooms_parser = reqparse.RequestParser(bundle_errors=True)
rooms_parser.add_argument('number', type=int, **default_config)
rooms_parser.add_argument('level', type=int, **default_config)
rooms_parser.add_argument('status', type=str, **default_config)
rooms_parser.add_argument('price', type=float, **default_config)

tenants_parser = reqparse.RequestParser(bundle_errors=True)
tenants_parser.add_argument('name', type=str, **default_config)
tenants_parser.add_argument('passport_id', type=str, **default_config)
tenants_parser.add_argument('age', type=int, **default_config)
tenants_parser.add_argument('sex', type=str, **default_config)
tenants_parser.add_argument('city', type=str, **default_config)
tenants_parser.add_argument('street', type=str, **default_config)
tenants_parser.add_argument('room_number', type=int, **default_config)

staff_parser = reqparse.RequestParser(bundle_errors=True)
staff_parser.add_argument('name', type=str, **default_config)
staff_parser.add_argument('passport_id', type=str, **default_config)
staff_parser.add_argument('position', type=str, **default_config)
staff_parser.add_argument('salary', type=float, **default_config)
