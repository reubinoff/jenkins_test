import requests
import cloudshell.api.cloudshell_api as cs_api

# IP = "52.177.135.165"
# blueprint = "shared device11"
# session = cs_api.CloudShellAPISession(IP, 'admin', 'admin', 'Global')
# resourceDict = {}
# res = session.CreateImmediateReservation(blueprint, "admin",5)
# print(res)



url = "https://verison-robot.azurewebsites.net/api/perfecto?code=x5u5GaCpIgGsw34YIYoo5HL/oWA6sIgTnReZKsurUdJisN3WXn3SDA=="
body = dict()
res = requests.post(url, body)
assert(res.status_code == 200)

