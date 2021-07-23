import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

APP_PATH = os.path.dirname(os.path.abspath(__file__)) + '/app'
print(APP_PATH)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = "postgresql://uac9qz1hvldmbx1ossw0:anSXTgU0RKebhLiIV80k@bajmdptyphyfvo8rsr4e-postgresql.services.clever-cloud.com:5432/bajmdptyphyfvo8rsr4e"
    SQLALCHEMY_DATABASE_URI = "postgresql://knlvynjefdxtkz:9f280a0b61c7c2220427e9c8cc60f714ec2acecb0f9797566f2f1e998406213b@ec2-54-236-137-173.compute-1.amazonaws.com:5432/dajm73sv16g1v2"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    SECRET_KEY = 'dev'


class ProductionConfig(Config):
    ENV = 'production'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class HerokuConfig(ProductionConfig):

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)



config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
}
