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

	# read
	print('==========================')
	print('read from datebase')
	print('==========================')
	print(db.read_mongo_patient("1234"))
	print(db.read_mongo_time("1234", '12:05:20pm-18/01/2019'))

	# update
	db.update_mongo("1234", '12:05:20pm-18/01/2019', 'age', '25')
	print(db.read_mongo_patient("1234"))
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

	# alert
	alert_json = alert_system.alertCheck(sensor_json)

	# output
	print('==========================')
	print('alert information output')
	print('==========================')
	patient = output_api.patient()
	patient.recieveFromAlert(json.loads(alert_json))
	patient.send_alert_to_UI()
	


if __name__ == '__main__':
	main()