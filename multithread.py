#!/bin/python3

# Multithread script example

import time
import concurrent.futures

figures = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # It's a ridiculously low amount of figures, increase !!!!

def print_figure(figure):
    print(figure)
    time.sleep(0.1)

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for figure in figures:
            executor.submit(print_figure, figure) # You can pass as many arguments as you want

if __name__ == "__main__":
    main()
