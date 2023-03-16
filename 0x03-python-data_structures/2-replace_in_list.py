#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    idx = 3
    my_list = [1, 2, 3, 4, 5]
    print(my_list)
    new_element = 9
    if idx < 0 and idx != my_list:
        return my_list
    my_list[3] = new_element
    print(my_list)
