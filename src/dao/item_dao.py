from src.dao.data_access_object import DataAccessObject
from src.do.item import Item


class ItemDao(DataAccessObject):
    def __init__(self, is_testing=False):
        super().__init__(table_name='items', is_testing=is_testing)

    def get_all_items(self, filters=None):
        """Get all invoices with related data"""
        try:
            query = self.session.query(Item)

            # Apply invoice filters
            if filters:
                for filter_condition in filters:
                    query = query.filter(filter_condition)
            return query.all()
        except Exception as e:
            self.logger.error(f"Error getting all items: {str(e)}")
            return []

    def get_item_by_id(self, item_id):
        """Get an item by ID"""
        try:
            return self.session.query(Item).filter(Item.id == item_id).first()
        except Exception as e:
            self.logger.error(f"Error getting item by ID: {str(e)}")
            return None

    def create_item(self, item_data):
        """Create a new item"""
        try:
            item = Item(**item_data)
            self.session.add(item)
            self.session.commit()
            return item
        except Exception as e:
            self.session.rollback()
            self.logger.error(f"Error creating item: {str(e)}")
            return None

    def update_item(self, item_id, item_data):
        """Update an existing item"""
        try:
            item = self.get_item_by_id(item_id)
            if not item:
                return None

            for key, value in item_data.items():
                setattr(item, key, value)

            self.session.commit()
            return item
        except Exception as e:
            self.session.rollback()
            self.logger.error(f"Error updating item: {str(e)}")
            return None

    def delete_item(self, item_id):
        """Delete an item"""
        try:
            item = self.get_item_by_id(item_id)
            if not item:
                return False

            self.session.delete(item)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            self.logger.error(f"Error deleting item: {str(e)}")
            return False
