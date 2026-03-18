

import random


class Car:
    
    
    def __init__(self, registration_number="", maximum_speed=0, current_speed=0, travelled_distance=0, hours=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
        self.hours = hours

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
        
    def add_travelled_distance(self, distance: int) -> None: # I fucking have no idea wtf is this 
        self.travelled_distance += max(distance, 0)

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + (self.current_speed * hours)

        
    

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

# that one car.drive(1.5) lol
car1.add_travelled_distance(2000)
car1.accelerate(60)
car1.drive(1.5)
print(f"Travelled Distance: {car1.travelled_distance}")

# I hate this
cars = []
for i in range(1, 11):
    reg = "ABC-" + str(i)
    max_spd = random.randint(150, 200)
    c = Car(registration_number=reg, maximum_speed=max_spd)
    c.default_current_speed()
    c.default_travelled_distance()
    cars.append(c)

race_hours = 0
race_on = True

# I hate this even more
while race_on:
    race_hours = race_hours + 1
    
    
    for thecar in cars:
        speed_change = random.randint(-10, 15)
        thecar.accelerate(speed_change)
        thecar.drive(1)
        if thecar.travelled_distance >= 10000:
            race_on = False


print("Race Finished")
print("Hours:", race_hours)


# I hate formats
print(f"{'Registration':<15}{'Max Speed':<12}{'Current Speed':<15}{'Distance':<12}")

for thecar in cars:
    print(f"{thecar.registration_number:<15}{thecar.maximum_speed:<12}{thecar.current_speed:<15}{thecar.travelled_distance:<12}")

