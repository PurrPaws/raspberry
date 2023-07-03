# routes/pairing.py
from flask import request


def register_pet():    
    payload = request.json
    if payload is None or 'data' not in payload:
        return {'message': 'Invalid payload'},400
    
    chip = payload['data'].get('chip')
    
    if chip is None:
        return {'message':'Chip not found in payload'},400
    
    chip_exists = False
    with open('config/pairing_config.txt', 'r+') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line.startswith('chip='):
                lines[i] = f"chip={chip}\n"
                chip_exists = True
                break
        # If chip line doesn't exist, append it to the file
        if not chip_exists:
            lines.append(f"chip={chip}\n")
        # Move the file pointer to the beginning and truncate the file
        file.seek(0)
        file.truncate()
        # Write the updated lines to the config file
        file.writelines(lines)
    return 'OK'
