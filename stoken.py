from itsdangerous import URLSafeTimedSerializer
from key import secret_key,salt
def token(data,salt):
    serialiazer=URLSafeTimedSerializer(secret_key)
    return serialiazer.dumps(data,salt=salt)
