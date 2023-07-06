import requests
from functionality.simulated_models.scales import Scales
from utils.datetime_utils import DateTimeUtils
from utils.token_utils import Token

class Serving_Interaction:
    def __init__(self, api_url):
        self.api_url = api_url + "serving"
        self.scales = Scales()
    
    def serving_portion(self):
        #Calculate the weight difference using the Serving class
        weight_difference = self.scales.weight_portion()
        
        current_datetime = DateTimeUtils.get_current_datetime()
        token = Token.show_token()
        payload = {
            "tank": {
                "state": True,
            },
            "scales": {
                "postAmountChange": weight_difference,
                "datetime": current_datetime
            }
        }
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }
        
        # Make a POST request to the Symfony API endpoint to send the feeder serving payload
        response = requests.post(f'{self.api_url}/serving', json=payload, headers=headers)
        
        # Check the response status code and handle any errors
        
        if response.status_code == 200:
            print('Feeder serving payload sent successfully')
        else:
            print(f'Failed to send feeder serving payload. Status code: {response.status_code}')
