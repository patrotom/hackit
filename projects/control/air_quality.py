
"""
    air_quality.py
        - function get_response serves for feeding the dfa with its sign input based on
        the air conditions preferations
"""

def get_response(packet, desired_air, outside_temp):
    """ -> Packet -> Int -> State 
        - takes packet of Inform or Urgent type and chooses most urgent response in
        form of State that will be processed further by dfa on that station
    """

    result = None
    if packet.t == 3:
        result = check_type3(packet.fire, packet.gas, packet.coa)
        if result != None:
            return result
    elif packet.t == 1:
        result = check_temp(packet.temp, desired_ait.temp, outside_temp)
        if result != None:
            return result
    else:
        return result

def check_temp(temp, desired_temp, outside_temp):
    """ -> Int -> State """
    if temp == None:
        return None
    if temp > desired_temp + 2:
        if outside_temp > temp:
            return State("close", 2)
        else:
            return State("open", 2)
    elif temp < desired_temp - 2:
        if outside_temp > temp:
            return State("open", 2)
        else:
            return State("close", 2)
    else:
        return None

def check_humid(humid, desired_humid):
    """ -> Int -> Int -> State """
    if humid == None:
        return None

    if humid < desired_humid - 5:
        return State("open", 3)
    elif humid > desired_humid + 5:
        return State("close", 3)
    else:
        return None

def check_type3(fire, gas, co):
    if fire or gas or co:
        return State("open", 4)
    else:
        return None
