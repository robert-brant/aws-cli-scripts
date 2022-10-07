import json, os

#### THIS SCRIPT CREATES AN EC2 INSTANCE FOR AN IAM USER THAT ALLOWS THEM TO RUN ALL NECESSARY FUNCTIONS FOR MANAGING AN AWS BUILD PIPELINE ####

#The user-ec2-config.json is manually created/edited with account and vpc details.
configFile = 'user-ec2-config.json'

## LOAD CONFIG FILE ##
f = open(configFile)
configData = json.load(f)

### CREATE INSTANCE PROFILE, ROLE AND POLICIES ###
print("Creating script user role with command:")
roleCommand = "aws iam create-role --role-name script-{}-role --assume-role-policy-document file://aws_service_trust_policy.json".format(configData['iam-user'])
print(roleCommand)
os.system(roleCommand)
print("Role created.")
policyCommand = "aws iam create-policy --policy-name ecr-codebuild-all-resources --policy-document file://policies/ecr_codebuild_all_resources.json"
print("Creating policy with command:")
print(policyCommand)
print("Policy Created.")
os.system(policyCommand)
attachPolicyCommand = "aws iam attach-role-policy --role-name script-{}-role --policy-arn arn:aws:iam::{}:policy/ecr-codebuild-all-resources".format(configData['iam-user',configData['accound-id')
print("Attaching policy to role with command:")
print(attachPolicyCommand)
os.system(attachPolicyCommand)
print("Policy Attached.")
instanceProfileCommand = "aws iam create-instance-profile --instance-profile-name script-{}-profile".format(configData['iam-user'])
print("Creating instance profile with command:")
print(instanceProfileCommand)
os.system(instanceProfileCommand)
print("Instance profile created.")
addRoleToInstanceProfileCommand="aws iam add-role-to-instance-profile --instance-profile-name script-{}-profile --role-name script-{}-role".format(configData['iam-user'],configData['iam-user'])
print("Attaching Role to Instance Profile with command:")
print(addRoleToInstanceProfileCommand)
os.system(addRoleToInstanceProfileCommand)
print("Role attached to Instance Profile.")


### CREATE KEY PAIR FOR CONNECTING TO EC2 INSTANCE ###
#The .pem file created here is used to ssh into the user ec2 instance with the command:
# ssh -i script-user-key-pair.pem ec2-user@<PublicDnsName>
# PublicDnsName should be in the user-instance-details.json or can be found using the instance id found in the user-instance-details.json with the following query:
# aws ec2 describe-instances --instance-ids <instance id> --query 'Reservations[].Instances[].PublicDnsName'
keyCommand = "aws ec2 create-key-pair --key-name script-{}-key-pair > script-{}-key-pair.pem".format(configData['iam-user'],configData['iam-user'])
# DEBUG print statement
# print(keyCommand)
# execute command
os.system(keyCommand)

### CREATE SECURITY GROUP FOR THE EC2 INSTANCE ###
securityCommand = "aws ec2 create-security-group --group-name script-{}-security-group --description 'Security group for managing build pipeline resources' --vpc-id {} > script-{}-security-group-id.json".format(configData['iam-user'],configData['vpc-id'],configData['iam-user'])
#DEBUG print statement
# print(securityCommand)
# execute command
os.system(securityCommand)

securityGroupIdFile = "script-{}-security-group-id.json".format(configData['iam-user'])
f2 = open(securityGroupIdFile)
securityData = json.load(f2)

### GRANT PERMISSION TO CONNECT FROM IP ADDRESS ###
ingressCommand = "aws ec2 authorize-security-group-ingress --group-id {} --protocol ssh --port 22 --cidr {}".format(securityData['GroupId'],configData['ip-address'])
#DEBUG print statement
# print(ingressCommand)
# execute command
os.system(ingressCommand)

### BUILD AND START THE EC2 INSTANCE ###
buildCommand = "aws ec2 run-instances --image-id {} --count 1 --instance-type t2.micro --key-name script-{}-key-pair --security-group-ids {} --tag-specifications 'ResourceType=instance,Tags=[{{Key=Name,Value=script-user}}]' > user-instance-details.json".format(configData['ami-id'],configData['iam-user'],securityData['GroupId'])
#DEBUG print statement
# print(buildCommand)
# execute command
os.system(buildCommand)

### ATTACH SECURITY TO THE RUNNING INSTANCE ###
#user-instance-details is created when buildCommand is executed successfully.
f3 = open('user-instance-details.json')
instanceData = json.load(f3)
iamCommand = "aws ec2 associate-iam-instance-profile --instance-id {} --iam-instance-profile Name=script-user-profile".format(instanceData['Instances'][0]['InstanceId'])

# DEBUG print statement
# print(iamCommand)
# excute command
os.system(iamCommand)
