import sqlite3

class storage:
	def create_table(params): #check on main.py if table present
		conn = sqlite3.connect('obd.db')
		print("Opened Database successfully.")
		conn.execute('''CREATE TABLE data
         (id INT PRIMARY KEY AUTO INCREMENT,
         currentdate DATE,
         currenttime TIME,
         speed INT,
         fuellevel INT,
         coolanttemp INT);''')
		print ("Table created successfully.")
		conn.close()

	def insert_data(params):
		conn = sqlite3.connect('obd.db')
		print("Opened Database successfully.")
		conn.execute("INSERT INTO COMPANY (currentdate,currenttime,speed,fuellevel,coolanttemp) VALUES ();")
		conn.commit()
		print ("Records created successfully.")
		conn.close()

	def display_data():
		conn = sqlite3.connect('obd.db')
		print("Opened Database successfully.")
		try:
			cursor = conn.execute("SELECT * from cardata;")
			# for row in cursor:
			#    print "ID = ", row[0]
			#    print "currentdate = ", row[1]
			#    print "currenttime = ", row[2]
			#    print "speed = ", row[3]
			#    print "fuellevel = ", row[4] 
			#    print "coolanttemp = ", row[5],"\n"
			print ("Operation done successfully.")
			conn.close()
			return 1
		except sqlite3.Error as e:
			return 0 		