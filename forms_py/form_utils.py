from PyQt5 import QtCore, QtGui, QtWidgets

main_max_size = (1600, 1000)
main_min_size = (1440, 900)
page_max_size = (1400, 1000)
page_min_size = (1224, 890)
sidebar_min_size = (200, 0)
sidebar_max_size = (200, 1000)

def create_checkbox(parent, text, font_size=12, bold=True, direction=QtCore.Qt.RightToLeft, object_name=None):
    """Create a standardized label with consistent styling

    Args:
        parent: Parent widget
        text: Label text
        font_size: Font size (default: 12)
        bold: Whether font should be bold (default: True)
        direction: Button and text direction (default: QtCore.Qt.RightToLeft)
        object_name: Object name for the label (optional)

    Returns:
        QCheckbox: The created checkbox
    """

    chkbox = QtWidgets.QCheckBox(parent)
    chkbox.setText(text)
    font = QtGui.QFont()
    font.setPointSize(font_size)
    chkbox.setFont(font)

    if bold:
        font.setBold(bold)
    if direction:
        chkbox.setLayoutDirection(direction)
    if object_name:
        chkbox.setObjectName(object_name)

    return chkbox

def create_label(parent, text, font_size=12, bold=True, object_name=None):
    """Create a standardized label with consistent styling

    Args:
        parent: Parent widget
        text: Label text
        font_size: Font size (default: 12)
        bold: Whether font should be bold (default: True)
        object_name: Object name for the label (optional)

    Returns:
        QLabel: The created label
    """
    label = QtWidgets.QLabel(parent)
    font = QtGui.QFont()
    font.setPointSize(font_size)
    font.setBold(bold)
    label.setFont(font)
    label.setText(text)
    if object_name:
        label.setObjectName(object_name)
    return label

def create_button(parent, text, min_size=(120, 40), font_size=12,
                 bold=True, tooltip=None, icon_path=None, object_name=None):
    """Create a standardized button with consistent styling

    Args:
        parent: Parent widget
        text: Button text
        min_size: Minimum size (default: (120, 40))
        font_size: Font size (default: 12)
        bold: Whether font should be bold (default: True)
        tooltip: Tooltip text (optional)
        icon_path: Path to icon (optional)
        object_name: Object name for the button (optional)

    Returns:
        QPushButton: The created button
    """
    button = QtWidgets.QPushButton(parent)
    button.setMinimumSize(QtCore.QSize(*min_size))
    font = QtGui.QFont()
    font.setPointSize(font_size)
    font.setBold(bold)
    button.setFont(font)
    button.setText(text)

    if tooltip:
        button.setToolTip(tooltip)
    if icon_path:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
    if object_name:
        button.setObjectName(object_name)

    return button

def create_line_edit(parent, min_size=(200, 40), font_size=12,
                    bold=False, placeholder=None, object_name=None):
    """Create a standardized line edit with consistent styling

    Args:
        parent: Parent widget
        min_size: Minimum size (default: (200, 40))
        font_size: Font size (default: 12)
        bold: Whether font should be bold (default: False)
        placeholder: Placeholder text (optional)
        object_name: Object name for the line edit (optional)

    Returns:
        QLineEdit: The created line edit
    """
    line_edit = QtWidgets.QLineEdit(parent)
    line_edit.setMinimumSize(QtCore.QSize(*min_size))
    font = QtGui.QFont()
    font.setPointSize(font_size)
    font.setBold(bold)
    line_edit.setFont(font)

    if placeholder:
        line_edit.setPlaceholderText(placeholder)
    if object_name:
        line_edit.setObjectName(object_name)

    return line_edit

def create_date_edit(parent, enabled=True, min_size=(160, 40),
                        font_size=12, bold=True, display_format="yyyy-MM-dd",
                        default_date=None, object_name=None):
    """Create a standardized date edit with consistent styling

    Args:
        parent: Parent widget
        enabled: Whether the date edit is enabled (default: True)
        min_size: Minimum size (default: (160, 40))
        font_size: Font size (default: 12)
        bold: Whether font should be bold (default: True)
        display_format: Date display format (default: "yyyy-MM-dd")
        default_date: Default date (QDate object, optional)
        object_name: Object name for the date edit (optional)

    Returns:
        QDateEdit: The created date edit
    """
    date_edit = QtWidgets.QDateEdit(parent)
    date_edit.setEnabled(enabled)
    date_edit.setMinimumSize(QtCore.QSize(*min_size))
    font = QtGui.QFont()
    font.setPointSize(font_size)
    font.setBold(bold)
    date_edit.setFont(font)
    date_edit.setCalendarPopup(True)
    date_edit.setDisplayFormat(display_format)

    if default_date:
        date_edit.setDate(QtCore.QDate(*default_date))
    if object_name:
        date_edit.setObjectName(object_name)

    return date_edit
