import requests

class RefillInteraction:
    def __init__(self, api_url):
        self.api_url = api_url
    
    def send_refill_payload(self, refill_amount, datetime):
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
