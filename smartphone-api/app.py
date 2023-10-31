from marshmallow import fields
import json
from flask import Flask, jsonify, request, make_response
from flask_marshmallow import Marshmallow
from flask_restful import *
from models import *
from helper import *

app = Flask(__name__)
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartphones.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

class SmartphoneSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
       model = SmartphoneModel
       sqla_session = db.session
       load_instance = True

   id = fields.Number(dump_only=True)
   smartphone_id = fields.String(required=True)
   brand_name = fields.String(required=True)
   model_name = fields.String(required=True)
   price = fields.Number(required=True)
   avg_rating = fields.Float(required=True)
   support_5g = fields.Boolean(required=True)
   processor_brand = fields.String(required=True)
   num_cores = fields.Number(required=True)
   processor_speed = fields.Float(required=True)
   battery_capacity = fields.Number(required=True)
   fast_charging = fields.Boolean(required=True)
   fast_charge_capacity = fields.Number(required=True)
   ram_capacity = fields.Number(required=True)
   internal_memory = fields.Number(required=True)
   screen_size = fields.Float(required=True)
   refresh_rate = fields.Number(required=True)
   num_rear_cameras = fields.Number(required=True)
   os = fields.String(required=True)
   primary_camera_rear = fields.Number(required=True)
   primary_camera_front = fields.Number(required=True)
   extended_memory_available = fields.Boolean(required=True)
   resolution_height = fields.Number(required=True)
   resolution_width = fields.Number(required=True)



@app.before_request
def create_table():
    db.create_all()


@app.route('/smartphone', methods=['GET','POST'])
def fetch():
    if request.method == 'GET':
        smartphones = SmartphoneModel.query.all()
        smartphone_schema = SmartphoneSchema(many=True)
        return make_response(jsonify({"smartphones": smartphones}))
    elif request.method == 'POST':
        data = request.get_json()
        smartphone_schema = SmartphoneSchema()
        smartphone = smartphone_schema.load(data)
        res = smartphone_schema.dump(smartphone.create())
        return make_response(jsonify({"smartphone": res}), 200)

@app.route('/smartphone/<string:smartphone_id>', methods=['GET', 'PUT', 'DELETE'])
def fetch_by_id(smartphone_id):
    get_smartphone = SmartphoneModel.query.filter_by(smartphone_id=smartphone_id).first()
    if request.method == 'GET':
        smartphone_schema = SmartphoneSchema()
        smartphone = smartphone_schema.dump(get_smartphone)
        return make_response(jsonify({"smartphone": smartphone}))
    elif request.method == 'PUT':
        data = request.get_json()
        if data.get('smartphone_id'):
            get_smartphone.smartphone_id = data['smartphone_id']
        if data.get('brand_name'):
            get_smartphone.brand_name = data['brand_name']
        db.session.add(get_smartphone)
        db.session.commit()
        smartphone_schema = SmartphoneSchema(only=['smartphone_id', 'brand_name'])
        smartphone = smartphone_schema.dump(get_smartphone)
        return make_response(jsonify({"smartphone": smartphone}))
    elif request.method == 'DELETE':
        db.session.delete(get_smartphone)
        db.session.commit()
        return make_response("", 204)

app.run(host='localhost', port=6666, debug=True)