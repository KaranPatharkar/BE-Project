import sqlite3

class Storage:

	global database_name
	database_name = 'fleet.db'

	@staticmethod
	def connection():
		conn = sqlite3.connect(database_name)
		print("Database '{0}' successfully opened.".format(database_name))
		return conn

	@staticmethod
	def create_table(conn): 
		print "Opened database successfully";
		conn.execute('''CREATE TABLE IF NOT EXISTS CARDATA(CUR_DATE DATETIME,LATITUDE REAL,LONGITUDE REAL,SPEED REAL,RPM INT,COOLANT_TEMP REAL);''')
		print "Table created successfully";


	@staticmethod
	def insert_data(conn,list):
		print(list['latitude'])
		date = list['date'] + " " + list['time']
		print "Opened database successfully";
		conn.execute("INSERT INTO CARDATA(CUR_DATE,LATITUDE,LONGITUDE,SPEED,RPM,COOLANT_TEMP) VALUES (?,?,?,?,?,?)",(date,list['latitude'],list['longitude'],list['SPEED'],list['RPM'],list['COOLANT_TEMP'] ));
		conn.commit()
		print "Records created successfully";


	@staticmethod	
	def display_data(conn):
		print "Opened database successfully";
		cursor = conn.execute("SELECT * from CARDATA")
		for row in cursor:
		   print "CUR_DATE = ", row[0]
		   print "LATITUDE = ", row[1]
		   print "LONGITUDE = ", row[2]
		   print "SPEED = ", row[3]
		   print "RPM = ", row[4]
		   print "COOLANT_TEMP = ", row[5], "\n"
		print "Operation done successfully";
		

	@staticmethod
	def close_connection(conn):
		print "Connection closed";	
		conn.close()	