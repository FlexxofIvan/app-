from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    lite: bool = True


    @property
    def db_url(self):
        if self.lite:
            return f"sqlite+aiosqlite:///./base/test.db"
            # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        else:
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


    model_config = SettingsConfigDict(env_file="base/.env_bd")


settings = Settings(lite=True)