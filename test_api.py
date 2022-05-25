from api_helper import ShoonyaApiPy
import logging
import yaml
import json
#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = ShoonyaApiPy()

#credentials
with open('cred.yml') as f:
    cred = yaml.load(f, Loader=yaml.FullLoader)
    print(cred)

ret = api.login(userid = cred['user'], password = cred['pwd'], twoFA=cred['factor2'], vendor_code=cred['vc'], api_secret=cred['apikey'], imei=cred['imei'])


print("-------------------------------Response---------------------------")
for keys in sorted(ret.keys()):
	print(keys)
print("-------------------------------------------------------")
for keys in ret.keys():
	print(str(keys) +':'+ str(ret[keys]))
	print("-------------------")
	
print("-------------------------------------------------------")
#response_info = json.dumps(ret)
#print(response_info)

