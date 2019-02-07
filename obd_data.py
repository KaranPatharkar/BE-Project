import obd
import time
obd.logger.setLevel(obd.logging.DEBUG)

ports = obd.scan_serial()      # return list of valid USB or RF ports
print(ports)                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']
connection = obd.OBD(ports[0])

 # auto-connects to USB or RF port
#time.sleep(60)
#cmd = obd.commands.COOLANT_TEMP # select an OBD command (sensor)
#cmd = obd.commands.FUEL_LEVEL
#cmd = obd.commands.SPEED
cmd = obd.commands.RPM
response = connection.query(cmd) # send the command, and parse the response
#time.sleep(60)
print("RPM",response.value) # returns unit-bearing values thanks to Pint
