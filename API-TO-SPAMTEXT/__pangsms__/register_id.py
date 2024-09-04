import requests,json,os
def register_pull(userID, phoneID, mailID):
    url = "https://www.pangsms.com/register"
    data = {
        "uname": userID,
        "pwd": "098098az",
        "cpwd": "098098az",
        "email": mailID,
        "phone": "09"+str(phoneID),
        "chkNews": "1",
        "chkCondition": "1",
        "submit.x": "39",
        "submit.y": "30"
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
       login_data = {"username": userID,"password": "098098az"}
       file_name1 = "__pangsms__/login.json"
       file_name2 = "login.json"
       with open(file_name1, "w") as json_file:
            json.dump(login_data, json_file)
       with open(file_name2, "w") as json_file:
             json.dump(login_data, json_file)
       print("\n• Creating your account..")
    else:print("\nข้อผิดพลาด:", response.status_code)
