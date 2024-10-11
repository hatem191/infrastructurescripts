# Encrypt Sensitive Data Using Python

from cryptography.fernet import Fernet

def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Generate a key (do this once and store it securely)
key = Fernet.generate_key()

# Example usage
encrypted_data = encrypt_data("Sensitive information", key)
print(f"Encrypted data: {encrypted_data}")
