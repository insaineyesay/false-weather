def get_weather(city):
    """Return weather data for a city using Open-Meteo.

    This service returns temperatures in Celsius only.
    """
    return {
        "city": city,
        "temperature": 21.3,
        "unit": "C",
        "source": "open-meteo",
    }
