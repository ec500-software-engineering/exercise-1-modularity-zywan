"""
Created on 02/11/2019
@author: Zhangyu Wan
"""

import input_generator
import storage_mongo
import output_api
import alert_system
import threading
import time
from queue import Queue

def input_generate(q):
	while True:
		time.sleep(3)
		print('generate random input data')
		# get info from input generator
		patient_json, sensor_json = input_generator.generate()
		# connect to database
		db = storage_mongo.storage()
		db.connectMongob()
		# insert
		db.insert_mongo(patient_json, sensor_json)
		# create a event
		evt = threading.Event()
		# push the event into queue
		q.put((sensor_json, evt))
		print("wait for the data to be process")

def alert(q,q1):
	while True:
		time.sleep(1)
		sensor_json, evt = q.get()
		# alert
		print("process the data to get the alert json")
		alert_json = alert_system.alertCheck(sensor_json)
		evt = threading.Event()
		q1.put((alert_json,evt))
		print("wait for output")



def output(q,q1):
	while True:
		alert_json, evt = q1.get()
		db = storage_mongo.storage()
		db.connectMongob()
		patient = output_api.patient()
		patient.recieveFromAlert(alert_json)
		patient.send_alert_to_UI(db.read_mongo_patient("001"))
		print("\n")

def main():
	q = Queue()
	q1 = Queue()
	thread_input = threading.Thread(target = input_generate, args=(q,))
	thread_alert = threading.Thread(target = alert, args=(q,q1,))
	thread_output = threading.Thread(target = output, args = (q,q1,))
	thread_input.start()
	thread_alert.start()
	thread_output.start()
	q.join()
	q1.join()


if __name__ == '__main__':
	main()
