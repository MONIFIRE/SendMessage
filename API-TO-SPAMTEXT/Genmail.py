import requests
import random
import json
import time
import re
import random
import string
import os
import shutil
from __pangsms__.register_id import register_pull
from __pangsms__.bypassID import bypass
User = ''.join(random.choice(string.ascii_letters) for _ in range(10))
Numbers = random.randint(10000000, 99999999)
python_cmd = shutil.which('python') or shutil.which('python3')
def generate_fake_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

fake_ip = generate_fake_ip()
session = requests.Session()

def _GenEmail():
    zort = session
    zort.headers.update({
        "name": "X-Forwarded-For","value": f"{fake_ip}"
    })
    Response_rmail = zort.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
    if Response_rmail.status_code == 200:
        Mail=Response_rmail.json()
        register_pull(User, Numbers, Mail[0])
        mail=Response_rmail.json()[0]
        mail_domain = "@" + mail.split("@")[-1] if "@" in mail else ""
        mail_name = mail.split("@")[0] if "@" in mail else mail
        name=mail_name
        domain=mail_domain[1:]
        email_data = {"name": name,"domain": domain}
        file_name = "Getmail/Email.json"
        with open(file_name, "w") as json_file:
             json.dump(email_data, json_file)
        time.sleep(1)
        with open('Getmail/Email.json', 'r') as file:
            data = json.load(file)
        user = data['name']
        email = data['domain']
        while True:
            rdomain = zort.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={email}').json()
            if rdomain:
                ids = [item['id'] for item in rdomain]
                if ids:
                   MessID=ids[0]
                   Getmass=zort.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={email}&id='+str(MessID)).json()
                   text_body = Getmass['textBody'].replace('\n', '')
                   Messbody = {"text": text_body}
                   file_names = "Pullcontent/textBody.json"
                   with open(file_names, "w") as json_files:
                        json.dump(Messbody, json_files)
                   pattern = r"https://www\.pangsms\.com/activate\?keycode=[A-Za-z0-9/+=]+=="
                   matches = re.findall(pattern, text_body)
                   for match in matches:
                       codes=match
                   bypass(codes)
                   if python_cmd:
                      os.system(f'{python_cmd} sendsms.py')
                   else:
                      print("คุณยังไม่ได้ติดตั้งภาษา python !!")
                   break
            time.sleep(5)
    else:print(f"Error: {Response_rmail}")

_GenEmail()

