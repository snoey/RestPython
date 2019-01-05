from flask import Flask
from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class RegistrationDriver(db.Model):	
	__tablename__ = 'driver_registration'
		
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
	date_last_modified = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
	active_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
	name = db.Column(db.String(250))
	phone = db.Column(db.BigInteger) 
	resign_date = db.Column(db.String(50))
	resign_reason = db.Column(db.String(250))
	status = db.Column(db.Integer) 
	tipe = db.Column(db.Integer)     
	area = db.Column(db.Integer) 
	operator_id = db.Column(db.String(50))
	modified_by = db.Column(db.String(50))
	vehicle_type = db.Column(db.String(50))
	helmet_qty = db.Column(db.String(50)) 
	jacket_qty = db.Column(db.String(50)) 
	vehicle_brand = db.Column(db.String(100))
	vehicle_year = db.Column(db.String(50))
	bike_type = db.Column(db.String(50))
	first_ride_bonus_awarded = db.Column(db.String(50))
	is_doc_completed = db.Column(db.String(50))

	def __init__(self, driver_registration):
		self.driver_registration = driver_registration		

		
class RegistrationDriverSchema(ma.Schema):
	id = fields.Integer()
	date_created = fields.DateTime()
	date_last_modified = fields.DateTime()
	active_date = fields.DateTime()
	name = fields.String()
	phone = fields.Integer()
	resign_date = fields.String()
	resign_reason = fields.String()
	status = fields.Integer()
	tipe = fields.Integer()
	area = fields.Integer()
	operator_id = fields.String()
	modified_by = fields.String()
	vehicle_type = fields.String()
	helmet_qty = fields.String()
	jacket_qty = fields.String()
	vehicle_brand = fields.String()
	vehicle_year = fields.String()
	bike_type = fields.String()
	first_ride_bonus_awarded = fields.String()
	is_doc_completed = fields.String()
	

class DailyOrderDriver(db.Model):	
	__tablename__ = 'daily_order'
	id = db.Column(db.Integer, primary_key=True)
	order_payment = db.Column(db.String(250))
	order_type = db.Column(db.String(50))
	order_status = db.Column(db.String(50))	
	customer_no = db.Column(db.Integer) 
	order_time = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
	

	def __init__(self, daily_order):
		self.daily_order = daily_order		

		
class DailyOrderDriverSchema(ma.Schema):
	order_payment = fields.String()
	order_type = fields.String()
	order_status = fields.String()
	customer_no = fields.Integer()
	order_time = fields.DateTime()	
	
	


	  			  


 	