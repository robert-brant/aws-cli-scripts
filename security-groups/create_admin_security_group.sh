#!/bin/bash
# Creates the script admin security group and attaches IP addresses which can use ssh to connect
VPCID=vpc-a814cad0
aws ec2 create-security-group --group-name script-admin-security-group --description "Security group for administering build pipeline resources" --vpc-id $VPCID > script-admin-security-group-id.json
echo "Created script admin security group."
