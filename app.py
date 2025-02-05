import requests
import json
from flask import Flask, render_template, request
import os

# Accessing API keys and other sensitive information from environment variables
weather_api_key = os.getenv('WEATHER_API_KEY')
secret_key = os.getenv('FLASK_SECRET_KEY')

app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key
api_key = os.getenv('WEATHER_API_KEY')

@app.route('/healthz') #render healtch check
def health_check():
    return 'OK', 200

@app.route("/", methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
    
    return render_template('index.html', weather_data=weather_data)

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_json = response.json()
    # Save response to a JSON file for me
        #with open(f'{city}_weather.json', 'w') as f:
            #json.dump(weather_json, f, indent=4)  # Pretty-print the JSON with indentation
        
        return weather_json
    return None

if __name__ == "__main__":
    app.run(debug=True)