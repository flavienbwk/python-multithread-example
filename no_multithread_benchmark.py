#!/bin/python3

# Multithread script example benchmark

import time
import random

figures = [random.randint(1, 500000) for i in range(0, 100)] # Generating random figures

def print_figure(figure):
    print(figure)
    time.sleep(1)

start_time = time.time()
for figure in figures:
    print_figure(figure)
print("--- %s seconds ---" % (time.time() - start_time))
