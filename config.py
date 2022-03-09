import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sharon:12345678@localhost/pitchapp'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SENDER_EMAIL = 'sharon.moringaprojects@gmail.com'
    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ruzplugpqreskf:f4c3d3345a72784dc0eea6ecdfa509449c388c7a01b69650dfa9db0ec991a000@ec2-52-44-209-165.compute-1.amazonaws.com:5432/dm0ae61uqj0b5'

class TestConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sharon:12345678@localhost/pitchapp_test'
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sharon:12345678@localhost/pitchapp'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}