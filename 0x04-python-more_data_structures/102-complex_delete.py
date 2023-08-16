#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for dico_val in list_keys:
        if value == a_dictionary.get(dico_val):
            del a_dictionary[dico_val]

    return (a_dictionary)
