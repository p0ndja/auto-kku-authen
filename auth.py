try:
    import requests
    import time
except:
    print("Module `")
    exit(0)

auth = "http://nac06.kku.ac.th/"

payload = {
    'username': '6330401661',
    'password': 'P0ndJ@1103',
}
headers = {'User-Agent': 'Mozilla/5.0'}

time_interval = 30*60 #second

def check_internet()->bool:
    gateway = requests.get(f"{auth}status")
    return gateway.url != f"{auth}status"

while(1):
    if (check_internet()):
        #KKU Gateway redirection you from /status to /login
        response = requests.get(f"{auth}login?username={payload['username']}&password={payload['password']}", headers=headers)
        if (check_internet()):
            print("Can't login, Please config Authentication data!")
            exit(0)
        else:
            print(f"Logged-in!\nAuth: {auth}login\nUser: {payload['username']}\nPass: {payload['password']}\nHappy to use KKU Internet!")
    else:
        print("Your Internet seem to be OK!")

    time.sleep(time_interval)