#Automate Cloud Resource Cleanup with Terraform

import subprocess

def terraform_cleanup(directory):
    subprocess.run(["terraform", "init"], cwd=directory)
    subprocess.run(["terraform", "plan", "-destroy"], cwd=directory)
    subprocess.run(["terraform", "apply", "-auto-approve"], cwd=directory)
    print("Unused resources cleaned up.")

# Example usage
terraform_cleanup("/path/to/terraform/configs")
