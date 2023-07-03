class Tank:
    def __init__(self, initial_state=True):
        self.tank_state = initial_state  # Initialize tank state as closed
    
    def tank_filled(self):
        # Simulate door opening
        self.tank_state = True
    
    def tank_emptying(self):
        # Simulate door opening
        self.tank_state = False
    
    def get_tank_state(self):
        return self.tank_state
