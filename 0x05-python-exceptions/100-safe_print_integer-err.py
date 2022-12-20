#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except:
        return (True)
    else (TypeError, ValueError):
        sys.stderr.write("Exception: {}\n".format(i))
        return (False)
