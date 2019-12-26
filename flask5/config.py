import os


class Config:
    NAME = 'default'
    DEBUG = True
    PG_USER = 'test_cursor'
    PG_PASSWORD = "111"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "test_orm_cursor"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@" \
                              f"{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    NAME = 'test'
    DEBUG = True


class ProdConfig(Config):
    NAME = 'prod'


def run_config():
    env = os.environ.get('ENV')
    if env == 'TEST':
        return TestConfig
    elif env == 'PROD':
        return ProdConfig
    else:
        return Config
