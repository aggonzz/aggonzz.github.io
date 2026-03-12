"""
Alexandra Gonzalez
Project 3 Improved Nighttime Landscape
Displays a more populated nighttime landscape with a moon, stars, hills, and trees.
Improvements were made to enhance the scene:
- Extra trees for forest feel and stars
- Extra hill
- Shooting star
- Refactored helper functions for reusability
- Organized code for easier maintenance
"""

import turtle
import math


# -- Basic Shape Functions --

def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_square(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_rectangle(t, width, height, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


# ---Figures --

def draw_moon(t):
    jump_to(t, 200, 150)
    draw_circle(t, 60, "white")


def draw_stars(t, positions):
    for x, y in positions:
        jump_to(t, x, y)
        draw_square(t, 8, "white")


def draw_hills(t):
    jump_to(t, -300, -50)
    draw_triangle(t, 300, "purple")
    jump_to(t, 0, -50)
    draw_triangle(t, 300, "purple")


def draw_tree(t, x, y):
    jump_to(t, x, y)
    draw_rectangle(t, 30, 60, "brown")
    jump_to(t, x + 15, y)
    draw_circle(t, 30, "darkgreen")


# -- new function for shooting star --
def draw_shooting_star(t, x, y):
    """Draws a small triangle shooting star at (x, y)"""
    jump_to(t, x, y)
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(3):  # small triangle
        t.forward(15)
        t.left(120)
    t.end_fill()


# -- Enhanced Scene  --

def draw_enhanced_scene(t):
    screen = t.getscreen()
    screen.bgcolor("midnightblue")

    draw_moon(t)

    # -- Stars --
    star_positions = [
        (-200, 180), (-150, 130), (-100, 170),
        (-50, 140), (0, 180), (50, 150),
        (100, 170), (150, 130),
        # Extra stars for enhanced scene
        (-250, 160), (-180, 190), (180, 190), (230, 160),
        (-100, 200), (0, 210), (100, 200)
    ]
    draw_stars(t, star_positions)

    # Extra: shooting star
    draw_shooting_star(t, 100, 220)

    # -- Hills --
    draw_hills(t)
    # Extra hill to make scene more populated
    jump_to(t, -150, -80)
    draw_triangle(t, 250, "purple")

    # -- Trees --
    # Original trees
    draw_tree(t, -100, -200)
    draw_tree(t, 200, -200)
    # Extra trees for enhanced scene
    draw_tree(t, -250, -200)
    draw_tree(t, -150, -200)
    draw_tree(t, -50, -200)
    draw_tree(t, 50, -200)
    draw_tree(t, 100, -200)
    draw_tree(t, 250, -200)


# -- Main Function --

def main():
    t, screen = setup_turtle()
    draw_enhanced_scene(t)  
    screen.mainloop()


if __name__ == "__main__":
    main()
