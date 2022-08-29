#!/usr/bin/python3
def no_c(my_string):
    new_list = my_string
    for i in range(len(new_list)):
        if i <= ord('c'):
            return(new_list[i])
            

