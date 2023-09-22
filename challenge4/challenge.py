import jwt

def create_jwt(payload):
    token = jwt.encode(payload, key='', algorithm='none')
    return token

def create_jwt(payload, secret):
    token = jwt.encode(payload, key=secret, algorithm='HS256')
    return token