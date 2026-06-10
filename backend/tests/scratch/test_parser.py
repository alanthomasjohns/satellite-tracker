from app.parsers.tle_parser import TLEParser
from app.providers.tle_provider import TLEProvider

provider = TLEProvider()
parser = TLEParser()

raw = provider.get_station_tles()

records = parser.parse_records(raw)

print(records[0])