# utils/datetime_utils.py
from datetime import datetime, timedelta

class DateTimeUtils:
    @staticmethod
    def convert_integer_to_datetime(minutes):
        base_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        target_datetime = base_date + timedelta(minutes=minutes)
        formatted_time = target_datetime.strftime("%H:%M")
        return formatted_time
    @staticmethod
    def get_current_datetime():
        current_datetime = datetime.now()
        string_formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return string_formatted_datetime
