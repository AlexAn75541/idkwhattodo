from property import Property

class Apartment(Property):
    def __init__(self, prop_id, address, price, sqm, floor_level):
        super().__init__(prop_id, address, price, sqm)
        self.floor_level = floor_level

    def get_actual_area(self):
        return self.sqm * 1.05

    def display_listing(self):
        bonus_area = self.get_actual_area()
        print(f"[APT] ID: {self.prop_id} | Floor {self.floor_level} | {self.address} | {self.price}B VND | Area: {bonus_area:.1f} sqm")


class Villa(Property):
    def __init__(self, prop_id, address, price, sqm, has_pool):
        super().__init__(prop_id, address, price, sqm)
        self.has_pool = has_pool

    def calculate_maintenance(self):
        return self.price * 0.0005

    def display_listing(self):
        fee = self.calculate_maintenance()
        print(f"[VILLA] ID: {self.prop_id} | {self.address} | {self.price}B VND | Pool: {self.has_pool} | Maintenance: {fee:.4f}B VND")

    def add_pool(self):
        self.has_pool = True


class Penthouse(Property):
    def __init__(self, prop_id, address, price, sqm, has_private_elevator):
        super().__init__(prop_id, address, price, sqm)
        self.has_private_elevator = has_private_elevator

    def get_taxed_price(self):
        return self.price * 1.1

    def display_listing(self):
        taxed_price = self.get_taxed_price()
        print(f"[PENTHOUSE] ID: {self.prop_id} | Elevator: {self.has_private_elevator} | Total Price (with Tax): {taxed_price:.2f}B VND | {self.address}")