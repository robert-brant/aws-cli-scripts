#!/bin/bash
# Creates the script user security group and attaches IP addresses which can use ssh to connect
VPCID=vpc-a814cad0
USERNAME=robertb
aws ec2 create-security-group --group-name script-$USERNAME-security-group --description "Security group for pipeline resources" --vpc-id $VPCID > script-admin-security-group-id.json
echo "Created script user security group."
