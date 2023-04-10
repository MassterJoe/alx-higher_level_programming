#!/usr/bin/python3
"""
This function finds the peak of a list of integers
"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""


    peak = None
    for i in range(len(list_of_integers)):
        if list_of_integers[i] < list_of_integers[i-1]:
            list_of_integers[i], list_of_integers[i-1] = (
                list_of_integers[i-1], list_of_integers[i])
        peak = list_of_integers[i]
    return peak
