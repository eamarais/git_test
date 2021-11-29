#!/usr/bin/python

"""
Arbitrary script to exit the python script using sys.exit(1)
Created for Git interactive learning session
"""

import os
import sys
import numpy as np

# Print hello world
print("Hello World")

# Create 2D array using np.arange that is 144 columns (longitudes)
# and 91 rows (latitudes):
nx=91
ny=144
data_array = np.arange(nx,ny)

# Exit the programme:
sys.exit(1)

