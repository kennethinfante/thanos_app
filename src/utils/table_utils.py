def apply_column_widths(table_view, model):
    """
    Apply column widths from a model to a table view

    Args:
        table_view: The QTableView to apply widths to
        model: The model with a get_column_widths method
    """
    if hasattr(model, 'get_column_widths'):
        column_widths = model.get_column_widths()
        for column, width in column_widths.items():
            table_view.setColumnWidth(column, width)