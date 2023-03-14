#!/usr/bin/python3
def element_at(my_list, idx):
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    if idx < 0 and idx != my_list:
        return None
    else:
        print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
