"""
This program will draw a snake of a user specified number of segments.
Each segment will be a random length, color, and angle.
The snake will also stay within a 400 by 400 unit bounding box.

@author Morgan Lecrone
"""

import turtle
import random


def draw_bounding_box(BOUNDING_BOX):
    """
    This function draws the bounding box that the snake will stay inside.

    BOUNDING_BOX: The maximum distance that the turtle can travel from the origin.

    Preconditions: The turtle is at the origin, facing East.
    Postconditions: The turtle is at the origin, facing East.
    """
    RIGHT_ANGLE = 90
    turtle.up()
    turtle.forward(BOUNDING_BOX)
    turtle.right(RIGHT_ANGLE)
    turtle.down()
    turtle.forward(BOUNDING_BOX)
    turtle.right(RIGHT_ANGLE)
    turtle.forward(BOUNDING_BOX * 2)
    turtle.right(RIGHT_ANGLE)
    turtle.forward(BOUNDING_BOX * 2)
    turtle.right(RIGHT_ANGLE)
    turtle.forward(BOUNDING_BOX * 2)
    turtle.right(RIGHT_ANGLE)
    turtle.forward(BOUNDING_BOX)
    turtle.left(RIGHT_ANGLE)
    turtle.up()
    turtle.back(BOUNDING_BOX)
    turtle.down()


def border_correct(BOUNDING_BOX, MAX_LENGTH):
    """
    This function causes the turtle to turn perpendicular to the edge
    of the bounding box if it gets within 20 units of the edge.

    BOUNDING_BOX: The maximum distance that the turtle can travel from the origin.
    MAX_LENGTH: The maximum length of a segment of the snake.

    Preconditions: The turtle is within the bounding box.
    Postconditions: The turtle is in the same position, or it turns to be perpendicular to the edge of the bounding box.
    """
    (x, y) = turtle.position()
    if x >= BOUNDING_BOX - MAX_LENGTH:
        turtle.setheading(180)
    elif x <= -BOUNDING_BOX + MAX_LENGTH:
        turtle.setheading(0)
    elif y >= BOUNDING_BOX - MAX_LENGTH:
        turtle.setheading(270)
    elif y <= -BOUNDING_BOX + MAX_LENGTH:
        turtle.setheading(90)


def draw_snake_tail(segments, total, BOUNDING_BOX):
    """
    This function draws a snake recursively with random segment length, thickness, and angle.

    Segments: The number of segments left to draw for the snake.
    Total: The total units of length of the snake.
    BOUNDING_BOX: The maximum distance that the turtle can travel from the origin.

    Preconditions: The turtle is in the bounding box.
    Postconditions: The turtle is in the bounding box.
    """
    if segments == 0:
        return total
    MAX_LENGTH = 20
    MIN_THICKNESS = 1
    MAX_THICKNESS = 10
    MAX_ANGLE = 30
    border_correct(BOUNDING_BOX, MAX_LENGTH)
    length = random.randint(0, MAX_LENGTH)
    turtle.pencolor(random.random(), random.random(), random.random())
    turtle.pensize(random.randint(MIN_THICKNESS, MAX_THICKNESS))
    turtle.forward(length)
    turtle.left(random.randint(0, MAX_ANGLE * 2) - MAX_ANGLE)
    return draw_snake_tail(segments - 1, total + length, BOUNDING_BOX)


def draw_snake_iter(segments, BOUNDING_BOX):
    """
    This function draws a snake iteratively with random segment length, thickness, and angle.

    Segments: The number of segments left to draw for the snake.
    Total: The total units of length of the snake.
    BOUNDING_BOX: The maximum distance that the turtle can travel from the origin.

    Preconditions: The turtle is in the bounding box.
    Postconditions: The turtle is in the bounding box.
    """
    total = 0
    while segments > 0:
        MAX_LENGTH = 20
        MIN_THICKNESS = 1
        MAX_THICKNESS = 10
        MAX_ANGLE = 30
        border_correct(BOUNDING_BOX, MAX_LENGTH)
        length = random.randint(0, MAX_LENGTH)
        turtle.pencolor(random.random(), random.random(), random.random())
        turtle.pensize(random.randint(MIN_THICKNESS, MAX_THICKNESS))
        turtle.forward(length)
        turtle.left(random.randint(0, MAX_ANGLE * 2) - MAX_ANGLE)
        total = total + length
        segments = segments - 1
    return total


def main():
    """
    This function prompts the user for the number of segments in the snake, calls the recursive function,
    prints the length of the recursive snake, calls the iterative function, and prints the length of the iterative snake.
    It then prompts the user to close the turtle window.

    Preconditions: The turtle is at the origin facing East.
    Postconditions:
    """
    segments = int(input("How many segments? (0-500)"))
    MAX_SEGMENTS = 500
    if not(segments <= MAX_SEGMENTS and segments >= 0):
        print("Segments must be between 0 and 500 inclusive.")
        return
    BOUNDING_BOX = 200
    turtle.screensize(BOUNDING_BOX * 2, BOUNDING_BOX * 2)
    turtle.hideturtle()
    draw_bounding_box(BOUNDING_BOX)
    total = draw_snake_tail(segments, 0, BOUNDING_BOX)
    print("The recursive snake is " + str(total) + " units long.")
    input("Press Enter to continue.")
    turtle.reset()
    turtle.hideturtle()
    draw_bounding_box(BOUNDING_BOX)
    total = draw_snake_iter(segments, BOUNDING_BOX)
    print("The iterative snake is " + str(total) + " units long.")
    print("Close the Turtle window to exit the program.")

    turtle.done()


if __name__ == '__main__':
    main()