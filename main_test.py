import main
import io
import sys
import re
import math
import types


def test_main_1():
    mylist = [5, 10, 15, 25, 20, 55, 40]
    ret = main.getAvg(mylist)
    print(f'Retrun value is {ret}')
    assert round(ret) == 24


def test_main_2():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ret = main.getAvg(mylist)
    print(f'Retrun value is {ret}')
    assert round(ret) == 6, 'round up of avg is 6'
