"""
Created on 02/10/2019
@author: Zhangyu Wan
"""

import csv
import json
import input_api
import storage_mongo
import output_api
import alert_system

def main():
	# get info from input module
	patient_json = input_api.getPatientInfo()
	sensor_json = input_api.readSensorData()

	# connect to database
	db = storage_mongo.storage()
	db.connectMongob()

	# insert
	db.insert_mongo(patient_json, sensor_json)

	# alert
	alert_json = alert_system.alertCheck(sensor_json)

	# output
	patient = output_api.patient()
	patient.recieveFromAlert(alert_json)
	patient.send_alert_to_UI(db.read_mongo_patient("1234"))

	'''
	database function test

	'''
	print("=======================")
	print("database function test")
	print("=======================")
	# read
	print("--------------------")
	print("search by id")
	print("--------------------")
	print(db.read_mongo_patient("1234"))
	print("--------------------")
	print('serch by id and datetime')
	print("--------------------")
	print(db.read_mongo_time("1234", '12:05:20pm-18/01/2019'))

	# update
	db.update_mongo("1234", '12:05:20pm-18/01/2019', 'age', '25')
	print('===============================================================')
	print('read from database after update (change the age from 30 to 25)')
	print('==============================================================')
	print(db.read_mongo_patient("1234"))

	# delete 
	db.delete_mongo_patient("1234")
	db.delete_mongo_time("1234",'12:05:20pm-18/01/2019')
	print('================================')
	print('read from database after delete')
	print('================================')
	print(db.read_mongo_patient("1234"))


if __name__ == '__main__':
	main()