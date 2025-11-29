from flask import Flask, jsonify
from config import CONFIG
from services.noaa_service import get_weather as noaa_get
from services.open_meteo_service import get_weather as om_get

app = Flask(__name__)


@app.get("/weather/<city>")
def weather(city):
    if CONFIG["WEATHER_SOURCE"] == "noaa":
        data = noaa_get(city)
    else:
        data = om_get(city)

    # NOTE: The README says temp unit MUST match default config unit.
    # TODO: Convert temp to the configured DEFAULT_TEMP_UNIT before returning.
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
