import socket
import sys

BUFFER_SIZE = 128

class Listener:
    '''Class which is handling getting of new messages'''
    def __init__(self, connection):
        '''Constructor'''
        self.connection = connection
        self.counter = 0

    def get_message(self):
        '''Function which is listening and waiting for a message'''
        while True:
            data = self.connection.recv(BUFFER_SIZE)
            if data and len(data) >= 1:
                raw_data = data.decode('ascii')
                print('R ========================== R')
                print('TypeOfMessage-1|Temp|Hum|Pressure|In/Out')
                print('TypeOfMessage-3|Fire|Gas|CO|In/Out')
                print(raw_data)
                print('R ========================== R')
                self.counter += 1
                if self.counter % 50 == 0:
                    self.connection.sendall('1'.encode())
                else:
                    self.connection.sendall('2'.encode())
                return raw_data
            else:
                return 'ERROR'
