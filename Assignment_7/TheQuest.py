


class Car:
    
    
    def __init__(self, registration_number="", maximum_speed=0, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def input_registration_number(self):
        self.registration_number = input("Enter the registration number: ")
    
    def input_maximum_speed(self):
        self.maximum_speed = int(input("Enter the maximum speed: "))
        
    def default_current_speed(self):
        self.current_speed = 0
        
    def default_travelled_distance(self):
        self.travelled_distance = 0

    def display_car_info(self):
        print(f"Car Registration Info: {self.registration_number}, Max Speed: {self.maximum_speed}")
        
    def accelerate(self, speed_increase):
        self.current_speed = self.current_speed + speed_increase
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
        
    def accelerate_print_current_speed(self): 
        print(f"Current Speed: {self.current_speed}")

car1 = Car()
car1.input_registration_number()
car1.input_maximum_speed()
car1.default_current_speed()
car1.default_travelled_distance()
car1.display_car_info()

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
car1.accelerate_print_current_speed()


# emergency break
car1.accelerate(-200)
car1.accelerate_print_current_speed()