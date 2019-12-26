from flask_restful import Resource, marshal_with, abort
from sqlalchemy.exc import IntegrityError
from .parsers import *
from .fields_formatting import *
from .fields_check_util import *
from .model import *
from .db import db


class Rooms(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        args = rooms_parser.parse_args(strict=True)
        if not any(args.values()):
            return RoomsModel.query.all()
        n_args = {k: v for k, v in args.items() if v}
        return RoomsModel.query.filter_by(**n_args).all()

    def post(self):
        args = rooms_parser.parse_args(strict=True)
        check = check_if_all_parameters_is_filled(args)
        if check:
            abort(**check)
        try:
            db.session.add(RoomsModel(**args))
            db.session.commit()
        except IntegrityError:
            abort(409, error_code=409,
                  message=f'Room {args["number"]} is already exists!')
        return f'New room {args} was successfully added'

    def put(self):
        args = rooms_parser.parse_args(strict=True)
        check1 = check_if_key_in_args('number', args, 'room')
        if check1:
            abort(**check1)
        check2 = check_if_all_parameters_is_filled(args)
        if check2:
            abort(**check2)
        room = RoomsModel.query.filter_by(number=args['number'])
        check3 = check_if_row_was_affected(
            room.first(), 'Room', args["number"])
        if check3:
            abort(**check3)
        room.update(args)
        db.session.commit()
        return f'Room {args} was successfully updated'

    def delete(self):
        args = rooms_parser.parse_args(strict=True)
        check1 = check_if_key_in_args('number', args, 'room')
        if check1:
            abort(**check1)
        room = RoomsModel.query.filter_by(number=args['number'])
        check2 = check_if_row_was_affected(
            room.first(), 'Room', args["number"])
        if check2:
            abort(**check2)
        room.delete()
        db.session.commit()
        return f'Room {args} was successfully deleted'


class Tenants(Resource):
    @marshal_with(tenants_structure)
    def get(self):
        args = tenants_parser.parse_args(strict=True)
        if not any(args.values()):
            return TenantsModel.query.all()
        n_args = {k: v for k, v in args.items() if v}
        return TenantsModel.query.filter_by(**n_args).all()

    def post(self):
        args = tenants_parser.parse_args(strict=True)
        check = check_if_all_parameters_is_filled(args)
        if check:
            abort(**check)
        try:
            db.session.add(TenantsModel(**args))
            db.session.commit()
        except IntegrityError:
            abort(409, error_code=409,
                  message=f'Tenant {args["passport_id"]} is already exists!')
        return f'New tenant {args} was successfully added'

    def put(self):
        args = tenants_parser.parse_args(strict=True)
        check1 = check_if_key_in_args('passport_id', args, 'tenant')
        if check1:
            abort(**check1)
        check2 = check_if_all_parameters_is_filled(args)
        if check2:
            abort(**check2)
        tenant = TenantsModel.query.filter_by(passport_id=args['passport_id'])
        check3 = check_if_row_was_affected(
            tenant.first(), 'Tenant', args["passport_id"])
        if check3:
            abort(**check3)
        tenant.update(args)
        db.session.commit()
        return f'Tenant {args} was successfully updated'

    def delete(self):
        args = tenants_parser.parse_args(strict=True)
        check1 = check_if_key_in_args('passport_id', args, 'tenant')
        if check1:
            abort(**check1)
        tenant = TenantsModel.query.filter_by(passport_id=args['passport_id'])
        check2 = check_if_row_was_affected(
            tenant.first(), 'Tenant', args["passport_id"])
        if check2:
            abort(**check2)
        tenant.delete()
        db.session.commit()
        return f'Tenant {args} was successfully deleted'


class Staff(Resource):
    @marshal_with(staff_structure)
    def get(self):
        args = staff_parser.parse_args(strict=True)
        if not any(args.values()):
            return StaffModel.query.all()
        n_args = {k: v for k, v in args.items() if v}
        return StaffModel.query.filter_by(**n_args).all()

    def post(self):
        args = staff_parser.parse_args(strict=True)
        check = check_if_all_parameters_is_filled(args)
        if check:
            abort(**check)
        try:
            db.session.add(StaffModel(**args))
            db.session.commit()
        except IntegrityError:
            abort(409, error_code=409,
                  message=f'Worker {args["passport_id"]} is already exists!')
        return f'New worker {args} was successfully added'

    def put(self):
        args = staff_parser.parse_args(strict=True)
        check1 = check_if_key_in_args('passport_id', args, 'worker')
        if check1:
            abort(**check1)
        check2 = check_if_all_parameters_is_filled(args)
        if check2:
            abort(**check2)
        worker = StaffModel.query.filter_by(passport_id=args['passport_id'])
        check3 = check_if_row_was_affected(
            worker.first(), 'Worker', args["passport_id"])
        if check3:
            abort(**check3)
        worker.update(args)
        db.session.commit()
        return f'Worker {args} was successfully updated'

    def delete(self):
        args = staff_parser.parse_args(strict=True)
        check1 = check_if_key_in_args('passport_id', args, 'worker')
        if check1:
            abort(**check1)
        worker = StaffModel.query.filter_by(passport_id=args['passport_id'])
        check2 = check_if_row_was_affected(
            worker.first(), 'Tenant', args["passport_id"])
        if check2:
            abort(**check2)
        worker.delete()
        db.session.commit()
        return f'Worker {args} was successfully deleted'


class RoomsStaff(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        args = rooms_staff_parser.parse_args(strict=True)
        check = check_if_key_in_args('staff_passport_id', args, 'worker')
        if check:
            abort(**check)
        return StaffModel.query.filter_by(
            passport_id=args['staff_passport_id']).first().rooms

    def post(self):
        args = rooms_staff_parser.parse_args(strict=True)
        check = check_if_all_parameters_is_filled(args)
        if check:
            abort(**check)
        try:
            room = RoomsModel.query.filter_by(
                number=args['room_number']).first()
            worker = StaffModel.query.filter_by(
                passport_id=args['staff_passport_id']).first()
            worker.rooms.append(room)
            db.session.commit()
        except IntegrityError:
            abort(409, error_code=409,
                  message=f'Worker {args["staff_passport_id"]} is '
                          f'already pinned!')
        return f'New worker {args} was successfully ' \
               f'pinned to {args} room'
