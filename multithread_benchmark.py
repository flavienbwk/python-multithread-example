#!/bin/python3

# Multithread script example benchmark

import time
import random
import concurrent.futures

figures = [random.randint(1, 500000) for i in range(0, 100)] # Generating random figures

def print_figure(figure):
    print(figure)
    time.sleep(1)

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for figure in figures:
            executor.submit(print_figure, figure) # You can pass as many arguments as you want

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

