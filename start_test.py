import requests
import cloudshell.api.cloudshell_api as cs_api

# IP = "52.177.135.165"
# blueprint = "shared device11"
# session = cs_api.CloudShellAPISession(IP, 'admin', 'admin', 'Global')
# resourceDict = {}
# res = session.CreateImmediateReservation(blueprint, "admin",5)
# print(res)



url = "https://ynet.co.il"
body = dict()
res = requests.get(url)
assert(res.status_code == 200)

