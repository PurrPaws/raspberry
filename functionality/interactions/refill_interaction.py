import requests
from functionality.simulated_models.scales import Scales
from utils.datetime_utils import DateTimeUtils
from utils.token_utils import Token

class Refill_Interaction:
    def __init__(self, api_url):
        self.api_url = api_url + "refill"
        self.scales = Scales()
    
    def refill_tank(self):
        self.refill.get_refill_amount()
        payload = {
            "refill": {
                "refillAmountSave": refill_amount,
                "datetime": datetime
            },
            "tank": {
                "state": True,
                "datetime": datetime
            }
        }
        
        # Make a POST request to the Symfony API endpoint to send the refill payload
        response = requests.post(f'{self.api_url}/refill', json=payload)
        
        # Check the response status code and handle any errors
        
        if response.status_code == 200:
            print('Refill payload sent successfully')
        else:
            print(f'Failed to send refill payload. Status code: {response.status_code}')
