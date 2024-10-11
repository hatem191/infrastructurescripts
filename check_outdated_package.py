# Check for Outdated Packages in CI/CD Pipeline

import subprocess

def check_outdated_packages():
    result = subprocess.run(['pip', 'list', '--outdated'], capture_output=True, text=True)
    if result.stdout:
        print("Outdated packages detected:")
        print(result.stdout)
    else:
        print("All packages are up-to-date.")

# Example usage
check_outdated_packages()
