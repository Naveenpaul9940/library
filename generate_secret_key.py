import secrets

new_secret_key = secrets.token_urlsafe(50)
print(new_secret_key)