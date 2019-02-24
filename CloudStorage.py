from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

class CloudStore:
	def cloud_connect():
		client = Cloudant.iam("97791747-97ab-4405-8017-0b3f4d661109-bluemix", "bVvvWRZrFp5smkAr20u9-yltNY-w9k89_kXMzcacOsj6")
		client.connect()
		databaseName = "fleet_db"
		global myDatabase
		myDatabase = client.create_database(databaseName)
		if myDatabase.exists():
			print ("'{0}' successfully created.\n".format(databaseName))

	def cloud_insert(params):
		newDocument = myDatabase.create_document(params)
		# Check that the document exists in the database.
		if newDocument.exists():
			print ("Document successfully created.")
