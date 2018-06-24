#!/usr/bin/python3

""" 
    dfa.py 
        - contains class for work with deterministic finate automaton
"""

class DFA:
    def __init__(self):
        self.language = [State("open", x+1) for x in Range(4)] + [State("close", x+1) for x in Range(4)]
        self.current = State("close", 1)
        self.has_changed = True

    def func(self, sign):
        """ -> State -> Boot
            - takes state computes dfa and changes current state
            - returns Bool if change should result in Control action
        """
        
        if current.state == "open" and sign.state == "open":
            self.current = State("open", max(current.priority, sign.priority))
            self.has_changed = False
            return self.has_changed
                
        elif current.state == "close" and sign.state == "close":
            self.current = State("close", max(current.priority, sign.priority))
            self.has_changed = False
            return self.had_changed
                
        elif current.state == "open" and sign.state == "close":
            if current.priority < sign.priority:
                self.current = State("close", sign.priority)
            else:
                self.current = State("open", current.priority)
            
            if current.priority < sign.priority:
                self.has_changed = True
            else:
                self.has_changed = False
            return self.has_changed
                
        elif current.state == "close" and sign.state == "open":
            if current.priority < sign.priority:
                self.current = State("open", sign.priority)
            else:
                self.current = State("close", current.priority)
            
            if current.priority < sign.priority:
                self.has_changed = True
            else:
                self.has_changed = False
            return self.has_changed

class State:
    """ Class representing state of the automaton. """
    def __init__(self, state, priority):
        self.state = state
        self.priority = priority
