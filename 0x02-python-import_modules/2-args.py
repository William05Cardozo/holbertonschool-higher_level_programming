#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    lng = len(sys.argv) - 1
    if lng == 0:
        print("{:d} arguments.".format(lng))
    elif lng == 1:
        print("{:d} arguments:".format(lng))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(lng))
        for i in range(1, l + 1):
            print("{:d}: {}".format(i, sys.argv[i]))
