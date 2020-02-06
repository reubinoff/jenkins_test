import requests
import cloudshell.api.cloudshell_api as cs_api

IP = "172.29.204.190"
blueprint = "EmptyCustomSetup 0"
session = cs_api.CloudShellAPISession(IP, 'admin', 'admin', 'Global')
resourceDict = {}
res = session.CreateImmediateReservation(blueprint, "admin",5)


print(res)
ID = res.Reservation.Id


url = "https://ynet.co.il"
body = dict()
res = requests.get(url)
assert(res.status_code == 200)



session.EndReservation(ID)
