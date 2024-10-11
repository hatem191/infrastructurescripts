# Automate Backup and Restore for Databases

import subprocess

def backup_postgres(db_name, user, output_file):
    subprocess.run(["pg_dump", "-U", user, "-F", "c", "-b", "-v", "-f", output_file, db_name])
    print(f"Backup for database {db_name} created at {output_file}")

# Example usage
backup_postgres("security_db", "admin", "backup_file.bak")
