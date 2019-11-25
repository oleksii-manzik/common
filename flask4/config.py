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
    config_options = {'TEST': TestConfig, 'PROD': ProdConfig}
    return config_options.get(env, Config)
