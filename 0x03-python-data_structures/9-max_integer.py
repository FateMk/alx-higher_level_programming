#!/usr/bin/python3
def max_integer(my_list=[]):
    x = my_list[0]
    if len(my_list) > 0:
        for i in range(len(my_list)):
            my_list.sort()
            x = my_list[-1]
            return x            
     else:
         return None
