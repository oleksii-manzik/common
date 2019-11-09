import os


class Config:
    NAME = 'default'
    DEBUG = False


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
