import obd
import time
import serial
from OBDCodes import Codes

class FetchObd:
	@staticmethod
	def fetch_protocols():
		obd.logger.setLevel(obd.logging.DEBUG)   # debug
		ports = obd.scan_serial()                # return list of valid USB or RF ports
		print(ports)                             # ['/dev/ttyUSB0', '/dev/ttyUSB1']
		connection = obd.OBD('COM10', baudrate=38400, fast=False)
		# cmd = obd.commands.PIDS_A
		# response = connection.query(cmd)
		# accepted_protocols=[]
		# for pid in range(0,32):
		# 	print(response.value[pid])
		# 	if response.value[pid] == True:
		# 		accepted_protocols.append(hex(pid))
		return connection

	@staticmethod
	def fetch_data():
		# connection = FetchObd.fetch_protocols()
		dict = {}
		# cmd = obd.commands.COOLANT_TEMP
		# response = connection.query(cmd)
		# print("COOLANT_TEMP : ",response.value)
		# dict['COOLANT_TEMP'] = response.value
		dict['COOLANT_TEMP'] = 38
		# cmd = obd.commands.SPEED
		# response = connection.query(cmd)
		# print("SPEED : ",response.value)
		# dict['SPEED'] = response.value
		dict['SPEED'] = 0
		# cmd = obd.commands.RPM
		# response = connection.query(cmd)
		# print("RPM : ",response.value)
		# dict['RPM'] = response.value
		dict['RPM'] = 100
		# command_list = []
		# for pid in protocol_list:
		# 	command = Codes.codes[pid]
		# 	command_list.append(command)
		# 	print(command)
		# 	cmd = obd.commands.STATUS
		# 	response = connection.query(cmd)
			
		# 	dict[command] = response.value
		return dict	


