#!/usr/bin/env python3
# Created by: Marcus Wehbi
# Created on: Sep 26, 2022
# This program asks the user for the radius of
# a circle in mm. It then calculates and displays
# the circumference using tau.
import constants
import math


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle (mm): "))

    # calculate the circumference
    circumference = constants.TAU * radius
    area = math.pi * radius**2

    # display the circumference
    print("")
    print("Circumference = {} mm".format(circumference))
    print("")
    print("Area = {} mm^2".format(area))


if __name__ == "__main__":
    main()
