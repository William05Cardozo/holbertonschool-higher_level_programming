#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lng = len(sys.argv) - 1
    result = 0
    for i in range(1, (lng + 1)):
        result = result + int(sys.argv[i])
    print("{:d}".format(result))
