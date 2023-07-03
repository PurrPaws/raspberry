class Token:
    def __init__(self):
        pass
    
    def check_token(self):
        # Read the token from the config file
        token = None
        with open('config/pairing_config.txt', 'r') as file:
            for line in file:
                if line.startswith('token='):
                    token = line.strip().split('=')[1]
                    break
        if token is not None:
            return token
        else:
            raise ValueError("Token error: Token not found in the pairing file")