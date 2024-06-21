from datetime import timedelta
import datetime
import uuid
import bcrypt
import jwt
from src import config


def encode_jwt(
    payload: dict,
    private_key: str = config.private_key_path.read_text(),
    algorithm: str = config.algorithm,
    expire_minutes: int = config.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,
) -> str:
    
    to_encode = payload.copy()
    now = datetime.utcnow()

    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)

    to_encode.update(
        exp=expire,
        iat=now,
        jti=str(uuid.uuid4()),
    )
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = config.public_key_path.read_text(),
    algorithm: str = config.algorithm
):
    decoded = jwt.decode(
        token, 
        public_key, 
        algorithms=[algorithm]
    )
    return decoded


def hash_password(
    password: str,
) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(
    password: str,
    hashed_password: bytes
) -> bool:
    return bcrypt.checkpw(
        password.encode(),
        hashed_password=hashed_password
    )