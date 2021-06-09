
class Config(object):
    DEBUG = False
    TESTING = False

    db_username = 'be8d953f0b3211'
    db_password = '0ab47492'
    db_host = 'us-cdbr-east-04.cleardb.com'
    db_db = 'heroku_49586dd45308328'

    SQLALCHEMY_DATABASE_URI = f'mysql://{db_username}:{db_password}@{db_host}/{db_db}'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


