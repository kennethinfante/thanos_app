import sys
from PyQt5.QtWidgets import QApplication
from accounting_app import AccountingApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AccountingApp()
    sys.exit(app.exec_())