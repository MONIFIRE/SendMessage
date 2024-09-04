import requests,json,os,time,pytz,shutil,ping3
from bs4 import BeautifulSoup, Comment
from datetime import datetime
from colored import fg, attr
_filename = "login.json"
__path1 = _filename
with open(__path1, 'r') as ____file:
     ___data = json.load(____file)
myusername = ___data['username']
host="google.com"
def check_ping(host):
    response_time = ping3.ping(host)
    if response_time is None:
        return f"Ping failed."
    else:
        return f"{response_time * 1000:.2f} ms."
python_cmd = shutil.which('python') or shutil.which('python3')
def rainbow_text(text):
    rainbow_colors = [fg('red'), fg('orange_1'), fg('yellow'), fg('green'), fg('cyan'), fg('blue'), fg('purple_1a')]
    reset = attr('reset')
    colored_text = ""
    for i, char in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        colored_text += f"{color}{char}{reset}"
    return colored_text
thailand_tz = pytz.timezone('Asia/Bangkok')
thailand_time = datetime.now(thailand_tz)
os.system("clear")
r = requests.get('https://ipinfo.io/json').json()

def red_text(text):
    red_color = fg('red')
    reset = attr('reset')
    colored_text = f"{red_color}{text}{reset}"
    return colored_text
def Function():
    amui=f'''
⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠐⠢⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠉⠀⠀⠀⠱⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⣮⣑⠡⡀⡀⠀⢀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⢠⣿⣄⠈⣌⠪⡄⢰⢡⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠈⢿⣾⣀⠈⢂⠃⡈⠘⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣷⣄⠤⢢⠁⡠⠂⠢⡀⠀
⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⣸⡿⠟⣾⠓⠉⡖⠀⠀⠈⢂
⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⡏⢸⠟⠀⣾⠀⠈⢡⡠⠂⠀⠈
    ⠱⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⡀⡇⢈⠐⠠⡟⠀⠀⢞⡿⢅⠄⢀
⠀    ⠹⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠊⢛⡃⠘⠀⠀⡇⠀⡈⠶⠄⠒⠂⡔
⠀    ⠀⠘⣿⣿⣿⣷⣄⣀⠀⠤⡠⡤⠒⠫⠱⠀⣼⠧⠀⠀⠀⢁⠠⢱⠤⠒⠒⣠⠇
⠀    ⠀⠀⠘⢿⣿⣿⣿⣾⡷⡋⣞⠔⡣⠎⠙⠂⠘⠒⠲⡖⡒⠒⡶⢙⠀⠈⠉⣸⠀
⠀⠀    ⠀⠀⠀⠉⠻⣿⣿⡿⣿⣿⣯⠪⡖⠤⠤⠔⣀⣤⡃⠀⠀⡁⠀⣀⠄⠊⡜⠀
⠀⠀    ⠀⠀⠀⠀⠀⠈⠛⢿⡌⠙⢿⣾⡫⠅⠂⠉⠀⠀⠁⠪⢁⠈⠉⠀⠀⣸⠀⠀
⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠙⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠉⠀⠀
'''
    channel=f'''
\033[5;37;40mx Discord >\033[0;37;40m https://discord.com/invite/kXQUq2TavJ

\033[5;37;40m• AccountsIP >\033[0;37;40m {r['ip']}  \033[5;37;40mPing >\033[0;37;40m {check_ping(host)}

\033[5;37;40m× Timenow >\033[0;37;40m {thailand_time.strftime('%H:%M:%S')}  \033[5;37;40mUser >\033[0;37;40m {myusername}

\033[5;37;40m[ / = \033[0;37;40m\033[1;32;40mworking\033[0;32;40m\033[5;37;40m, x = \033[0;37;40m\033[1;31;40mcoming soon\033[0;31;40m, \033[5;37;40m! = \033[0;37;40m\033[1;34;40mupdating\033[0;34;40m \033[5;37;40m]\033[0;37;40m

\033[5;37;40m• SPAMMER FOR TEXT\033[0;37;40m (\033[1;32;40m/\033[0;32;40m)  \033[5;37;40m|  EXIT (CTRL + Z)\033[0;37;40m
'''
    print(rainbow_text(amui))
    print(channel)
Function()
prompt1='\033[5;37;40mx PhoneNumber: \033[0;37;40m'
sphone = input(prompt1)
print('')
prompt2='\033[5;37;40m• Messages: \033[0;37;40m'
smessages = input(prompt2)

filename = "login.json"
path1 = filename
try:
    with open(path1, 'r') as file:
        data = json.load(file)
    suser = data['username']
    spass = data['password']
    url = "https://www.pangsms.com/login"
    pull_data = {
        "lusername": suser,
        "lpassword": spass,
        "input.x": "76",
        "input.y": "31"
    }
    data = {
        "sender": "DOTSMS",
        "stelephone": sphone,
        "smessage": smessages,
        "smstype": "0",
        "sdate": "",
        "hour": "00",
        "min": "00",
        "hidcounttel": "0",
        "hidcountmessage": "0",
        "hidcountcredit": "0",
    }
    session = requests.Session()
    response = session.post(url, data=pull_data)
    if response.status_code == 200:
       cookies = session.cookies.get_dict()
       sms = session.post('https://www.pangsms.com/sendsms', data=data,cookies=cookies)
       if sms.status_code == 200:
          soup = BeautifulSoup(sms.content, 'html.parser')
          comments = soup.find_all(string=lambda text: isinstance(text, Comment))
          cadit_element = soup.find('td', class_='Cadit')
          for comment in comments:
              comment_soup = BeautifulSoup(comment, 'html.parser')
              cadit_element = comment_soup.find('td', class_='Cadit')
              if cadit_element:
                 cadit_text = cadit_element.get_text()[9:]
                 if int(cadit_text) == 0:
                    sends=f'\n\033[5;37;40m[\033[0;37;40m \033[1;35;40m{cadit_text}/5\033[0;35;40m \033[5;37;40m]\033[0;37;40m Successfully sent to \033[5;37;40m(\033[0;37;40m \033[1;35;40m{sphone}\033[0;35;40m \033[5;37;40m)\033[0;37;40m \033[5;37;40m(\033[0;37;40m \033[1;35;40m{smessages}\033[0;35;40m \033[5;37;40m)\033[0;37;40m'
                    print(sends)
                    print('\nx Starting a new program....')
                    if python_cmd:
                       os.system(f'{python_cmd} Genmail.py')
                    else:
                       print("คุณยังไม่ได้ติดตั้งภาษา python !!")
                 else:
                    sends=f'\n\033[5;37;40m[\033[0;37;40m \033[1;35;40m{cadit_text}/5\033[0;35;40m \033[5;37;40m]\033[0;37;40m Successfully sent to \033[5;37;40m(\033[0;37;40m \033[1;35;40m{sphone}\033[0;35;40m \033[5;37;40m)\033[0;37;40m \033[5;37;40m(\033[0;37;40m \033[1;35;40m{smessages}\033[0;35;40m \033[5;37;40m)\033[0;37;40m'
                    print(sends)
                    time.sleep(2)
                    os.system('clear')
                    if python_cmd:
                       os.system(f'{python_cmd} sendsms.py')
                    else:
                       print("คุณยังไม่ได้ติดตั้งภาษา python !!")
                    break
       else:print("\nเกิดข้อผิดพลาด:", sms.status_code)
    else:print("\nเกิดข้อผิดพลาด:", response.status_code)
except:pass
