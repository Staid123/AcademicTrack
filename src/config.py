from pathlib import Path
from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent
load_dotenv()


class PostgresDatabaseSettings(BaseModel):
    HOST = os.environ.get("DB_HOST")
    PORT = os.environ.get("DB_PORT")
    NAME = os.environ.get("DB_NAME")
    USER = os.environ.get("DB_USER")
    PASS = os.environ.get("DB_PASS")


class PostgresTestDatabaseSettings(BaseModel):
    HOST_TEST = os.environ.get("DB_HOST_TEST")
    PORT_TEST = os.environ.get("DB_PORT_TEST")
    NAME_TEST = os.environ.get("DB_NAME_TEST")
    USER_TEST = os.environ.get("DB_USER_TEST")
    PASS_TEST = os.environ.get("DB_PASS_TEST")


class GoogleSettings(BaseModel):
    SECRET_AUTH = os.environ.get("SECRET_AUTH")
    SMTP_USER = os.environ.get("SMTP_USER")
    SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: PostgresDatabaseSettings = PostgresDatabaseSettings()
    db_test: PostgresTestDatabaseSettings = PostgresTestDatabaseSettings()
    google: GoogleSettings = GoogleSettings()
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()