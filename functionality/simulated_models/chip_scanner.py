import random
import time

class Chip_Scanner:
    # Initialize any required variables or configurations for the chip scanner
    def __init__(self):
        self.chip_ids = ["1234", "5678"]  # Example chip IDs for two cats
        self.detected_chip = None
        self.last_detection_time = None
        self.paired_chip = None

    # Simulate scanning a chip and returning the chip ID
    def get_chip_id(self):
        # Select a random chip ID from the list
        chip_id = random.choice(self.chip_ids)
        
        #Update the detected chip
        self.detected_chip = chip_id
        
        self.check_chip_id
        
        return chip_id

    def check_chip_id(self):
        with open('config/pairing_config.txt', 'r') as file:
            for line in file:
                if line.startswith('chip='):
                    self.paired_chip = line.strip().split('=')[1]
                    
        return self.detected_chip == self.paired_chip
    
    def presence_duration(self):
        is_present = random.choices([True, False], weights=[0.8, 0.2], k=1)[0]
        return is_present