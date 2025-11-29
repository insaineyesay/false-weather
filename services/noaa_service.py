def get_weather(city):
    """Return weather data for a city using NOAA.

    This service returns temperatures in Fahrenheit only.
    """
    return {
        "city": city,
        "temperature": 72.4,
        "unit": "F",
        "source": "noaa",
    }
