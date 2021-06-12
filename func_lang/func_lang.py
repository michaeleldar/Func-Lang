#!/usr/bin/python3

import random
from turtle import *


def run_graphics():  # opens the turtle window and makes
    shape("classic")  # standard settings
    speed(1)
    pensize(4)


varibles = {}  # makes a varibles dictionary


def make_ran_num(varible, min_num, max_num):  # makes a
    if min_num and max_num in varibles:
        varibles[varible] = random.randint(varibles[min_num],
                                           varibles[max_num])
    elif max_num in varibles:
        varibles[varible] = random.randint(min_num, varibles[max_num])
    elif min_num in varibles:
        varibles[varible] = random.randint(varibles[min_num], max_num)
    else:
        varibles[varible] = random.randint(min_num, max_num)
    # random number and sets it to a varible


def graphics_turn(direction, degrees):  # turns the turtle
    if direction == "right":  # shape
        right(degrees)
    elif direction == "left":
        left(degrees)
    else:
        print(direction, "is not a valid direction")


def graphics_move(direction, pixels):  # moves the turtle
    if direction == "forward":  # shape
        forward(pixels)
    elif direction == "backward":
        back(pixels)
    else:
        print(direction, "is not a valid direction")


def graphics_colour(colour):  # sets the pen colour
    if colour == "blue":
        color("blue")
    elif colour == "red":
        color("red")
    elif colour == "green":
        color("green")
    elif colour == "yellow":
        color("yellow")
    else:
        print(colour, "is not a reconised colour")


def write(contents):  # displays text on the screen
    print(contents)


def declare(varible, value):  # makes a varible
    varibles[varible] = value


def write_var(varible):  # displays a varible on the screen
    print(varibles[varible])


def ask_input(varible, question):  # asks a question and
    varibles[varible] = input(question)  # and sets the
    # answer to a varible


def add(varible, num1, num2):  # adds 2 numbers and sets
    if num1 and num2 in varibles:  # them to varibles
        varibles[varible] = int(varibles[num1]) + int(varibles[num2])
    elif num1 in varibles:
        varibles[varible] = int(varibles[num1]) + num2
    elif num2 in varibles:
        varibles[varible] = int(varibles[num2]) + num1
    else:
        varibles[varible] = num1 + num2


def subtract(varible, num1, num2):  # subtracts two numbers
    if num1 and num2 in varibles:  # and sets them to
        varibles[varible] = int(varibles[num1]) - int(varibles[num2])
    elif num1 in varibles:  # varibles
        varibles[varible] = int(varibles[num1]) - num2
    elif num2 in varibles:
        varibles[varible] = int(varibles[num2]) - num1
    else:
        varibles[varible] = num1 - num2


def multiply(varible, num1, num2):  # multiplys two numbers
    if num1 and num2 in varibles:  # and sets them to a
        varibles[varible] = int(varibles[num1]) * int(varibles[num2])
    elif num1 in varibles:  # to a varible
        varibles[varible] = int(varibles[num1]) * num2
    elif num2 in varibles:
        varibles[varible] = int(varibles[num2]) * num1
    else:
        varibles[varible] = num1 * num2


def divide(varible, num1, num2):  # divides two numbers
    if num1 and num2 in varibles:  # and sets them to a
        varibles[varible] = int(varibles[num1]) / int(varibles[num2])
    elif num1 in varibles:  # varible
        varibles[varible] = int(varibles[num1]) / num2
    elif num2 in varibles:
        varibles[varible] = int(varibles[num2]) / num1
    else:
        varibles[varible] = num1 / num2


def check_equals(num1, num2, file):  # checks if 2 numbers are
    if num1 and num2 in varibles:  # equal
        if varibles[num1] != varibles[num2]:
            quit()
    elif num1 in varibles:
        if varibles[num1] != num2:
            quit()
    elif num2 in varibles:
        if num1 != varibles[num2]:
            quit()
    else:
        if num1 != num2:
            quit()


def graphics_bgcolour(colour):
    Screen().bgcolor(colour)
