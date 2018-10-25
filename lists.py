#!/usr/bin/env python3

# John Asare
# 10/25/18 14:44

""" Lab on lists """


def sumOfOdd(intlist):
    total = 0
    for i in intlist:
        if i % 2 == 1:
            total = total + i
    return total
    pass


def productOfEven(intlist):
    total = 1
    for i in intlist:
        if i % 2 == 0:
            total = total * i
    return total
    pass


def changeList(intlist):
    for index, value in enumerate(intlist):
        if value % 2 == 1:
            intlist[index] = (value + 5) / 2
        else:
            intlist[index] = value / 2
    pass

def membersDivisibleBy3(intlist):
    pass

def isReverse(intlist_one, intlist_two):
    pass

