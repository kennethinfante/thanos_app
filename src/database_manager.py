from src.logger import Logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config


class DatabaseManager(object):
    class __DatabaseManager:
        def __init__(self):
            self.val = None
            self.current_database = f'{config.PROJECT_ROOT_PATH}/assets/database/{config.DB_NAME}.db'
            self.logger = Logger()
            self.Base = declarative_base()
            self.Session = None
            self.engine = None
            self.connectToDatabase()

        def __str__(self):
            return "{0!r} {1}".format(self, self.val)

        def connectToDatabase(self):
            try:
                # Create SQLAlchemy engine
                self.engine = create_engine(f'sqlite:///{self.current_database}')
                self.val = self.engine

                # Create session factory
                self.Session = sessionmaker(bind=self.engine)

                # Test connection
                connection = self.engine.connect()
                connection.close()

                self.logger.debug("database opened")
            except Exception as e:
                self.logger.error(f"Can not open database with file name: {self.current_database}. Error: {str(e)}")
                return

    instance = None

    def __new__(cls, is_testing=False):
        if not DatabaseManager.instance:
            DatabaseManager.instance = DatabaseManager.__DatabaseManager()
        return DatabaseManager.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr(self, item):
        return setattr(self.instance, item)