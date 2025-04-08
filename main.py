import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap
import config
from src.main_window import AppMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(''))
    splash.show()
    app.processEvents()
    main_window = AppMainWindow()
    splash.finish(main_window)
    main_window.show()
    sys.exit(app.exec_())
