import requests

gettheirpin = 'http://192.168.12.12:5000/api/EncryptedPin'
getmypin = 'http://192.168.12.12:5000/api/EncryptPin'
payload = {"pin": 99999}
for pin in range(10**4):
    payload["pin"] = '0' * (4 - len(str(pin))) + str(pin)
    my = requests.post(getmypin, json=payload).json()["encrypted_pin"]
    their = requests.get(gettheirpin).json()["encrypted_pin"]
    print(payload["pin"], my, their)
    if my == their:
        print(my, their, pin)
        break