import pygame
import sys
from pygame.locals import *
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Cube")

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define cube vertices
vertices = [
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, -1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

# Define edges
edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]

# Function to project 3D point to 2D
def project(point):
    x = point[0] * width / (point[2] + 5) + width / 2
    y = point[1] * height / (point[2] + 5) + height / 2
    
    # Add a small epsilon value to avoid division by zero
    epsilon = 1e-6
    z = 1 / ((cosx * cosy - 1) + epsilon)
    
    return int(x), int(y)

# Main loop
clock = pygame.time.Clock()
angle_x = 0
angle_y = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    screen.fill((0, 0, 0))

    # Rotate vertices
    rotated_vertices = []
    for vertex in vertices:
        cosx = math.cos(angle_x)
        sinx = math.sin(angle_x)
        cosy = math.cos(angle_y)
        siny = math.sin(angle_y)

        rx1 = vertex[0] * (cosy) - vertex[2] * (siny)
        ry1 = vertex[1] * (cosx) + vertex[2] * (sinx) - vertex[0] * (siny)
        rz1 = vertex[1] * (sinx) + vertex[2] * (cosx)

        rx2 = rx1 * (cosx) - ry1 * (sinx)
        ry2 = rx1 * (sinx) + ry1 * (cosx)

        z = 1 / ((cosx * cosy - 1) + epsilon)
        
        vx, vy = project([rx2, ry2, z])

        rotated_vertices.append([vx, vy])

    # Draw edges
    for edge in edges:
        pygame.draw.line(screen, white, (rotated_vertices[edge[0]][0], rotated_vertices[edge[0]][1]),
                         (rotated_vertices[edge[1]][0], rotated_vertices[edge[1]][1]), 2)

    # Update angles
    angle_x += 0.01
    angle_y += 0.01

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
