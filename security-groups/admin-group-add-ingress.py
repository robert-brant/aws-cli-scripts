import json, os

groupIdJSON = 'script-admin-security-group-id.json'
# from the machine you would like to access the ec2 instance from run:
# curl https://checkip.amazonaws.com
# the result is the ip address to add here. You can add multiple addresses if
# you want to connect from multiple ip addresses
ipAddress =
f = open(groupIdJSON)
data = json.load(f)
os.system('aws ec2 authorize-security-group-ingress --group-id ' + data['GroupId'] + '--protocol ssh --port 22 --cidr ' + ipAddress)
