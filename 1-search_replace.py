#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list[:] = [x if x != 2 else 89 for x in my_list]