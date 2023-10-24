client_id = 'NmzOQUtCep6wWTwrUxNawS4GDOwJfDPuZTPuXrkc'
client_secret = 'P6REwLZbL2hBe2zfQKo82txAFB7LvBMBBPqMSp7CITCTWmxaL0RFsME3r4GP8q6Nkbjr82WwCcp6yMl1NOrvf8EhcWy66Tc6MDWbUzXmDWmSkaRMpaKT3yC6r4QTr9jt'
redirect_uri = 'http://localhost:8000/home/'
success_string1 = "fuck"
import requests


URL = '/oauth/authorise/?client_id=' + client_id + '<&redirect_uri=' + redirect_uri + '><&state=' + success_string1 + '>'
url = 'https://channeli.in/oauth/authorise'
params = {'client_id':'NmzOQUtCep6wWTwrUxNawS4GDOwJfDPuZTPuXrkc', 'redirect_uri' : 'http://localhost:8000/home/','state':'yay its working part1'}


print("before the request")
response = requests.get(url, params=params)

print("outer print")
if response.status_code == 200:
    print("status code is correct")
    print(response)
    # data = response.json()
    # Now, 'data' contains the response data in JSON format
    # print(data)
else:
    print(f"Error: {response.status_code}")

print(URL)