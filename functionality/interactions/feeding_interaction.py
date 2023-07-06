import requests, time
from functionality.simulated_models.chip_scanner import Chip_Scanner
from functionality.simulated_models.scales import Scales
from functionality.simulated_models.door import Door
from utils.datetime_utils import DateTimeUtils
from utils.token_utils import Token

class Feeding_Interaction:
    def __init__(self, api_url):
        self.api_url = api_url + "feed"
        self.scales = Scales()
        self.chip_scanner = Chip_Scanner()
        self.door = Door()
        self.is_chip_validated = True
    
    def start_feeding(self):
        #Open the door
        door_opened_state, door_opened_time = self.door.door_opening()
        
        while self.is_chip_validated:
            self.check_chip_validation()
            
            time.sleep(2)
        self.complete_feeding()
        
        door_closed_state, door_opened_time = self.door.door_closing()
        payload = {
            "tank": {
                "state": True,
                "datetime": datetime
            },
            "serving": {
                "postAmountChange": eaten,
                "datetime": datetime
            },
            "door": [
                {
                    "state": True,
                    "datetime": datetime
                },
                {
                    "state": False,
                    "datetime": datetime
                }
            ]
        }
        
        # Make a POST request to the Symfony API endpoint to send the feeding payload
        response = requests.post(f'{self.api_url}/feeding', json=payload)
        
        # Check the response status code and handle any errors
        
        if response.status_code == 200:
            print('Feeding payload sent successfully')
        else:
            print(f'Failed to send feeding payload. Status code: {response.status_code}')

    def check_chip_validation(self):
        return self.chip_scanner.presence_duration()