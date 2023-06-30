# registration.py
import requests
import logging

logging.basicConfig(level=logging.DEBUG)  # Add logging configuration

def check_token():
    # Read the token from the config file
    token = None
    with open('config/object_config.txt', 'r') as file:
        for line in file:
            if line.startswith('token='):
                token = line.strip().split('=')[1]
                break
    if token is not None:
        # Send a request to the Symfony API to check the token in the database
        payload = {
            "token":token
        }
        response = requests.post('http://localhost:3001/api/iot/registration', json=payload)
        if response.status_code == 200:
            # Token exists in the database
            data = response.json()
            if 'data' in data and 'token' in data['data']:
                # Token matches
                token_matches = data['data']['token'] == token
                return True
            else:
                # Token doesn't match
                logging.debug("Invalid token, please reinitialize the feeder.")
                return False
    else: 
        initiate_registration()

def initiate_registration():
    logging.debug("Starting registration process...")

    with open('config/object_config.txt', 'r') as file:
        for line in file:
            if line.startswith('SN='):
                SN = line.strip().split('=')[1]
            if line.startswith('PW='):
                PW = line.strip().split('=')[1]
    registration_payload = {"SN" : SN,
                            "PW" : PW}
    # Send payload to the registration endpoint
    response = requests.post('http://localhost:3001/api/iot/registration', json=registration_payload)
    if response.status_code == 200:
        # Registration successful
        logging.debug("Registration successful.")
        # Read the token from the response
        token = response.json().get('data', {}).get('token')
        # Check if the token line already exists in the config file
        with open('config/object_config.txt', 'r+') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.startswith('token='):
                    lines[i] = f"token={token}\n"
                    token_exists = True
                    break

            # If token line doesn't exist, append it to the file
            if not token_exists:
                lines.append(f"token={token}\n")

            # Move the file pointer to the beginning and truncate the file
            file.seek(0)
            file.truncate()

            # Write the updated lines to the config file
            file.writelines(lines)

            # Registration successful
        logging.debug("Registration successful.")
        return True

    # Registration failed
    logging.debug("Registration failed.")
    return False
check_token()

