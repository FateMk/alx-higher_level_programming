#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    items = len(sys.argv)
    if items <= 1:
        print("0 arguments.")
    else:
        if items == 2:
            print("{:d} argument:".format(items -1))
        else:
            print("{:d} arguments:".format(items -1))
        for i in range(1, items):
            print("{:d}: {}".format(i, sys.argv[i]))
