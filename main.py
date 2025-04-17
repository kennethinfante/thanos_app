import sys
import os
import shutil

from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap

import config
from config import PROJECT_ROOT_PATH
from src.main_window import AppMainWindow

def reset_database():
    """Reset the database by replacing it with the backup copy"""
    try:
        # Define paths
        db_path = os.path.join(PROJECT_ROOT_PATH, 'assets', 'database', 'accounting.db')
        backup_path = os.path.join(PROJECT_ROOT_PATH, 'assets', 'database', 'accounting_bk.db')

        # Check if backup exists
        if not os.path.exists(backup_path):
            print(f"Warning: Backup database not found at {backup_path}")
            return False

        # Remove existing database if it exists
        if os.path.exists(db_path):
            os.remove(db_path)
            print(f"Removed existing database: {db_path}")

        # Copy backup to main database location
        shutil.copy2(backup_path, db_path)
        print(f"Database reset successfully: {backup_path} → {db_path}")

        return True
    except Exception as e:
        print(f"Error resetting database: {str(e)}")
        return False

if __name__ == "__main__":
    reset_database()
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(''))
    splash.show()
    app.processEvents()
    main_window = AppMainWindow()
    splash.finish(main_window)
    main_window.show()
    sys.exit(app.exec_())
