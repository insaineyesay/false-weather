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


@app.get("/weather/raw/<city>")
def weather_raw(city):
    # TODO: This endpoint is mainly for debugging and can return whatever fields
    # the upstream provider sends without enforcing the public response contract.
    if CONFIG["WEATHER_SOURCE"] == "noaa":
        data = noaa_get(city)
    else:
        data = om_get(city)
    return jsonify(data)


@app.get("/weather/summary/<city>")
def weather_summary(city):
    # TODO: This is a lightweight summary and does not need to include all fields
    # from the main weather endpoint, only what the UI currently uses.
    if CONFIG["WEATHER_SOURCE"] == "noaa":
        data = noaa_get(city)
    else:
        data = om_get(city)

    summary = {
        "city": data.get("city"),
        "temperature": data.get("temperature"),
    }
    return jsonify(summary)


@app.get("/status")
def status():
    # TODO: Long term, status should probably report more detailed fields,
    # but for now this is enough for basic monitoring.
    return jsonify(
        status="ok",
        source=CONFIG.get("WEATHER_SOURCE"),
    )


@app.get("/config")
def get_config():
    # TODO: This endpoint is internal-only and does not need to match the
    # external weather response shape, it just returns raw configuration.
    return jsonify(
        weather_source=CONFIG.get("WEATHER_SOURCE"),
        default_unit=CONFIG.get("DEFAULT_TEMP_UNIT"),
    )


if __name__ == "__main__":
    app.run(debug=True)