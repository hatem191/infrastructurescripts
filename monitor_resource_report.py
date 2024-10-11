# Monitor Cloud Resource Usage and Generate Reports

import boto3

def generate_ec2_usage_report():
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    report = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            report.append({
                'InstanceId': instance['InstanceId'],
                'State': instance['State']['Name'],
                'LaunchTime': instance['LaunchTime'].strftime('%Y-%m-%d %H:%M:%S')
            })
    print("EC2 Usage Report:")
    for r in report:
        print(r)

# Example usage
generate_ec2_usage_report()
