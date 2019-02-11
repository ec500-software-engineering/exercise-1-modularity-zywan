'''
Copied from https://github.com/alexlin0625/EC500_Spring19/blob/input_module/input.py
'''
import csv
import json

def checkInput(header,row):
	error = 0
	for i,value in enumerate(row):
		if value == "":
			error = 1
			print(header[i] + " is missing")
	return error

def getPatientInfo():
	with open("patientdetails.csv") as csvfile:
		readCsv = csv.reader(csvfile, delimiter=',')
		for i,row in enumerate(readCsv):
			if i==0:
				header= row
				continue
			else:
				patientdata = {}
				if checkInput(header,row)==0:
					patientId = row[0]
					name = row[1]
					gender = row[2]
					age = row[3]
					patientdata[patientId] = {'name':name,'gender':gender,'age':age}
					json_string = json.dumps(patientdata)
					return json_string

def readSensorData():
	with open("sensorinput.csv") as csvfile:
		readCsv = csv.reader(csvfile, delimiter=',')
		for i,row in enumerate(readCsv):
			if i==0:
				header= row
				continue
			else:
				sensordata = {}
				if checkInput(header,row)==0:
					patientId = row[0]
					pulse = row[1]
					pulseRangeLower = row[2]
					pulseRangeUpper = row[3]
					bloodPressure = row[4]
					pressureRangeLower = row[5]
					pressureRangeUpper = row[6]
					bloodOx = row[7]
					oxRangeLower = row[8]
					oxRangeUpper = row[9]
					time = row[10]
					sensordata[patientId] = {'pulse': pulse,
					'pulseRange': {'lower': pulseRangeLower, 'upper': pulseRangeUpper},
					'bloodPressure': bloodPressure,
					'pressureRange': {'lower':pressureRangeLower, 'upper':pressureRangeUpper},
					'bloodOx': bloodOx,
					'oxRange': {'lower':oxRangeLower, 'upper':oxRangeUpper},
					'time': row[10]}
					json_string = json.dumps(sensordata)
					return json_string


