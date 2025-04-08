import logging

class Logger:
    def __init__(self):
        self.LOGS_FILE_NAME = ""

    def debug(self, message):
        logging.basicConfig(filename=self.LOGS_FILE_NAME, level=logging.DEBUG)
        logging.getLogger("logger").debug(message)
        print("DEBUG: ", message)

    def cirtical(self, message):
        logging.basicConfig(filename=self.LOGS_FILE_NAME, level=logging.CRITICAL)
        logging.getLogger("logger").critical(message)
        print("CRITICAL: ", message)

    def warning(self, message):
        logging.basicConfig(filename=self.LOGS_FILE_NAME, level=logging.WARNING)
        logging.getLogger("logger").warning(message)
        print("WARNING: ", message)

    def error(self, message):
        logging.basicConfig(filename=self.LOGS_FILE_NAME, level=logging.ERROR)
        logging.getLogger("logger").error(message)
        print("ERROR: ", message)
