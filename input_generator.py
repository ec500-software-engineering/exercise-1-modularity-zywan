'''
Created on 02/11/2019
@author: Zhangyu Wan
'''
import json
import random
import time
def generate():
	# gender_list = ['Male', 'Female']
	# name_list = ['a', 'b', 'c', 'd', 'e']
	# generate random patient information
	patient_dict = {
		# "patiendId": str(random.randint(1, 100)),
		# "gender": random.choice(gender_list),
		# "name": random.choice(name_list),
		# "age": str(random.randint(1,70))
			"patientId": "001",
			"gender": "Male",
			"name": "Jack",
			"age": "20"
		}

	patient_json = json.dumps(patient_dict)
	# generate random sensor data
	sensor_dict = {
		patient_dict["patientId"]:{
			"pulse": str(random.randint(40,130)),
			'pulseRange': {"lower": '50', "upper": '120'},
			'bloodPressure': str(random.randint(10,140)),
			'pressureRange': {'lower': '30', 'upper': '100'},
			'bloodOx': str(random.randint(50,100)),
			'oxRange': {'lower': '60', 'upper': '90'},
			'time': time.ctime(time.time())
		}
	}
	sensor_json = json.dumps(sensor_dict)
	return patient_json, sensor_json
