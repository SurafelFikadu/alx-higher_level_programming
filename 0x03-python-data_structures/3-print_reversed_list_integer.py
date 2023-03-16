#1/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for my_list in reversed(range(1, 6)):
        print(print_reversed_list_integer(my_list))
