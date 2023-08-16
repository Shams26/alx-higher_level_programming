#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    re_arr = list(a_dictionary.keys())
    re_arr.sort()
    for i in re_arr:
        print("{}: {}".format(i, a_dictionary.get(i)))
