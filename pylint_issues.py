import os
import sys
import json


def BadFunctionName(a,b,c,d,e,f,g,h):
    x = 1
    unused_variable = 5
    if a == None:
        return b
    else:
        return c


class myclass:
    def method(self):
        print("no docstring, bad class name")
        undefined_call(5)
