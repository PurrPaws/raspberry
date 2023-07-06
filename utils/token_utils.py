class Token:
    @staticmethod
    def show_token():
        with open('config/pairing_config.txt', 'r') as file:
            for line in file:
                if line.startswith('token='):
                    token = line.strip().split('=')[1]
        return token
           