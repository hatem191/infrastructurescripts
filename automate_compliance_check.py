# Automate IAM Policy Compliance Check

import boto3


def check_iam_policies():
    iam = boto3.client('iam')
    policies = iam.list_policies(Scope='Local')['Policies']
    for policy in policies:
        policy_name = policy['PolicyName']
        policy_arn = policy['Arn']
        version = iam.get_policy(PolicyArn=policy_arn)['Policy']['DefaultVersionId']
        document = iam.get_policy_version(PolicyArn=policy_arn, VersionId=version)['PolicyVersion']['Document']

        # Check for overly permissive policies
        for statement in document.get('Statement', []):
            if statement.get('Effect') == 'Allow' and statement.get('Action') == '*':
                print(f"Policy {policy_name} is overly permissive")


# Example usage
check_iam_policies()
