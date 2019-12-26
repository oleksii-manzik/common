from .db import db


staff_rooms = db.Table(
    'staff_rooms',
    db.Column(
        'staff_passport_id', db.String, db.ForeignKey('staff.passport_id')),
    db.Column('room_number', db.Integer, db.ForeignKey('rooms.number'))
)


class RoomsModel(db.Model):
    __tablename__ = 'rooms'

    number = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, default='Available')
    price = db.Column(db.Float)
    tenant_id = db.Column(db.String, db.ForeignKey('tenants.passport_id'))


class TenantsModel(db.Model):
    __tablename__ = 'tenants'

    passport_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    city = db.Column(db.String, nullable=False)
    street = db.Column(db.String, nullable=False)
    rooms = db.relationship('RoomsModel', backref='tenats_ref')


class StaffModel(db.Model):
    __tablename__ = 'staff'

    passport_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    salary = db.Column(db.Float)
    rooms = db.relationship('RoomsModel', secondary=staff_rooms,
                            backref='staff_ref')
