# Weather Service

This service exposes a single endpoint:

**GET** `/weather/<city>`

Response format (**all fields required**):

```json
{
  "city": "string",
  "temperature": 72.4,
  "unit": "F",
  "source": "noaa"
}
```

The `temperature` unit returned **MUST always match** the unit defined
in `config.py` (`CONFIG["DEFAULT_TEMP_UNIT"]`).

If you modify the endpoint, ensure the response matches the spec above.
