#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("{:d} / {:d} = {:d}".format(a, b, result))
    except ZeroDivisionError:
        return None
    finally:
        return result
