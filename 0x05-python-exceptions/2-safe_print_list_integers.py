#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    this is where i print my code to print a list of anything, but only prints the integers
    Returns the amount of integers printed
    """
    integer = 0
    printed = 0
    for integer in range(0, x):
        try:
            print("{:d}".format(my_list[integer]), end="")
            printed = printed + 1
        except (ValueError, TypeError):
            continue
    print()
    return printed
