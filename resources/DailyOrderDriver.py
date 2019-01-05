from flask import request
from flask_restful import Resource
from Model import db, DailyOrderDriver, DailyOrderDriverSchema

daily_orders_schema = DailyOrderDriverSchema(many=True)
daily_order_schema = DailyOrderDriverSchema()

class DailyOrderDriverResource(Resource):
    def get(self):
        daily_order = DailyOrderDriver.query.all()
        daily_order = daily_orders_schema.dump(daily_order).data
        return {'status': 'success', 'data': daily_order}, 200    