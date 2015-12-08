#!/usr/bin/env python3

import skilstak.colors as c

def hello(who):
    """Print Hello world!"""
    print(c.clear + "Hello " + who + c.reset)

def multi(message):
    """print hello world in multicolored letters"""
    while True:
        print(c.clear + c.multi(message))

def nyan(message):
    """print hello world in nyan"""
    while True:
        print(c.rc() + message, end= " ")
