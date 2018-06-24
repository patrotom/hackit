#!/usr/bin/python3

import socket
import sys

import message_getting as mg

BUFFER_SIZE = 128


class Handler:
    '''Main class which is evaluating incoming messages using finite state automata'''
    def __init__(self, connection, client_address):
        '''Constructor'''
        self.connection = connection
        self.client_address = client_address
        self.listener = mg.Listener(self.connection)

    def automata(self):
        '''Function which is implementing automata for evaluation of messages'''    
        while True:
            try:
                packet = self.listener.get_message()
                if packet == 'ERROR':
                    break
            except socket.error:
                pass


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.10.1', 10000)
    print('Starting up on {}, port: {}'.format(*server_address))
    sock.bind(server_address)
    sock.listen(1)
    while True:
        connection, client_address = sock.accept()
        h = Handler(connection, client_address)
        h.automata()
main()
