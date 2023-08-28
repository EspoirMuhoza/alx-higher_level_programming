#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    integer = 0
    printed = 0
    for integer in range(0, x):
        try:
            print("{}".format(my_list[integer]), end="")
            printed = printed + 1
        except ValueError:
            continue
    print()
    return printed
