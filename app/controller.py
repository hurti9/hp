import os
from werkzeug import security

def new_password(password):
    generated_password = security.generate_password_hash(password)
    return generated_password
def check_password(password, hash):
    return security.check_password_hash(hash, password)

