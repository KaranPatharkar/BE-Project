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
		connection = obd.OBD(ports[0], baudrate=38400, fast=False)
		cmd = obd.commands.PIDS_A
		response = connection.query(cmd)
		accepted_protocols=[]
		for pid in range(0,32):
			if response.value[pid] == 'True':
				accepted_protocols.append(hex(pid))
		return accepted_protocols
	@staticmethod
	def fetch_data():
		protocol_list = FetchObd.fetch_protocols()
		dict = {}
		for pid in protocol_list:
			command = Codes.codes[pid]
			cmd = obd.commands.command
			response = connection.query(cmd)
			dict[command] = response.value
		return dict	

