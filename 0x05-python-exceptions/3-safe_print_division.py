#!/usr/bin/python3


def safe_print_division(a, b):
    """
    my function to dive two integers
    """
    try:
        result = a / b
    except:
        result = None
    finally:
        print("Inside result: {}".format(res))
    return result
