



class creditcard:
    @creditcard1
    def __init__(self, number="", CVV=0, expiry_date=""):
        self.number = number
        self.CVV = CVV
        self.expiry_date = expiry_date



class User:
    @User1
    def __init__(self, name):
        self.name = "An"
        self.credit_card = []
        
    def add_card(self, card):
        self.credit_card.append(card)
        
    def print_name(self):
        print(f"User Name: {self.name}")
        
    def print_last_four_digits(self):
        for card in self.credit_card:
            print(f"Last four digits of card: {card.number[-4:]}")
        
card1 = creditcard(number=input("Enter credit 1st card number: "))
card2 = creditcard(number=input("Enter credit 2nd card number: "))
card3 = creditcard(number=input("Enter credit 3rd card number: "))


user = User()
user.print_name()
user.add_card(card1)
user.add_card(card2)
user.add_card(card3)

user.print_last_four_digits()