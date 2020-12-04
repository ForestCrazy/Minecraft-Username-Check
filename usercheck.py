import urllib3
import certifi
import json

with open('userlist.txt') as f:
    for line in f:
        line = line.strip(' ').strip('\n')

        url = 'https://api.mojang.com/users/profiles/minecraft/'
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        try:
            r = http.request('GET', url + line)
            # print(str(url + line))
        except urllib3.exceptions.SSLError as e:
            print(str(e))

        try:
            r_data = json.loads(r.data.decode('utf-8'))
            # print(r_data)
        except Exception as e:
            # print(str(e))
            r_data = ""

        if r_data:
            print("Username: " + r_data['name'] + ", UUID: " + r_data['id'] + ", Paid: TRUE")
        else:
            print("Username: " + line + " UUID: N/A Paid: FALSE")