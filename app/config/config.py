class BaseConfig:
    """Base configuration."""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://bassilekin:gaston2006@db:5432/hospital_flask'

class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://bassilekin:gaston2006@db:5432/hospital_flask'

class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://bassilekin:gaston2006@db:5432/hospital_flask'


def get_config_by_name(config_name):
    """ Get config by name """
    if config_name == 'development':
        return DevelopmentConfig()
    elif config_name == 'production':
        return ProductionConfig()
    elif config_name == 'testing':
        return TestingConfig()
    else:
        return DevelopmentConfig()
