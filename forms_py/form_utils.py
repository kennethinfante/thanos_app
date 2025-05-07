def apply_macos_button_style(button):
    button_style = """
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #c0c0c0;
                border-radius: 4px;
                padding: 4px 15px;
                color: #000000;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """

    button.setStyleSheet(button_style)

def apply_macos_table_style(table_view):
    table_style = """
        QTableView {
            border: 1px solid #d0d0d0;
            gridline-color: #f0f0f0;
            selection-background-color: #b2d7ff;
            selection-color: #000000;
            alternate-background-color: #f9f9f9;
            background-color: #ffffff;
        }
        QHeaderView::section {
            background-color: #f0f0f0;
            padding: 4px;
            border: 1px solid #d0d0d0;
            font-weight: bold;
        }
    """

    table_view.setStyleSheet(table_style)

def apply_macos_line_edit_style(line_edit):
    line_edit_style = """
        QLineEdit {
            border: 1px solid #c0c0c0;
            border-radius: 4px;
            padding: 2px 4px;
            background-color: #ffffff;
        }
        QLineEdit:focus {
            border: 1px solid #5c9eff;
        }
    """

    line_edit.setStyleSheet(line_edit_style)

# def apply_macos_combobox_style(combobox):
#     combobox_style = """
#         QComboBox {
#             border: 1px solid #c0c0c0;
#             border-radius: 4px;
#             padding: 2px 18px 2px 4px;
#             background-color: #ffffff;
#             min-height: 25px;
#         }
#         QComboBox:focus {
#             border: 1px solid #5c9eff;
#         }
#         QComboBox::drop-down {
#             subcontrol-origin: padding;
#             subcontrol-position: top right;
#             width: 20px;
#             border-left-width: 0px;
#             border-top-right-radius: 4px;
#             border-bottom-right-radius: 4px;
#         }
#         QComboBox::down-arrow {
#             image: url(:/icons/dropdown_arrow.png);
#             width: 12px;
#             height: 12px;
#         }
#     """
#     combobox.setStyleSheet(combobox_style)
#
# def apply_macos_dateedit_style(dateedit):
#     dateedit_style = """
#         QDateEdit {
#             border: 1px solid #c0c0c0;
#             border-radius: 4px;
#             padding: 2px 4px;
#             background-color: #ffffff;
#             min-height: 25px;
#         }
#         QDateEdit:focus {
#             border: 1px solid #5c9eff;
#         }
#         QDateEdit::drop-down {
#             subcontrol-origin: padding;
#             subcontrol-position: top right;
#             width: 20px;
#             border-left-width: 0px;
#             border-top-right-radius: 4px;
#             border-bottom-right-radius: 4px;
#         }
#         QDateEdit::down-arrow {
#             image: url(:/icons/calendar_icon.png);
#             width: 12px;
#             height: 12px;
#         }
#     """
#     dateedit.setStyleSheet(dateedit_style)


def apply_macos_combobox_style(combobox):
    combobox_style = """
        QComboBox {
            border: 1px solid #c0c0c0;
            border-radius: 4px;
            padding: 2px 18px 2px 4px;
            background-color: #ffffff;
            min-height: 25px;
        }
        QComboBox:focus {
            border: 1px solid #5c9eff;
        }
    """
    combobox.setStyleSheet(combobox_style)

def apply_macos_dateedit_style(dateedit):
    dateedit_style = """
        QDateEdit {
            border: 1px solid #c0c0c0;
            border-radius: 4px;
            padding: 2px 4px;
            background-color: #ffffff;
            min-height: 25px;
        }
        QDateEdit:focus {
            border: 1px solid #5c9eff;
        }
    """
    dateedit.setStyleSheet(dateedit_style)