from flask_restful import Api
from flask import Blueprint
from hotel.resources import Rooms, Tenants, Staff

api_hotel_bp = Blueprint('Hotel', __name__)
api_hotel = Api(api_hotel_bp)

api_hotel.add_resource(Rooms, '/rooms')
api_hotel.add_resource(Tenants, '/tenants')
api_hotel.add_resource(Staff, '/staff')
