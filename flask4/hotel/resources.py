import sqlite3
from flask_restful import Resource, marshal_with, abort
from hotel import db_utils as du
from hotel.base_classes import *
from hotel.parsers import *
from hotel.fields_formatting import *
from hotel.fields_check import *


class Rooms(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        args = rooms_parser.parse_args(strict=True)
        if not any(args.values()):
            return [Room(*x[1:]) for x in du.get_all('Rooms')]
        for key, value in args.items():
            if value:
                return [Room(*x[1:]) for x in
                        du.get_with_filter('Rooms', key, value)]

    def post(self):
        args = rooms_parser.parse_args(strict=True)
        check_if_all_parameters_is_filled(args)
        check_if_value_is_positive('number', args)
        check_if_value_is_positive('level', args)
        check_if_value_is_positive('price', args)
        try:
            du.add_new_item('Rooms', args)
        except sqlite3.IntegrityError:
            abort(409, error_code=409,
                  message=f'Room {args["number"][0]} is already exists!')
        return f'New room {args["number"][0]} was successfully added'

    def put(self):
        args = rooms_parser.parse_args(strict=True)
        check_if_key_in_args('number', args, 'room')
        check_if_value_is_positive('number', args)
        check_if_value_is_positive('level', args)
        check_if_value_is_positive('price', args)
        keys = [key for key in args.keys() if args[key]]
        values = [value for value in args.values() if value]
        result = du.update_item('Rooms', keys, values, 'number',
                                args['number'][0])
        check_if_row_was_affected(result, 'Room', args["number"][0])
        return f'Room {args["number"][0]} was successfully updated'

    def delete(self):
        args = rooms_parser.parse_args(strict=True)
        check_if_key_in_args('number', args, 'room')
        result = du.delete_item('Rooms', 'number', args['number'][0])
        check_if_row_was_affected(result, 'Room', args["number"][0])
        return f'Room {args["number"][0]} was successfully deleted'


class Tenants(Resource):
    @marshal_with(tenants_structure)
    def get(self):
        args = tenants_parser.parse_args(strict=True)
        if not any(args.values()):
            return [Tenant(*x[1:]) for x in du.get_all('Tenants')]
        for key, value in args.items():
            if value:
                return [Tenant(*x[1:]) for x in
                        du.get_with_filter('Tenants', key, value)]

    def post(self):
        args = tenants_parser.parse_args(strict=True)
        check_if_all_parameters_is_filled(args)
        check_if_value_is_positive('age', args)
        check_if_value_is_positive('room_number', args)
        try:
            du.add_new_item('Tenants', args)
        except sqlite3.IntegrityError:
            abort(409, error_code=409,
                  message=f'Tenant {args["passport_id"][0]} is already exists!'
                  )
        return f'New tenant {args["passport_id"][0]} was successfully added'

    def put(self):
        args = tenants_parser.parse_args(strict=True)
        check_if_key_in_args('passport_id', args, 'tenant')
        check_if_all_parameters_is_filled(args)
        check_if_value_is_positive('age', args)
        check_if_value_is_positive('room_number', args)
        keys = [key for key in args.keys() if args[key]]
        values = [value for value in args.values() if value]
        result = du.update_item('Tenants', keys, values,
                                'passport_id', args['passport_id'][0])
        check_if_row_was_affected(result, 'Tenant', args["passport_id"][0])
        return f'Tenant {args["passport_id"][0]} was successfully updated'

    def delete(self):
        args = tenants_parser.parse_args(strict=True)
        check_if_key_in_args('passport_id', args, 'tenant')
        result = du.delete_item('Tenants', 'passport_id',
                                args['passport_id'][0])
        check_if_row_was_affected(result, 'Tenant', args["passport_id"][0])
        return f'Tenant {args["passport_id"][0]} was successfully deleted'


class Staff(Resource):
    @marshal_with(staff_structure)
    def get(self):
        args = staff_parser.parse_args(strict=True)
        if not any(args.values()):
            return [Worker(*x[1:]) for x in du.get_all('Staff')]
        for key, value in args.items():
            if value:
                return [Worker(*x[1:]) for x in
                        du.get_with_filter('Staff', key, value)]

    def post(self):
        args = staff_parser.parse_args(strict=True)
        check_if_all_parameters_is_filled(args)
        check_if_value_is_positive('salary', args)
        try:
            du.add_new_item('Staff', args)
        except sqlite3.IntegrityError:
            abort(409, error_code=409,
                  message=f'Worker {args["passport_id"][0]} is already exists!'
                  )
        return f'New worker {args["passport_id"][0]} was successfully added'

    def put(self):
        args = staff_parser.parse_args(strict=True)
        check_if_key_in_args('passport_id', args, 'worker')
        check_if_all_parameters_is_filled(args)
        check_if_value_is_positive('salary', args)
        keys = [key for key in args.keys() if args[key]]
        values = [value for value in args.values() if value]
        result = du.update_item('Staff', keys, values,
                                'passport_id', args['passport_id'][0])
        check_if_row_was_affected(result, 'Worker', args["passport_id"][0])
        return f'Worker {args["passport_id"][0]} was successfully updated'

    def delete(self):
        args = staff_parser.parse_args(strict=True)
        check_if_key_in_args('passport_id', args, 'worker')
        result = du.delete_item('Staff', 'passport_id', args['passport_id'][0])
        check_if_row_was_affected(result, 'Worker', args["passport_id"][0])
        return f'Worker {args["passport_id"][0]} was successfully deleted'
