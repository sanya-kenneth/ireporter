class BaseConfig:
    """Default configuration. Details from this configuration
    class are shared across all environments  """
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = 'qwertyuiopasdfghjklsdfghjklzxcvbnmdfgh'
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


app_config = {
            "Development": DevelopmentConfig,
            "Testing": TestingConfig,
            "Production": ProductionConfig
            }
