import random

class Scales:
    
    def weight_portion(self):
        # Simulate weight measurement
        random_portion = random.randint(1, 10)
        data = 0
        i = 0
        while i < 30:
            data += random_portion * 5
            i += 1
        self.weight = round(data / i + random.uniform(-1, 1), 1)
        return self.weight