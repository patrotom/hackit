#!/usr/bin/python3

"""
    parse.py
        - function parse returns parsed packet based on 4 given integers
        - see format of each packet and its description
"""

def parse(t, d1, d2, d3):
    """ Packet format: type{Inform : 1, Urgent : 2, Control : 3}[4B] | ..."""
    if t == 1:
        return Inform(d1, d2, d3)
    elif t == 2:
        return Control(d1)
    elif t == 3:
        return Urgent(d1, d2, d3)
    else:
        print("Error: parsing packet of unknown type")

class Inform:
    """ type | Temperature(Int)[4B] | Humidity(Int)[4B] | Pressure(Int)[4B] """
    def __init__(self, d1, d2, d3):
        self.type = 1
        self.temp = d1
        self.humid = d2
        self.press = d3

class Urgent:
    """ type | fire(Bool)[4B] | flamable_gas(Bool)[4B] | CO(Bool)[4B] """
    def __init__(self, d1, d2, d3):
        self.type = 3
        self.fire = d1
        self.gas = d2
        self.co = d3

class Control:
    """ type | cmd{ Request : 0, Open :  1, Close : 2 }[4B] """
    def __init__(self, d1):
        self.type = 2
        self.cmd = d1
