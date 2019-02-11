import json
import os


class patient(object):
    def __init__(self):
        self.name = "test"

    def set_bp_id(self, bp_id):
        self.bp_id = bp_id

    def set_pulse_id(self, pulse_id):
        self.pulse_id = pulse_id

    def set_temp_id(self, temp_id):
        self.temp_id = temp_id

    def get_bp_id(self, bp_id):
        return bp_id

    def get_pulse_id(self, pulse_id):
        return pulse_id

    def get_temp_id(self, temp_id):
        return temp_id

    def recieveFromAlert(self, rawJson):
        data = json.loads(rawJson)
        self.msg = data["alert_message"]
        self.bp_id = data["bloodPressure"]
        self.pulse_id = data["pulse"]
        self.temp_id = data["bloodOx"]

    def recieveFromUsers(self, data):
        self.user_req = data["req"]
        self.select(self.user_req)

    def select(self, req):
        data = ''
        if req == "bloodPressure":
            data = self.bp_id
        elif req == 'pulse':
            data = self.pulse_id
        elif req == 'bloodOx':
            data = self.temp_id
        self.send_select_to_UI(req, data)

    def send_alert_to_UI(self, patient_info):
        print('===================================')
        print('Welcome to Health Monitoring System')
        print('===================================')
        print('PatientID: ', patient_info[0]['patientId'])
        print('Gender: ', patient_info[0]['gender'])
        print('Age: ', patient_info[0]['age'])
        print('===============================')
        print('alert_message: ', self.msg)
        print('pulse: ', self.pulse_id)
        print('bloodPressure: ', self.bp_id)
        print('bloodOx: ', self.temp_id)
        print('===============================')
        # send_data = json.dumps({
        #     'alert_message': self.msg,
        #     'bloodPressure': self.bp_id,
        #     'pulse': self.pulse_id,
        #     'bloodOx': self.temp_id
        # })
        # # print(send_data)
        # return send_data

    def send_select_to_UI(self, req, data):
        send_data = json.dumps({
            req: data
        })
        print(send_data)
        return send_data


def main():
    patient_1 = patient()
    json_dir = os.getcwd()
    with open(json_dir + '/patient.json', 'r') as rawJson:
        patient_1.recieveFromAlert(rawJson)
        patient_1.send_alert_to_UI()
        rawJson.close()

    with open(json_dir + '/users.json', 'r') as rawJson:
        data = json.load(rawJson)
        patient_1.recieveFromUsers(data)
        rawJson.close()


if __name__ == "__main__":
    main()
