from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class SmartphoneModel(db.Model):
    __tablename__ = "table"

    id: int
    smartphone_id: str
    brand_name: str
    model_name: str
    price: int
    avg_rating: float
    support_5g: bool
    processor_brand: str
    processor_speed: float
    num_cores: int
    battery_capacity: int
    fast_charging: bool
    fast_charge_capacity: int
    ram_capacity: int
    internal_memory: int
    screen_size: float
    refresh_rate: int
    num_rear_cameras: int
    os: str
    primary_camera_rear: int
    primary_camera_front: int
    extended_memory_available: bool
    resolution_height: int
    resolution_width: int

    id = db.Column(db.Integer, primary_key=True)
    smartphone_id = db.Column(db.String(), unique=True)
    brand_name = db.Column(db.String(99))
    model_name = db.Column(db.String(999))
    price = db.Column(db.Integer())
    avg_rating = db.Column(db.Float())
    support_5g = db.Column(db.Boolean())
    processor_brand = db.Column(db.String(99))
    num_cores = db.Column(db.Integer())
    processor_speed = db.Column(db.Float())
    battery_capacity = db.Column(db.Integer())
    fast_charging = db.Column(db.Boolean())
    fast_charge_capacity = db.Column(db.Integer())
    ram_capacity = db.Column(db.Integer())
    internal_memory = db.Column(db.Integer())
    screen_size = db.Column(db.Float())
    refresh_rate = db.Column(db.Integer())
    num_rear_cameras = db.Column(db.Integer())
    os = db.Column(db.String(99))
    primary_camera_rear = db.Column(db.Integer())
    primary_camera_front = db.Column(db.Integer())
    extended_memory_available = db.Column(db.Boolean())
    resolution_height = db.Column(db.Integer())
    resolution_width = db.Column(db.Integer())

    def create(self):
       db.session.add(self)
       db.session.commit()
       return self

    def __init__(self, smartphone_id, brand_name, model_name, price, avg_rating, support_5g, processor_brand,
                 num_cores, processor_speed, battery_capacity, fast_charging, fast_charge_capacity, ram_capacity,
                 internal_memory, screen_size, refresh_rate, num_rear_cameras, os, primary_camera_rear, primary_camera_front,
                 extended_memory_available, resolution_height, resolution_width):
        self.smartphone_id = smartphone_id
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.avg_rating = avg_rating
        self.support_5g = support_5g
        self.processor_brand = processor_brand
        self.num_cores = num_cores
        self.processor_speed = processor_speed
        self.battery_capacity = battery_capacity
        self.fast_charging = fast_charging
        self.fast_charge_capacity = fast_charge_capacity
        self.ram_capacity = ram_capacity
        self.internal_memory = internal_memory
        self.screen_size = screen_size
        self.refresh_rate = refresh_rate
        self.num_rear_cameras = num_rear_cameras
        self.os = os
        self.primary_camera_rear = primary_camera_rear
        self.primary_camera_front = primary_camera_front
        self.extended_memory_available = extended_memory_available
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width
    
    def __repr__(self):
        return f"{self.smartphone_id}:{self.brand_name}"
