# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 14:41:53 2021

@author: akhil
"""

from ks_api_client import ks_api
from akhil_api import cred as akhil
import akhil_otp
import time

class login:
    def author():
        det = akhil()
        client = ks_api.KSTradeApi(access_token = det.access_token, userid = det.user_id, \
        consumer_key = det.consumer_key, ip = det.ip, app_id = det.app_id)
        try:
            client.login(password=det.password)
            print('Logged in')
        except Exception as e:
            print("Exception when calling Session Api->login: %s\n" % e)
        
        try:
            client.positions(position_type='OPEN')
        except:
            time.sleep(60)
            otp = akhil_otp.get_otp()
            client.session_2fa(access_code = otp)
            print('Session initialized. OTP = ',otp)
        
        return client
