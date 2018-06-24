#!/usr/bin/python3

import socket
import sys

import message_getting as mg
import control_unit as cu

BUFFER_SIZE = 128

class Handler:
    '''Main class which is evaluating incoming messages using finite state automata'''
    def __init__(self, connection, client_address):
        '''Constructor'''
        self.connection = connection
        self.client_address = client_address
        self.listener = mg.Listener(self.connection)
        self.last_standard = []
        self.last_urgent = []
        self.control_unit = cu.ControlUnit()

    def automata(self):
        '''Function which is implementing automata for evaluation of messages'''    
        while True:
            try:
                packet = self.listener.get_message()
                
                #if len(packet) > 1:
                #    self.print_info(packet)
                # result = self.process_message(packet)

                # if result != None and result != 'ERROR':
                #     self.connection.sendall(str(result[1]).encode())
                # print(result)
                # if result == None:
                #     print('Normal results', packet)

                if packet == 'ERROR':
                    break
            except socket.error:
                pass
                #print('Slow WiFi connection...')
    
    # 1 - inner, 0 - outter
    # def process_message(self, message):
    #     message = message.replace('\r\n', '')
    #     input_values = message.split('|')
    #     if len(input_values) <= 1 and len(input_values) >= 5:
    #         #print(input_values[0], 'GOOD')
    #         return 'ERROR'
    #     tmp = ''
    #     try:
    #         for i in range (0, len(input_values), 1):
    #             input_values[i] = int(input_values[i])
    #         print('OK')
    #         if input_values[4] == 1:
    #             tmp = 'in'
    #         else:
    #             tmp = 'out'
    #     except ValueError:
    #         pass

    #     return self.control_unit.process(tmp, input_values[0], input_values[1], input_values[2], input_values[3])

    def print_info(self, message):
        values = message.split('|')
        # for i in range (0, len(values), 1):
        #     values[i] = int(values[i])
        print('=================')
        print('Temperature:', values[1], '*C')
        print('Humidity:', values[2], '%')
        print('Pressure:', values[3], 'PA')
        print('=================')

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
