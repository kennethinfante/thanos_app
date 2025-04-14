import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap

import config
from src.main_window import AppMainWindow
from src.database_manager import DatabaseManager

def init_db():
    """Initialize the database schema"""
    db_manager = DatabaseManager()

    # Create all tables
    db_manager.Base.metadata.create_all(db_manager.engine)

    print("Database schema created successfully")

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(''))
    splash.show()
    app.processEvents()
    main_window = AppMainWindow()
    splash.finish(main_window)
    main_window.show()
    sys.exit(app.exec_())
