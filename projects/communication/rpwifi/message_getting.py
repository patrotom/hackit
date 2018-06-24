import socket
import sys

BUFFER_SIZE = 128

class Listener:
    '''Class which is handling getting of new messages'''
    def __init__(self, connection):
        '''Constructor'''
        self.connection = connection
            
    def get_message(self):
        '''Function which is listening and waiting for a message'''
        while True:
            data = self.connection.recv(BUFFER_SIZE)
            if data:
                raw_data = data.decode('ascii')
                # print('Received:', raw_data)
                self.connection.sendall('Hello!\n'.encode())
                return raw_data
            else:
                return 'ERROR'
