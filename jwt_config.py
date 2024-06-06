import secrets

def generate_jwt_secret_key(length=32):
    return secrets.token_urlsafe(length)

# Generate a JWT secret key of 64 characters (default length)
jwt_secret_key = generate_jwt_secret_key()
print("JWT Secret Key:", jwt_secret_key)