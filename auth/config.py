from pydantic_settings import BaseSettings, SettingsConfigDict

class AuthConf(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    EXP_TIME: int

    model_config = SettingsConfigDict(env_file='auth/.conf_auth')

auth_config = AuthConf()
