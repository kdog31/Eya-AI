import json
from pprint import pprint
import os
cwd = os.getcwd()
db = open(cwd+"/eyadb.json", "r")
data = json.loads(db.read())
print data['eya']['inputs']['positive responce']