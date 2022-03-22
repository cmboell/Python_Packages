"""
Assignment: Python Packages Assignment
Program: main.py
Author: Colby Boell
Last date modified: 03/21/2022

The purpose of this program is to use modules from a package by importing them in to the main.
"""
# imports from the package
from definitions import greetings, dictionary_ops, set_ops


# main to call
if __name__ == '__main__':
    dict_list = {12: 'Colby', 13: 'Margot', 14: 'Nala'}
    set_list = ('Cardigan', 'Sweater', 'T-shirt', 'Sweater')

    print(greetings.greeting())
    print(greetings.author())
    dictionary_ops.print_dict(dict_list)
    set_ops.print_set(set_list)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


"""
Output:
Hello, nice to meet you!
Author: Colby Boell
12 Colby
13 Margot
14 Nala
Cardigan
Sweater
T-shirt
Sweater
"""
