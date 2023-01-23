#!/usr/bin/env python3
""" Write a type-annotated function sum_list which takes
a list input_list of floats as argument and
returns their sum as a float. """



def sum_list(input_list: list([float])) -> float:
    """ takes a list input_list of floats and return their sum"""
    summ: float = 0.0
    for i in input_list:
            summ += i
        
    return summ
