import secrets
import os

# Generate a secure random secret key
secret_key = secrets.token_hex(16)  # 16 bytes (32 characters) is a common choice

# Set the Flask secret key as an environment variable
os.environ['FLASK_SECRET_KEY'] = secret_key
