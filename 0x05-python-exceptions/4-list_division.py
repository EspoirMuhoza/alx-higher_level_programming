#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    here is my code to takee two lists and creates a new list with result of divison
    operation

    handles errors and prints them to stdout
    """
    integer = 0
    new_list = []
    result = 0
    for integer in range(0, list_length):
        try:
            result = (my_list_1[integer] / my_list_2[integer])
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
