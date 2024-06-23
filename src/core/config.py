from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent


class PostgresDatabaseSettings(BaseModel):
    host: str
    port: int
    name: str
    user: str
    password: str
    url: str

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class PostgresTestDatabaseSettings(BaseModel):
    host: str
    port: int
    name: str
    user: str
    password: str
    url: str


class GoogleSettings(BaseModel):
    secret_auth: str
    smtp_user: str
    smtp_password: str


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__"
    )
    run: RunConfig = RunConfig()
    auth_jwt: AuthJWT = AuthJWT()
    db: PostgresDatabaseSettings
    db_test: PostgresTestDatabaseSettings
    google: GoogleSettings


settings = Settings()