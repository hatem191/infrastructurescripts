# Automate Security Group Audit on AWS

import boto3

def audit_security_groups():
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups()
    for sg in response['SecurityGroups']:
        for rule in sg['IpPermissions']:
            if rule['IpProtocol'] == '-1' and any(ip['CidrIp'] == '0.0.0.0/0' for ip in rule.get('IpRanges', [])):
                print(f"Security Group {sg['GroupId']} has a rule allowing all traffic from any IP address")

# Example usage
audit_security_groups()
