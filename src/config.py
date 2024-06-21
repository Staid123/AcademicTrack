from pathlib import Path
from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent
load_dotenv()


class PostgresDatabaseSettings(BaseModel):
    host = os.environ.get("DB_HOST")
    port = os.environ.get("DB_PORT")
    name = os.environ.get("DB_NAME")
    user = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASS")
    url = os.environ.get("DB_URL")


class PostgresTestDatabaseSettings(BaseModel):
    host_test = os.environ.get("DB_HOST_TEST")
    port_test = os.environ.get("DB_PORT_TEST")
    name_test = os.environ.get("DB_NAME_TEST")
    user_test = os.environ.get("DB_USER_TEST")
    password_test = os.environ.get("DB_PASS_TEST")


class GoogleSettings(BaseModel):
    secret_auth = os.environ.get("SECRET_AUTH")
    smtp_user = os.environ.get("SMTP_USER")
    smpt_password = os.environ.get("SMTP_PASSWORD")


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