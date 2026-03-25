import random


class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor = self.current_floor + 1
            print(f"Elevator at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor = self.current_floor - 1
            print(f"Elevator at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Floor {target_floor} is out of range")
            return

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()


class Building:

    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for _ in range(number_of_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        index = elevator_number - 1
        if index < 0 or index >= len(self.elevators):  # what even is this
            print(f"No elevator {elevator_number}")
            return

        print(f"Running elevator {elevator_number} to floor {destination_floor}")
        self.elevators[index].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("FIRE ALARM!!! everyone please f**king go to bottom floor")
        for elevator_number, elevator in enumerate(self.elevators, start=1):
            print(f"Elevator {elevator_number} returning to bottom")
            elevator.go_to_floor(self.bottom_floor)


class Car:

    def __init__(self, registration_number="", maximum_speed=0, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, drive_hours):
        self.travelled_distance = self.travelled_distance + (self.current_speed * drive_hours)


class Race:

    def __init__(self, name, distance_in_km, car_list):
        self.name = name
        self.distance_in_km = distance_in_km
        self.cars = car_list

    def hour_passes(self):
        for one_car in self.cars:
            speed_change = random.randint(-10, 15)
            one_car.accelerate(speed_change)
            one_car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Registration':<15}{'Max Speed':<12}{'Current Speed':<15}{'Distance':<12}") # Im tired of ts formats stuff
        for one_car in self.cars:
            print(f"{one_car.registration_number:<15}{one_car.maximum_speed:<12}{one_car.current_speed:<15}{one_car.travelled_distance:<12.1f}") # and ts too

    def race_finished(self):
        for one_car in self.cars:
            if one_car.travelled_distance >= self.distance_in_km:
                return True
        return False


#fr car + building + elevator really likes a Tokyo Drift refrence lol

# 1st, elevator goes up and down
print("\n 1st ")

h = Elevator(1, 10)
h.go_to_floor(5)
h.go_to_floor(1)


# 2nd, building with many elevators
print("\n 2nd ")

building = Building(1, 10, 3)
building.run_elevator(1, 7)
building.run_elevator(2, 3)
building.run_elevator(3, 10)
building.run_elevator(2, 1)


# 3rd, da fire
print("\n 3rd ")

building.fire_alarm()


# 4th, da race
print("\n  4th ") # 

cars = []
for i in range(1, 11):
    reg = "ABC-" + str(i)
    max_spd = random.randint(150, 200)
    c = Car(registration_number=reg, maximum_speed=max_spd)
    cars.append(c)

race = Race("Grand Demolition Derby", 8000, cars)
hours = 0


# def not my OG code and neither some of the code blocks in ts
while not race.race_finished():
    hours = hours + 1
    race.hour_passes()

    if hours % 10 == 0:
        print(f"\nafter {hours} hours:")
        race.print_status()

print(f"\nrace finished in {hours} hours")
race.print_status()


# ngl i hate For and While loops, always making me insane and giving up