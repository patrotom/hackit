#!/usr/bin/python3

import socket
import sys

import message_getting as mg

BUFFER_SIZE = 128


class Handler:
    '''Main class which is evaluating incoming messages using finite state automata'''
    def __init__(self, sock):
        '''Constructor'''
        self.sock = sock
        self.listener = mg.Listener(self.sock)

    def automata(self):
        '''Function which is implementing automata for evaluation of messages'''    
        while True:
            packet = self.listener.get_message()
            if packet == 'ERROR':
                break


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('192.168.10.1', 10000)
    print('Starting up on {}, port: {}'.format(*server_address))
    sock.bind(server_address)
    
    h = Handler(sock)
    h.automata()
main()
