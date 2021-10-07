#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This program uses a nested loop to print integers from 1000-2000


def main():
    # this function uses a nested loop to print integers

    # loop var
    integer_count = 1000

    # process & output
    for integer_count in range(1000, 2000 + 1):
        if integer_count % 5 == 0:
            print("")
            print(integer_count, end=" ")
        else:
            print("{0} ".format(integer_count), end="")

    print("\nDone.")


if __name__ == "__main__":
    main()
