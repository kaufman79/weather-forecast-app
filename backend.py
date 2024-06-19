import os
import requests

api_key = os.getenv("OPEN_WEATHER_API")

def get_data(place, forecast_days):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?q={place}"
           f"&appid={api_key}")
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days  # there are 8 data points per day, so we multiply 8 by how many days the user selects
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=3))