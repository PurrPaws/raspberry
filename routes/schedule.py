# routes/schedule.py
from flask import request
from utils.datetime_utils import convert_integer_to_datetime

def receive_data():
    received_json_data = request.get_json()
    data = received_json_data['data']
    
    schedule = data['schedule']
    state = data['state']
    
    with open('config/feeding_schedule_config.txt', 'w') as file:
        file.write(f"{state}\n")
        for item in schedule:
            amount = item['amount']
            minutes = item['time']
            date_time = convert_integer_to_datetime(minutes)
            file.write(f"{date_time}-{amount}\n")
    
    return 'OK'
