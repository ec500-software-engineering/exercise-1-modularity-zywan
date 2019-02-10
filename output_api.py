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

    def recieveFromAlert(self, data):
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

    def send_alert_to_UI(self):
        send_data = json.dumps({
            'alert_message': self.msg,
            'bloodPressure': self.bp_id,
            'pulse': self.pulse_id,
            'bloodOx': self.temp_id
        })
        print(send_data)
        return send_data

    def send_select_to_UI(self, req, data):
        send_data = json.dumps({
            req: data
        })
        print(send_data)
        return send_data

