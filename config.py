import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "env_secret_key")
