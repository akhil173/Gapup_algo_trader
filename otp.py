# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:23:50 2021

@author: akhil
"""

import imaplib
import email
import html
import re

host = 'imap.gmail.com'
username = 'akhil.sa352001@gmail.com'
password = 'Akhil@0305'


def get_otp():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'FROM "accesscode@kotaksecurities.com"')
    my_message = []
    num = search_data[0].split()[-1]
    email_data = {}
    _, data = mail.fetch(num, '(RFC822)')
        # print(data[0])
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    for header in ['subject', 'to', 'from', 'date']:
        email_data[header] = email_message[header]

    otp = re.search(r'\d\d\d\d', email_data['subject']).group()
    print(otp)
    return otp


# f = open('token.json')
# data = json.load(f)
# url = 'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=ya29.a0ARrdaM-PLgimF3SKdH_BD0PEc78qqKML7DSSsYl2r2Lu5nF3lMLWxXuQ1vE-FyfYewVC6mCMdBVlDvmixUiyb8OukEp_yVPD45QxlcqzKsdbkBOJ2dHR3aMXzHRlIB_a4-41HeAXcu29lHHY_L52W9Py23O4UA'
# access = requests.get(url)
# access_data = access.json()