from app.providers.tle_provider import TLEProvider


provider = TLEProvider()
data = provider.get_station_tles()
print(data[:500])