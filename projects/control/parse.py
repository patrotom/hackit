#!/usr/bin/python3

"""
    parse.py
        - function parse returns parsed packet based on 4 given integers
        - see format of each packet and its description
"""

def parse(t, d1, d2, d3):
    return Packet(t, d1, d2, d3)

class Packet:
    """ Packet format: type{Inform : 1, Urgent : 2, Control : 3}[4B] | ..."""
    def __init__(self, t, d1, d2, d3):
        self.type = t
        if t == 1:
            self = Inform(d1, d2, d3)
        elif t == 2:
            self == Control(d1)
        elif t == 3:
            self = Urgent(d1, d2, d3)
        else:
            print("Error: parsing packet of unknown type")

class Inform(Packet):
    """ type | Temperature(Int)[4B] | Humidity(Int)[4B] | Pressure(Int)[4B] """
    def __init__(self, d1, d2, d3):
        self.type = 1
        self.temp = d1
        self.humid = d2
        self.press = d3

class Urgent(Packet):
    """ type | fire(Bool)[4B] | flamable_gas(Bool)[4B] | CO(Bool)[4B] """
    def __init__(self, d1, d2, d3):
        self.type = 3
        self.fire = d1
        self.gas = d2
        self.co = d3

class Control(Packet):
    """ type | cmd{ Request : 0, Open :  1, Close : 2 }[4B] """
    def __init__(self, d1):
        self.type = 2
        self.cmd = d1
