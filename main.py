import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap
import config
from src.login import Login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(''))
    splash.show()
    app.processEvents()
    window = Login()
    splash.finish(window)
    window.show()
    sys.exit(app.exec_())
