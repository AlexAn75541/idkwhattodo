class Person:
	def __init__(self, name, height):
		self.name = name
		self.height = height


class Room:
	def __init__(self, room_number, capacity):
		self.room_number = room_number
		self.capacity = capacity

	def add_person(self, person):
		if self.capacity > 0:
			self.capacity -= 1
			print(f"{person.name} has entered the room.")
		else:
			print("The room is full. Cannot add more people.")

	def is_empty(self):
		return self.capacity == 0

	def print_info(self):
		print(f"Room {self.room_number} has a capacity of {self.capacity}.")

	def tallest_person(self, people):
		tallest = max(people, key=lambda p: p.height)
		print(
			f"The tallest person in the room is {tallest.name} with a height of {tallest.height} cm."
		)

	def remove_tallest_person(self, people):
		tallest = max(people, key=lambda p: p.height)
		people.remove(tallest)
		print(f"{tallest.name} has been removed from the room.")
