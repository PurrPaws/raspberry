import random

class Feeding:
    
    def feeding_portion(self):
        # Simulate weight measurement
        random_portion = random.randint(1, 10)
        data = 0
        i = 0
        while i < 30:
            data += random_portion * 3
            i += 1
        self.weight = round(-(data / i + random.uniform(-1, 1)),1)
        
    def get_weight_difference(self):
        return self.weight