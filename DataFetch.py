import obd
import time
import serial
#from OBDCodes import Codes

class FetchObd:
	@staticmethod
	def fetch_protocols():
		obd.logger.setLevel(obd.logging.DEBUG)   # debug
		ports = obd.scan_serial()                # return list of valid USB or RF ports
		print("PORTS:",ports)                             # ['/dev/ttyUSB0', '/dev/ttyUSB1']
		connection = obd.OBD(ports[0], baudrate=38400, fast=False)
		# cmd = obd.commands.PIDS_A
		# response = connection.query(cmd)
		# accepted_protocols=[]
		# for pid in range(0,32):
		# 	print(response.value[pid])
		# 	if response.value[pid] == True:
		# 		accepted_protocols.append(hex(pid))
		return connection
	@staticmethod
	def fetch_data(connection):
		#connection = FetchObd.fetch_protocols()
		dict = {}
		cmd = obd.commands.COOLANT_TEMP
		response = connection.query(cmd)
		if not response.is_null():
			print("COOLANT_TEMP : ",response.value)
			dict['COOLANT_TEMP'] = response.value.magnitude
		# dict['COOLANT_TEMP'] = 38
		cmd = obd.commands.SPEED
		response = connection.query(cmd)
		if not response.is_null():
			print("SPEED : ",response.value)
			dict['SPEED'] = response.value.magnitude
		# dict['SPEED'] = 0
		cmd = obd.commands.RPM
		response = connection.query(cmd)
		if not response.is_null():
			print("RPM : ",response.value)
			dict['RPM'] = response.value.magnitude
		# dict['RPM'] = 100
		cmd = obd.commands.STATUS
		response = connection.query(cmd)
		if not response.is_null():
			print("STATUS : ",response.value.MIL)
			print("Status : ",response.value.DTC_count)
			dict['EngineStatus'] = response.value.MIL
			if response.value.MIL == True:
				cmd = obd.commands.GET_DTC
				response = connection.query(cmd)
				print("DTC : ",response.value)
				dict['DTC'] = response.value
		return dict
