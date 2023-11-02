import json
from flask import Response

def eval_int(req):
    return None if req == '' else int(req)

def eval_float(req):
    return None if req == '' else float(req)

def eval_bool(req):
    if req == '1': return True
    elif req == '0': return False
    else: return None
    
def update_data(curr_data, new_data):
    if new_data.get('smartphone_id'): curr_data.smartphone_id = new_data['smartphone_id']
    if new_data.get('brand_name'): curr_data.brand_name = new_data['brand_name']
    if new_data.get('model_name'): curr_data.model_name = new_data['model_name']
    if new_data.get('price'): curr_data.price = new_data['price']
    if new_data.get('avg_rating'): curr_data.avg_rating = new_data['avg_rating']
    if new_data.get('support_5g'): curr_data.support_5g = new_data['support_5g']
    if new_data.get('processor_brand'): curr_data.processor_brand = new_data['processor_brand']
    if new_data.get('processor_speed'): curr_data.processor_speed = new_data['processor_speed']
    if new_data.get('num_cores'): curr_data.num_cores = new_data['num_cores']
    if new_data.get('battery_capacity'): curr_data.battery_capacity = new_data['battery_capacity']
    if new_data.get('fast_charging'): curr_data.fast_charging = new_data['fast_charging']
    if new_data.get('fast_charge_capacity'): curr_data.fast_charge_capacity = new_data['fast_charge_capacity']
    if new_data.get('ram_capacity'): curr_data.ram_capacity = new_data['ram_capacity']
    if new_data.get('internal_memory'): curr_data.internal_memory = new_data['internal_memory']
    if new_data.get('screen_size'): curr_data.screen_size = new_data['screen_size']
    if new_data.get('refresh_rate'): curr_data.refresh_rate = new_data['refresh_rate']
    if new_data.get('num_rear_cameras'): curr_data.num_rear_cameras = new_data['num_rear_cameras']
    if new_data.get('os'): curr_data.os = new_data['os']
    if new_data.get('primary_camera_rear'): curr_data.primary_camera_rear = new_data['primary_camera_rear']
    if new_data.get('primary_camera_front'): curr_data.primary_camera_front = new_data['primary_camera_front']
    if new_data.get('extended_memory_available'): curr_data.extended_memory_available = new_data['extended_memory_available']
    if new_data.get('resolution_height'): curr_data.resolution_height = new_data['resolution_height']
    if new_data.get('resolution_width'): curr_data.resolution_width = new_data['resolution_width']
    
    return curr_data