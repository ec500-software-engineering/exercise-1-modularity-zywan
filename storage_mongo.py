"""
Created on 02/10/2019
@author: Zhangyu Wan
"""


import pymongo
import json

class storage:
	'''
	class for storage of data from input module
	basic functions: CRUD(create, read, update, delete)
	'''
	def connectMongob(self):
		'''
			connect to the mongodb
		'''
		self.client = pymongo.MongoClient()
		self.mydb = self.client.hospital
		self.mycol = self.mydb.patient

	def insert_mongo(self, patient_json, sensor_json):
		'''
			add data to the mongodb
		'''
		patient_data = json.loads(patient_json)
		sensor_data = json.loads(sensor_json)

		patient_dict = {}
		patientId = patient_data["patientId"]
		for key, value in patient_data.items():
			patient_dict[key] = value
		for key, value in sensor_data[patientId].items():
			patient_dict[key] = value
		insert = self.mycol.insert_one(patient_dict)

	def delete_mongo_patient(self, patientID):
		'''
			delete all data of one patient
		'''
		query = { "patientId": patientID }

		# delete
		self.mycol.delete_many(query)


	def delete_mongo_time(self, patientID, datetime):
		'''
			delete patient data at specific time
		'''
		query = { "patientId": patientID, "time": datetime}

		# delete
		self.mycol.delete_one(query)


	def update_mongo(self, patientID, datetime, item, data):
		'''
			update data
		'''
		query = {"patientId": patientID, "time": datetime}
		updated_data = {"$set": {item: data}}
		self.mycol.update_one(query, updated_data)


	def read_mongo_patient(self, patientID):
		'''
			read data of patient
		'''
		data = []
		for info in self.mycol.find({'patientId': patientID}):
 			data.append(info)

		return data

	def read_mongo_time(self, patientID, datetime):
		'''
			read data of patient and specific time
		'''
		data = []
		for info in self.mycol.find({'patientId': patientID, 'time': datetime}):
			data.append(info)

		return data

def main():
	drop = storage()
	drop.connectMongob()
	drop.mycol.drop()
if __name__ == '__main__':
	main()
