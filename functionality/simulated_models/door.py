class Door:
    def __init__(self):
        self.door_state = False  # Initialize door state as closed

    def door_opening(self):
        # Simulate door opening
        self.door_state = True

    def door_closing(self):
        # Simulate door closing
        self.door_state = False

    def get_door_state(self):
        return self.door_state