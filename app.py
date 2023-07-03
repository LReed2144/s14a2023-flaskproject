from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! Welcome to S14A2023'

@app.route('/datetime')
def show_datetime():
    # Get current datetime in the server's timezone
    server_time = datetime.now()

    # Get current datetime in UTC timezone
    utc_time = datetime.now(pytz.utc)

    # Get current datetime in your own timezone
    your_timezone = pytz.timezone('Pacific Standard Time')  # Replace 'Your/Timezone' with your actual timezone
    your_time = datetime.now(your_timezone)

    # Format the datetime objects as strings
    server_time_str = server_time.strftime('%Y-%m-%d %H:%M:%S')
    utc_time_str = utc_time.strftime('%Y-%m-%d %H:%M:%S')
    your_time_str = your_time.strftime('%Y-%m-%d %H:%M:%S')

    # Create the response string
    response = f"Server Time: {server_time_str}<br>"
    response += f"UTC Time: {utc_time_str}<br>"
    response += f"Your Time: {your_time_str}"

    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run()