#!/usr/bin/python3

""" 
    station.py 
        - class for arduino station, specifying default configuration of the station.
"""

import dfa as df

class Station:
    """ Station contains info about stations relevant for the computation. """ 
    def __init__(self, ip, name, position, sensors):
        """ -> String -> "in" / "out" -> [String] -> Station() """
        self.ip = ip
        self.name = name
        self.sensors = Sensors(sensors)
        self.position = position
        self.dfa = df.DFA()        
        
    def process(self, state):
        """ -> State -> Bool
            - takes state processes it in dfa and sets new State
            - return True if change of state was triggered resulting in Control action
        """
        return self.dfa.func(state)

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def set_name(self, name):
        self.name = name

    def get_temp(self):
        if self.sensors.temp:
            return self.sensors.temp_v

    def has_sensor(self, name):
        if name == "fire":
            return self.sensors.fire
        elif name == "temp":
            return self.sensors.temp
        elif name == "humid":
            return self.sensors.humid
        elif name == "press":
            return self.sensors.press
        elif name == "gas":
            return self.sensors.gas
        elif name == "co":
            return self.sensors.co
        elif name == "servo":
            return self.sensors.servo



class Sensors:
    """ Class for managing available sensors on Station. """
    
    def __init__(self, sensors):
        """ -> [String] -> Sensors() """
        
        self.fire_v = None
        self.temp_v = None
        self.pres_v = None
        self.humid_v = None
        self.co_v = None
        self.gas_v = None

        if "fire" in sensors:
            self.fire = True
        else:
            self.fire = False
                
        if "temp" in sensors:
            self.temp = True
        else:
            self.temp = False
                
        if "pres" in sensors:
            self.pres = True
        else:
            self.pres = False
                
        if "humid" in sensors:
            self.humid = True
        else:
            self.humid = False
                
        if "co" in sensors:
            self.co = True
        else:
            self.co = False
                
        if "gas" in sensors:
            self.gas = True
        else:
            self.gas = False
        
        if "servo" in sensors:
            self.servo = True
        else:
            self.servo = False

    def set_temp(self, temp):
        self.temp_v = temp

    def set_humid(self, humid):
        self.humid_v = humid

    def set_pres(self, pres):
        self.pres_v = pres
