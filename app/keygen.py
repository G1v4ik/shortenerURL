import secrets
import string


def create_random_key(length: int=5) -> str:
    chars = string.ascii_lowercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))
