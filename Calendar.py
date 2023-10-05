from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def display_date():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return f'Today\'s date is: {current_date}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
