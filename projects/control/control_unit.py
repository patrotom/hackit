#!/usr/bin/python3

import station      # for classes Station, Sensors
import parse        # for parse() and classes Inform, Control, Urgent
import dfa          # for classes DFA, State
import air_quality  # for get_response()

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
        self.aim = desired_air_status
        demo()

    def demo(self):
        self.stations = [ Station("10.0.0.1", "room1", "in", ["fire", "temp", "humid", "pres", "servo"]), Station("10.0.0.2", "room2", "in", ["servo", "co", "gas", "temp"]), Station("10.0.0.3", "garden", "out", ["temp", "humid"])]

    def process(self, ip, t, d1, d2, d3):
        """ -> String -> Int -> Int -> Int -> Int -> State
            - main function returns response for information packet creating response
            - if no action should be triggered returns None
        """
        packet = parse(t, d1, d2, d3)
        if packet.t != 1 and packet != 3:
            print("Error: ControlUnit received packet of wrong type.")
        
        station = None                                                      # find matching ip station
        for s in self.stations:
            if ip == s.ip:
                station = s
        if station:
            print("Error: ControlUnit received packet from unknown IP.")

        responce_sign = get_response(packet, self.aim, get_outside_temp())  # get response based on user preferences
        if station.dfa.func(response_sign):                                 # if station state has changed
            if station.dfa.current.state == "open":
                return open_window
            else:
                return close_window
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
        return self.ain.humid

    def set_desired_temp(self, val):
        self.aim.temp = val

    def set_desired_humid(self, val):
        self.aim.humid = val

    def open_window(self):
        return Control(1)

    def close_window(self):
        return Control(2)


class Desired_air_status:
    """ Representing desired status of temp and humidity. """
    def __init__(self):
        self.temp = 21
        self.humid = 42

