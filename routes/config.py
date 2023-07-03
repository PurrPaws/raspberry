# routes/config.py
from flask import request

def register_token():    
    payload = request.json
    if payload is None or 'data' not in payload:
        return {'message': 'Invalid payload'},400
    
    token = payload['data'].get('token')
    
    if token is None:
        return {'message':'Token not found in payload'},400
    
    token_exists = False
    with open('config/pairing_config.txt', 'r+') as file:
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
    return 'OK'
