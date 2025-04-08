import copy
class Invoice(object):
    def __init__(self, invoice_id=None, date=None, employee=None, customer=None,
                 serial_number=None, accessories=None, above_installation=None, products=[], employees_shares=[]):
        self.invoice_id = invoice_id
        self.date = date
        self.employee = employee
        self.customer = customer
        self.serial_number = serial_number
        self.products = copy.deepcopy(products)
        self.employees_shares = copy.deepcopy(employees_shares)
        self.accessories = accessories
        self.above_installation = above_installation

    def get_employees_shares(self):
        return self.employees_shares

    def set_employees_shares(self, employees_shares:list):
        self.employees_shares = copy.deepcopy(employees_shares)

    def get_products(self):
        return self.products

    def set_products(self, products: list):
        self.products = copy.deepcopy(self.products)

    def append_product(self, product):
        self.products.append(product)

    def append_employee_share(self, employee_share: dict):
        self.employees_shares.append(employee_share)

    def get_invoice_id(self):
        return self.invoice_id

    def set_invoice_id(self, invoice_id):
        self.invoice_id = invoice_id

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_employee(self):
        return self.employee

    def set_employee(self, employee):
        self.employee = employee

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def get_serial_number(self):
        return self.serial_number

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number

    def get_accessories(self):
        return self.accessories

    def set_accessories(self, accessories):
        self.accessories = accessories

    def get_above_installation(self):
        return self.above_installation

    def set_above_installation(self, above_installation):
        self.above_installation = above_installation

    def __str__(self):
        return self.serial_number

    def serialize_invoice(self, fields='All', exclude=None):
        keys_to_be_excluded = list(set(self.__dict__.keys()) - set(fields)) if fields != 'All' else []
        keys_to_be_excluded.extend(exclude) if exclude else None
        for key in keys_to_be_excluded:
            del self.__dict__[key]
        return self.__dict__
