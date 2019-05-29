from DataFetch import FetchObd
from GPSFetch import GPS_Fetch
from CloudStorage import CloudStore
# from LocalStorage import Storage
import json
import datetime
import time
class FleetData:
	@staticmethod
	def fleet_data():
		#conn_obd = FetchObd.fetch_protocols()	
		now = datetime.datetime.now()
		conn_cloud = CloudStore.cloud_connect()
		# conn_local = Storage.connection()
		# Storage.create_table(conn_cloud)
		while True:
			# print(protocols)	
			dict = {}
			time.sleep(5)
			#dict = FetchObd.fetch_data(conn_obd)
			dict['timestamp'] = int(time.time())
			dict['id'] = 1
			dict['date'] = now.strftime("%Y-%m-%d")
			dict['time'] = now.strftime("%H:%M")
			dict['latitude'],dict['longitude'] = 0,0
			dict['latitude'],dict['longitude'] = GPS_Fetch.GPS_Info()
			dict1 = json.dumps(dict)
			dict2 = json.loads(dict1)
			print(dict1)
			print(dict2)
			# Storage.insert_data(conn_local,dict2)
			CloudStore.cloud_insert(conn_cloud,dict2)
			# Storage.close_connection(conn_local)

if __name__ == '__main__':
	FleetData.fleet_data()
