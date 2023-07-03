# registration.py
import requests
import logging
import time

logging.basicConfig(level=logging.DEBUG)  # Add logging configuration

def check_token():
    # Read the token from the config file
    token = None
    with open('config/pairing_config.txt', 'r') as file:
        for line in file:
            if line.startswith('token='):
                token = line.strip().split('=')[1]
                break
    if token is not None:
        # Send a request to the Symfony API to check the token in the database
        payload = {
            "token":token
        }
        response = requests.post('http://localhost:3001/api/iot/check_token', json=payload)
        if response.status_code == 200:
            # Token exists in the database
            print("Token validated")
            return True
        else:
            # Token doesn't match
            logging.debug("Invalid token, please reinitialize the feeder.")
            return False
    else:
        initiate_registration()

def initiate_registration():
    logging.debug("Starting registration process...")

    # Read Serial Number (SN) and Password (PW) from the config file
    with open('config/object_config.txt', 'r') as file:
        for line in file:
            if line.startswith('SN='):
                SN = line.strip().split('=')[1]
            if line.startswith('PW='):
                PW = line.strip().split('=')[1]
    registration_payload = {"SN": SN, "PW": PW}
    
    # Define registration parameters
    start_time = time.time()
    max_duration = 15  # Maximum duration for registration in seconds
    interval = 3  # Time interval for retrying the registration

    # Try to register the device within the maximum duration
    while time.time() - start_time < max_duration:
        # Send payload to the registration endpoint
        response = requests.post('http://localhost:3001/api/iot/check_token', json=registration_payload)
        if response.status_code == 200:
            # Registration successful
            logging.debug("Registration successful.")
            return True

        # Registration failed, retry after the defined interval
        logging.debug("Registration failed. Retrying...")
        time.sleep(interval)
    
    # Registration failed within the maximum duration
    logging.debug("Registration failed.")
    return False

# Call the check_token function to start the registration process
check_token()
