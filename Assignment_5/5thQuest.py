import random

# approximate pi using random points
n_points = int(input("How many random points do you want to generate? "))

inside_circle = 0

for i in range(n_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside_circle = inside_circle + 1

pi = 4 * inside_circle / n_points
print("The approximation of pi is:", pi)
