#!/usr/bin/python3

import parse        as pa    # for parse() and classes Inform, Control, Urgent
import station      as st    # for classes Station, Sensors
import dfa          as df    # for classes DFA, State

""" 
    control_unit.py 
        - responsible for handling of control unit (raspberry pi)
        - categorizes stations (arduinos) based on their sensors
        - 
"""

class ControlUnit:
    """ Main control unit.
        Current init implements hard-coded demo of the infrastructure.
        Function process does return coresponding response in format of packet.
        Other setters serve for customization of desired air and getting
        current air conditions.
    """        
    def __init__(self):
        self.aim = DesiredAir()
        self.demo()
    # 0 - IP, 1 - Inner/Outter, 2 - Message type, 3-5 - values
    def demo(self):
        self.stations = [st.Station("in", "room1", "in", ["temp", "humid", "pres", "servo", "gas", "co"]), st.Station("out", "garden", "out", ["temp", "humid"])]

    def process(self, ip, t, d1, d2, d3):
        """ -> String -> Int -> Int -> Int -> Int -> State
            - main function returns response for information packet creating response
            - if no action should be triggered returns None
        """
        packet = pa.parse(t, d1, d2, d3)
        if packet.type != 1 and packet != 3:
            print("Error: ControlUnit received packet of wrong type.")
            return None
        
        # find matching ip station
        station = None
        for s in self.stations:
            if ip == s.ip:
                station = s
        if station is None:
            print("Error: ControlUnit received packet from unknown IP.")
            return None

        self.sensor_avail_filter(station, packet)

        # get response based on user preferences
        response_sign = get_response(packet, self.aim, self.get_outside_temp(), station) 
        
        # case of no respon
        if response_sign is None:
            return None

        # if station state has changed
        if station.dfa.func(response_sign):                                     
            if station.dfa.current.state == "open":
                return [2, 1, 0, 0]
            else:
                return [2, 2, 0, 0]
        return None

    def sensor_avail_filter(self, station, packet):
        """ - in case of type 1 packet change unrelevant data to None """
        if packet.type == 1:
            if not station.has_sensor("temp"):
                packet.temp = None
            if not station.has_sensor("humid"):
                packet.humid = None
            if not station.has_sensor("pres"):
                packet.pres = None

    def get_temp(self, station_name):
        for s in self.stations:
            if s.get_name() == station_name:
                return s.get_temp()
        return None

    def get_outside_temp(self):
        for s in self.stations:
            if s.get_position() == "out":
                return s.get_temp()
        return None

    def get_desired_temp(self):
        return self.aim.temp

    def get_desired_humid(self):
        return self.aim.humid

    def set_desired_temp(self, val):
        self.aim.temp = val

    def set_desired_humid(self, val):
        self.aim.humid = val


class DesiredAir:
    """ Representing desired status of temp and humidity. """
    def __init__(self):
        self.temp = 21
        self.humid = 42


"""
    air_quality
        - function get_response serves for feeding the dfa with its sign input
        based on the air conditions preferations
"""

def get_response(packet, desired_air, outside_temp, station):
    """ -> Packet -> Int -> Sensor -> State 
        - takes packet of Inform or Urgent type and chooses most urgent 
        response in form of State that will be processed further by dfa on that
        station
    """
    if packet.type == 1:
        station.sensors.set_temp(packet.temp)
        station.sensors.set_humid(packet.humid)
        station.sensors.set_pres(packet.pres)

    result = None
    if packet.type == 3:
        result = check_type3(packet.fire, packet.gas, packet.co)
    if result is not None:
        return result
    elif packet.type == 1:
        result = check_humid(packet.humid, desired_air.humid)
    if result is not None:
        return result
    result = check_temp(packet.temp, desired_air.temp, outside_temp)
    if result is not None:
        return result
    else:
        return result

def check_temp(temp, desired_temp, outside_temp):
    """ -> Int -> State """
    if temp is None or outside_temp is None:
        return None

    if temp > desired_temp + 2:
        if outside_temp > temp:
            return df.State("close", 2)
        else:
            return df.State("open", 2)
    elif temp < desired_temp - 2:
        if outside_temp > temp:
            return df.State("open", 2)
        else:
            return df.State("close", 2)
    else:
        return None

def check_humid(humid, desired_humid):
    """ -> Int -> Int -> State """
    if humid is None:
        return None

    if humid < desired_humid - 5:
        return df.State("open", 3)
    elif humid > desired_humid + 5:
        return df.State("close", 3)
    else:
        return None

def check_type3(fire, gas, co):
    if fire or gas or co:
        return df.State("open", 4)
    else:
        return None

'''
u = ControlUnit()
print(u.process(0, 1, 20, 40, 10000))
print(u.process(1, 1, 10, 40, 10000))
print(u.process(1, 1, 5, 40, 10000))
print(u.process("in", 1, 1, 90, 10000))
print(u.process("in", 1, 30, 10, 10000))
print(u.process("in", 1, 1, 40, 10000))
'''
