class Watch:
    def __init__(self, brand, model, price, uid, isConsigned=None, serialNumber=None, full_kit=None, year=None, sold=None):
        self.brand = brand
        self.model = model
        self.price = price
        self.uid = uid
        self.isConsigned = None
        self.year = None
        self.full_kit = None
        self.serial_number = None
        self.sold = False

    # Setter methods
    def set_consignment(self, isConsigned):
        self.isConsigned = isConsigned

    def set_year(self, year):
        self.year = year

    def set_full_kit(self, full_kit):
        self.full_kit = full_kit

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number

    def set_sold(self, sold):
        self.sold = sold

    # Getter methods
    def get_isConsigned(self):
        return self.isConsigned

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    def get_uid(self):
        return self.uid

    def get_year(self):
        return self.year

    def get_full_kit(self):
        return self.full_kit

    def get_serial_number(self):
        return self.serial_number

    def __str__(self):
        return (f"Watch(Brand: {self.brand}, Model: {self.model}, Price: {self.price}, UID: {self.uid}, "
                f"Year: {self.year}, Full Kit: {self.full_kit}, Serial Number: {self.serial_number} "
                f"Consigned: {self.isConsigned})")

    def isSold(self):
        return self.sold


