import json, os

configFile = 'admin-ec2-config.json'
securityGroupFile = 'script-admin-security-group-id.json'
f = open(configFile)
configData = json.load(f)
f2 = open(securityGroupFile)
securityData = json.load(f2)
os.system('aws ec2 run-instances --image-id '+ configData('ami-id')
        + ' --count 1 --instance-type t2.micro --key-name ' + configData('key-pair')
        + ' --security-group-ids ' + securityData('GroupId')
        + ' --subnet-id ' + configData('subnet'))
