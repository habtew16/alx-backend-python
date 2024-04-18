#!/usr/bin/env python3
'''
list of numbers and floats
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Computes the sum of a list of integers and floating numbers.
    '''
    return float(sum(mxd_lst))
