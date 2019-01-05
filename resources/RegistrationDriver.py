from flask import request
from flask_restful import Resource
from Model import db, RegistrationDriver, RegistrationDriverSchema

driver_registrations_schema = RegistrationDriverSchema(many=True)
driver_registration_schema = RegistrationDriverSchema()

class RegistrationDriverResource(Resource):
    def get(self):
        driver_registration = RegistrationDriver.query.all()
        driver_registration = driver_registrations_schema.dump(driver_registration).data
        return {'status': 'success', 'data': driver_registration}, 200    