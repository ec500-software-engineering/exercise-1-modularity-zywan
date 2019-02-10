'''
Create on 02/10/2019
@author: Zhangyu Wan
I use new version of alert system module modified by XiangKun Ye
'''

'''
Created on 02/10/2019
@author: Xiangkun Ye
Source code copied from https://github.com/alexlin0625/EC500_Spring19/blob/alert-system/alert_system.py.
With lots of modifications to make it work.
Basically I rewrited the whole file.
The original one by mohitbeniwal is bullshit.
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:29:32 2019

@author: mohitbeniwal
"""
import json


def sendToUI(msg,j):
    ui_dict={"alert_message":msg,"bloodPressure":j["bloodPressure"],"pulse":j["pulse"],"bloodOx":j["bloodOx"]}
    ui_json=json.dumps(ui_dict)
    return ui_json


def alertCheck(j_o):
    j=json.loads(j_o)
    alert_message=""
    for value in j.values():
        val = value
    if(val["bloodPressure"]<val["pressureRange"]["lower"]):
        alert_message+="BloodPressure is Too low, "
    elif(val["bloodPressure"]>val["pressureRange"]["upper"]):
        alert_message="BloodPressure is Too high, "
    if(val["pulse"]<val["pulseRange"]["lower"]):
        alert_message+="Pulse is Too low, "
    elif(val["pulse"]>val["pulseRange"]["upper"]):
        alert_message+="Pulse is Too high, "
    if(val["bloodOx"]<val["oxRange"]["lower"]):
        alert_message+="BloodOx is Too low, "
    elif(val["bloodOx"]>val["oxRange"]["upper"]):
        alert_message+="BloodOx is Too high, "
    return sendToUI(alert_message, val)
