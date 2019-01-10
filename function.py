# this module will be sent to the server as 'flameexample.stuff'

#from __future__ import print_function


def numberoflines(filename):
    number = 0

    with open(filename, 'r') as f:
        for line in f:
            number += 1
    return number

