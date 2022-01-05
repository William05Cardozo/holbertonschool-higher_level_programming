#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = [replace if x == search else x for x in my_list]
    return(nlist)
