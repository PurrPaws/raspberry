import requests

class CatFeedingInteraction:
    def __init__(self, api_url):
        self.api_url = api_url
    
    def send_feeding_payload(self, datetime, eaten):
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
