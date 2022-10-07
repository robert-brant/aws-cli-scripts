import json, os, sys

### CREATE INSTANCE PROFILE, ROLE AND POLICIES ###

def createRole(roleFilePath, roleIamUser):
  #has role already been created
  checkRoleCommand = "aws iam get-role --role-name script-{}-role > script-{}-role.json".format(roleIamUser, roleIamUser)
  creeateRoleCommand = "aws iam create-role --role-name script-{}-role --assume-role-policy-document file://policies/aws_service_trust_policy.json > script-{}-role.json".format(roleIamUser,roleIamUser)

  if os.path.exists(roleFilePath):
    print("Role file found.")
    if not (os.stat(roleFilePath).st_size == 0):
      print("Role file size greater than 0.")
      roleFile = open(roleFilePath)
      roleData = json.load(roleFile)
      if "RoleName" in roleData['Role']:
        print("Role name that was found:")
        print(roleData['Role']['RoleName'])
    else:
      print("Role file empty.")
      os.system(checkRoleCommand)
      print("Role file created.")
      if os.path.exists(roleFilePath):
        print("Role file found.")
        if not (os.stat(roleFilePath).st_size == 0):
          roleFile = open(roleFilePath)
          roleData = json.load(roleFile)
          if "RoleName" in roleData:
            print("Role name in role file.")
            print(roleData['Role']['RoleName'])
  else:
    print("Role file not found, checking to see if it was already created.")
    os.system(checkRoleCommand)
    print("Role file created.")
    if os.path.exists(roleFilePath):
      print("Role file found.")
      if not (os.stat(roleFilePath).st_size == 0):
        roleFile = open(roleFilePath)
        roleData = json.load(roleFile)
        if "RoleName" in roleData['Role']:
          print("Role name in role file.")
          print(roleData['Role']['RoleName'])
        else:
          print("Creating script user role with command:")
          print(roleCommand)
          os.system(roleCommand)
          print("Role created.")
