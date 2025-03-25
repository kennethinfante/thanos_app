from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QPushButton

class Invoice(QWidget):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Invoice table
        self.invoice_table = QTableWidget()
        layout.addWidget(self.invoice_table)

        # Add invoice button
        add_button = QPushButton("Add Invoice")
        add_button.clicked.connect(self.add_invoice)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_invoice(self):
        # Implement add invoice functionality
        pass

    # Add other invoice-related methods here