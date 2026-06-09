class Property:
    def __init__(self, prop_id, address, price, sqm):
        self.prop_id = prop_id
        self.address = address
        self.price = price
        self.sqm = sqm

    def display_listing(self):
        print(f"ID: {self.prop_id} | {self.address} | {self.price}B VND | {self.sqm} sqm")