import os


class BaseConfig:
    """Default configuration. Details from this configuration
    class are shared across all environments  """
    DEBUG = False
    TESTING = False
    SECRET = os.getenv('SECRET')
    DATABASE_URI = 'postgres://postgres:psql@localhost:5432/ireporter'


class DevelopmentConfig(BaseConfig):
    """Development configuraion. Loads development configuration data
    when the app is in the development environment"""
    DEBUG = True
    TESTING = False
    ENV = "Development"
    DATABASE_URI = 'postgres://postgres:psql@localhost:5432/ireporter'


class TestingConfig(BaseConfig):
    """Testing configuraion. Loads Test configuration data
    when the app is in the Test environment"""
    DEBUG = True
    TESTING = True
    ENV = "Testing"
    DATABASE_URI = 'postgres://postgres:psql@localhost:5432/test_ireporter'


class ProductionConfig(BaseConfig):
    """Production configuraion. Loads Production configuration data
    when the app is in the Production environment"""
    DEBUG = False
    TESTING = False
    ENV = "Production"
    DATABASE_URI = 'postgres://fpqprtiphlrxzl:f5f606addb1955098f039503a7c325f446ab24130e1129ce38e7134265981166@ec2-54-227-246-152.compute-1.amazonaws.com:5432/df82gdm7bihppe'


app_config = {
    "Development": DevelopmentConfig,
    "Testing": TestingConfig,
    "Production": ProductionConfig
}
