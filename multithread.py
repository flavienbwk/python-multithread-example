#!/bin/python3

# Multithread script example

import concurrent.futures

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # It's a ridiculously low amount of numbers, increase !!!!

def print_square_number(number):
    print()

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for number in numbers:
            executor.submit(print_square_number, number) # You can pass as many arguments as you want

if __name__ == "__main__":
    main()
