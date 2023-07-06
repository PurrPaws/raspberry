from utils.datetime_utils import DateTimeUtils

class Door:
    def __init__(self):
        self.door_state = False  # Initialize door state as closed

    def door_opening(self):
        # Simulate door opening
        self.door_state = True
        self.datetime = DateTimeUtils.get_current_datetime()
        return self.door_state, self.datetime()

    def door_closing(self):
        # Simulate door closing
        self.door_state = False
        self.datetime = DateTimeUtils.get_current_datetime()
        return self.door_state, self.datetime()

    def get_door_state(self):
        return self.door_state