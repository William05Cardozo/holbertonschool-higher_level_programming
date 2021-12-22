#!/usr/bin/python3
for a in range(97, 122):
    if a in [101, 113]:
        continue
    print("{:c}".format(a), end="")
