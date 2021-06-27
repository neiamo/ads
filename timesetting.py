import os
import sys
import requests
os.environ['NO_PROXY'] = 'stackoverflow.com'

url = "https://api.m.jd.com/client.action?functionId=queryMaterialProducts&client=wh5"
r = requests.post(url).json()
timestr = r['currentTime'][-8:]
# print(rr)
comdd = 'date -s ' + timestr
print(comdd)
os.system(comdd)
sys.exit(0)
