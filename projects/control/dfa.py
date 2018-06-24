#!/usr/bin/python3

""" 
    dfa.py 
        - contains class for work with deterministic finate automaton
"""

class State:
    """ Class representing state of the automaton. """
    def __init__(self, state, priority):
        self.state = state
        self.priority = priority


class DFA:
    def __init__(self):
        self.language = [State("open", x+1) for x in range(4)] + [State("close", x+1) for x in range(4)]
        self.current = State("close", 1)
        self.has_changed = True

    def func(self, sign):
        """ -> State -> Boot
            - takes state computes dfa and changes current state
            - returns Bool if change should result in Control action
        """
        
        if self.current.state == "open" and sign.state == "open":
            self.current = State("open", max(self.current.priority, sign.priority))
            self.has_changed = False
            return self.has_changed
                
        elif self.current.state == "close" and sign.state == "close":
            self.current = State("close", max(self.current.priority, sign.priority))
            self.has_changed = False
            return self.has_changed

        elif self.current.state == "open" and sign.state == "close":
            if self.current.priority <= sign.priority:
                self.current = State("close", sign.priority)
            else:
                self.current = State("open", self.current.priority)
            
            if self.current.priority <= sign.priority:
                self.has_changed = True
            else:
                self.has_changed = False
            return self.has_changed
                
        elif self.current.state == "close" and sign.state == "open":
            if self.current.priority <= sign.priority:
                self.current = State("open", sign.priority)
            else:
                self.current = State("close", self.current.priority)
            
            if self.current.priority <= sign.priority:
                self.has_changed = True
            else:
                self.has_changed = False
            return self.has_changed
