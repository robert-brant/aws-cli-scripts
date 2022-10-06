import json, os

#get json
f = open('script-admin-security-group-id.json')
data = json.load(f)
os.system('aws ec2 describe-security-groups --group-ids ' + data['GroupId'])
f.close()
