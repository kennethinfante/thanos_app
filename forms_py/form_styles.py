import sys
import platform

# Flag to determine if we're running on macOS
IS_MACOS = platform.system() == 'Darwin'

def apply_main_window_style(window):
    """Apply macOS-like styling to the main window, only if running on macOS"""
    if IS_MACOS:
        window_style = """
            QMainWindow {
                background-color: #F5F5F5;
            }
            QMenuBar {
                background-color: #F5F5F5;
                border-bottom: 1px solid #D0D0D0;
            }
            QMenuBar::item {
                background: transparent;
                padding: 4px 10px;
            }
            QMenuBar::item:selected {
                background: #E0E0E0;
                border-radius: 4px;
            }
            QMenu {
                background-color: #FFFFFF;
                border: 1px solid #C0C0C0;
                border-radius: 4px;
                padding: 4px 0px;
            }
            QMenu::item {
                padding: 4px 20px;
            }
            QMenu::item:selected {
                background-color: #5C9EFF;
                color: white;
            }
            QStackedWidget {
                background-color: white;
                border: none;
            }
        """
    else:
        # Default style for non-macOS platforms
        window_style = """
            QMainWindow {
                background-color: #F0F0F0;
            }
            QStackedWidget {
                background-color: white;
                border: 1px solid #C0C0C0;
            }
        """

    window.setStyleSheet(window_style)

def apply_sidebar_style(sidebar):
    """Apply macOS-like styling to the sidebar, only if running on macOS"""
    if IS_MACOS:
        sidebar_style = """
            QWidget#SideBar {
                background-color: #F0F0F0;
                border-right: 1px solid #D0D0D0;
                margin: 0;
            }
            QPushButton { 
                background-color: transparent;
                color: #404040;
                border: none;
                text-align: left;
                text-decoration: none;
                padding: 8px 12px;
                font-size: 13px;
                border-radius: 4px;
                margin: 2px 8px;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.05);
            }
            QPushButton:pressed {
                background-color: rgba(0, 0, 0, 0.1);
            }
            QPushButton:checked {
                background-color: #E0E0E0;
                color: #000000;
            }
        """
    else:
        # Default style for non-macOS platforms
        sidebar_style = """
            QWidget#SideBar {
                background-color: #E8E8E8;
                border-right: 1px solid #C0C0C0;
            }
            QPushButton { 
                background-color: transparent;
                color: #303030;
                border: none;
                text-align: left;
                padding: 8px 12px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #D0D0D0;
            }
            QPushButton:pressed {
                background-color: #B0B0B0;
            }
            QPushButton:checked {
                background-color: #C0C0C0;
                font-weight: bold;
            }
        """

    sidebar.setStyleSheet(sidebar_style)

def apply_line_edit_style(line_edit):
    """Apply macOS-like styling to line edits, only if running on macOS"""
    if IS_MACOS:
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
    else:
        # Default style for non-macOS platforms
        line_edit_style = """
            QLineEdit {
                border: 1px solid #a0a0a0;
                padding: 2px 4px;
                background-color: #ffffff;
            }
            QLineEdit:focus {
                border: 1px solid #0078d7;
            }
        """

    line_edit.setStyleSheet(line_edit_style)

def apply_button_style(button):
    """Apply macOS-like styling to buttons, only if running on macOS"""
    if IS_MACOS:
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
    else:
        # Default style for non-macOS platforms
        button_style = """
            QPushButton {
                background-color: #e1e1e1;
                border: 1px solid #adadad;
                padding: 4px 15px;
                color: #000000;
            }
            QPushButton:hover {
                background-color: #e5f1fb;
                border: 1px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #cce4f7;
                border: 1px solid #0078d7;
            }
        """

    button.setStyleSheet(button_style)

def apply_table_style(table_view):
    """Apply macOS-like styling to table views, only if running on macOS"""
    if IS_MACOS:
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
    else:
        # Default style for non-macOS platforms
        table_style = """
            QTableView {
                border: 1px solid #c0c0c0;
                gridline-color: #e0e0e0;
                selection-background-color: #0078d7;
                selection-color: #ffffff;
                alternate-background-color: #f5f5f5;
                background-color: #ffffff;
            }
            QHeaderView::section {
                background-color: #e1e1e1;
                padding: 4px;
                border: 1px solid #c0c0c0;
                font-weight: bold;
            }
        """

    table_view.setStyleSheet(table_style)

def apply_combobox_style(combobox):
    """Apply macOS-like styling to comboboxes, only if running on macOS"""
    if IS_MACOS:
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
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 0px;
                border-top-right-radius: 4px;
                border-bottom-right-radius: 4px;
            }
        """
    else:
        # Default style for non-macOS platforms
        combobox_style = """
            QComboBox {
                border: 1px solid #a0a0a0;
                padding: 2px 18px 2px 4px;
                background-color: #ffffff;
                min-height: 25px;
            }
            QComboBox:focus {
                border: 1px solid #0078d7;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 0px;
            }
        """

    combobox.setStyleSheet(combobox_style)

def apply_dateedit_style(dateedit):
    """Apply macOS-like styling to date edits, only if running on macOS"""
    if IS_MACOS:
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
            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 0px;
                border-top-right-radius: 4px;
                border-bottom-right-radius: 4px;
            }
        """
    else:
        # Default style for non-macOS platforms
        dateedit_style = """
            QDateEdit {
                border: 1px solid #a0a0a0;
                padding: 2px 4px;
                background-color: #ffffff;
                min-height: 25px;
            }
            QDateEdit:focus {
                border: 1px solid #0078d7;
            }
        """

    dateedit.setStyleSheet(dateedit_style)

# the date dropdowns are missing
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

