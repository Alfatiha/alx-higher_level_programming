#!/usr/bin/python3
def no_c(my_string):
    my_string_is = list(my_string)
    index_c = 0
    for index in my_string_is:
        if index == 'c' or index == 'C':
            my_string_is[index_c] = ""
        index_c += 1
    return ''.join(my_string_is)
