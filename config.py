import os

class ProductionConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    # Add any other configuration variables here

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    DEBUG = True