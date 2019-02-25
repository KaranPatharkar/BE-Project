from DataFetch import FetchObd
from GPSFetch import FetchGps
from CloudStorage import CloudStore
from LocalStorage import storage
import json

class FleetData:
	@staticmethod
	def fleet_data():
		CloudStore.cloud_connect()
		dict = {}
		dict['latitude'],dict['longitude'] = 10,10
		dict = FetchObd.fetch_data()
		dict['latitude'],dict['longitude'] = FetchGps.gps_info()
		dict1 = json.dumps(dict)
		dict2 = json.loads(dict1)
		CloudStore.cloud_insert(dict2)

if __name__ == '__main__':
	FleetData.fleet_data()
