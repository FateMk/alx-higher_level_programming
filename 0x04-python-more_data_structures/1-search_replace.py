#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in my_list:
        new_list = my_list
        if i == search:
            replace = search
    return [replace if search == n else n for n in my_list]

