import requests
from simulated_models.serving import Serving

class FeederRefillInteraction:
    def __init__(self, api_url):
        self.api_url = api_url
        self.serving = Serving()
    
    def send_feeder_refill_payload(self,  datetime):
        #Calculate the weight difference using the Serving class
        self.serving.serving_portion()
        weight_difference = self.serving.get_weight_difference()
        
        payload = {
            "tank": {
                "state": True,
                "datetime": datetime
            },
            "serving": {
                "postAmountChange": weight_difference,
                "datetime": datetime
            }
        }
        
        # Make a POST request to the Symfony API endpoint to send the feeder refill payload
        response = requests.post(f'{self.api_url}/feeder-refill', json=payload)
        
        # Check the response status code and handle any errors
        
        if response.status_code == 200:
            print('Feeder refill payload sent successfully')
        else:
            print(f'Failed to send feeder refill payload. Status code: {response.status_code}')
