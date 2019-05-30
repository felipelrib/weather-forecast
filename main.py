import datetime
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    cityName = request.args.get('cityName')
    forecastData = []
    if cityName:
        url = "http://api.openweathermap.org/data/2.5/forecast?q={},BR&units=metric&appid=c30e0cca20b1b51229eabd3e454d12c3"
        response = requests.get(url.format(cityName)).json()
        # Check if the response was 200 OK
        if response["cod"] == "200":
            for weatherForecast in response["list"]:
                dateObj = datetime.datetime.fromtimestamp(weatherForecast["dt"]);
                dateStr = dateObj.strftime("%H:%M %B %d")

                icon = weatherForecast["weather"][0]["icon"]
                description = weatherForecast["weather"][0]["main"]
                temp = round(weatherForecast["main"]["temp"], 1)

                weather = {"date": dateStr, "icon": icon, "description": description, "temp": temp}
                forecastData.append(weather)
    return render_template('index.html', forecastData=forecastData, cityName=cityName)

