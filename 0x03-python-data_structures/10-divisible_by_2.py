#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            my_new_list.append(True)
        else:
            my_new_list.append(False)
    return my_new_list
