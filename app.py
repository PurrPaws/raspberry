# app.py
from flask import Flask
from routes import schedule, pairing, config

app = Flask(__name__)

app.route('/schedule', methods=['GET'])(schedule.receive_data)
app.route('/pairing', methods=['POST'])(pairing.send_data)
app.route('/config', methods=['POST'])(config.register_token)

if __name__ == '__main__':
    host = 'localhost'
    port = 8080    
    app.run(host=host, port=port)
        
        
