from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry
from src.logger import Logger
import config


class DatabaseManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, is_testing=False):
        if self._initialized:
            return

        self.DATABASE_FILENAME = f'{config.PROJECT_ROOT_PATH}/assets/database/{config.DB_NAME}.db'
        self.TESTING_DATABASE_FILENAME = f'{config.PROJECT_ROOT_PATH}/assets/database/{config.DB_NAME}_testing.db'
        self.is_testing = is_testing
        self.current_database = self.DATABASE_FILENAME if not is_testing else self.TESTING_DATABASE_FILENAME
        self.logger = Logger()

        # Create registry for ORM models
        self.registry = registry()
        self.Base = self.registry.generate_base()

        self.Session = None
        self.engine = None
        self.connectToDatabase()
        self._initialized = True

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