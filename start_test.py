import requests


url = "https://verison-robot.azurewebsites.net/api/perfecto?code=x5u5GaCpIgGsw34YIYoo5HL/oWA6sIgTnReZKsurUdJisN3WXn3SDA=="
body = dict()
res = requests.post(url, body)
assert(res.status_code == 200)

