# https://www.tutorialspoint.com/sqlite/sqlite_python.htm
import sqlite3

conn = sqlite3.connect('obd.db')

print "Opened database successfully";

conn.execute('''CREATE TABLE cardata
         (id INT PRIMARY KEY AUTO INCREMENT,
         currentdate DATE,
         currenttime TIME,
         speed INT,
         fuellevel INT,
         coolanttemp INT);''')
print "Table created successfully";

conn.execute("INSERT INTO COMPANY (currentdate,currenttime,speed,fuellevel,coolanttemp) \
      VALUES ();")

conn.commit()
print "Records created successfully";

# cursor = conn.execute("SELECT * from cardata;")
# for row in cursor:
#    print "ID = ", row[0]
#    print "currentdate = ", row[1]
#    print "currenttime = ", row[2]
#    print "speed = ", row[3]
#    print "fuellevel = ", row[4] 
#    print "coolanttemp = ", row[5],"\n"

print "Operation done successfully";

conn.close()