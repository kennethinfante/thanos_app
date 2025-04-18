from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

from src.logger import Logger
import config

class DatabaseManager:
    _instance = None

    def __new__(cls, is_testing=False):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance._initialize(is_testing)
        return cls._instance

    def _initialize(self, is_testing=False):
        """Initialize the database connection"""
        self.DATABASE_FILENAME = f'{config.PROJECT_ROOT_PATH}/database/{config.DB_NAME}.db'
        self.TESTING_DATABASE_FILENAME = f'{config.PROJECT_ROOT_PATH}/database/{config.DB_NAME}_testing.db'
        self.is_testing = is_testing
        self.current_database = self.DATABASE_FILENAME if not is_testing else self.TESTING_DATABASE_FILENAME
        self.logger = Logger()

        # Create the database engine
        self.engine = create_engine(f'sqlite:///{self.current_database}')

        # Create a base class for declarative models
        self.Base = declarative_base()

        # Create a scoped session factory
        self.session_factory = scoped_session(sessionmaker(bind=self.engine))

    @property
    def Session(self):
        """Get the current session factory"""
        return self.session_factory

    def create_session(self):
        """Create a new session"""
        return self.session_factory()

    def remove_session(self):
        """Remove the current session"""
        self.session_factory.remove()
