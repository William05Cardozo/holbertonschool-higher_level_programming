#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list2 = my_list[:]
    if not my_list:
        return(None)
    for i in range(len(list2)):
        if (list2[i] % 2 == 0):
            list2[i] = True
        else:
            list2[i] = False
    return(list2)
