#!/bin/bash
#Create the scripts admin role and attach required policies
AccountID=682591188398
aws iam create-role --role-name script-admin-role --assume-role-policy-document file://aws_service_trust_policy.json
aws iam create-policy --policy-name ec2-script-admin --policy-document file://policies/ec2_admin.json
aws iam create-policy --policy-name iam-script-admin --policy-document file://policies/iam_admin.json
aws iam attach-role-policy --policy-arn arn:aws:iam::$AccountID:policy/ec2-scripts-admin
aws iam attach-role-policy --policy-arn arn:aws:iam::$AccountID:policy/iam-scripts-admin
aws iam create-instance-profile --instance-profile-name script-admin-profile
aws iam add-role-to-instance-profile --instance-profile-name script-admin-profile --role-name script-admin-role
