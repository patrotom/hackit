import socket
import sys

BUFFER_SIZE = 128


class Listener:
    '''Class which is handling getting of new messages'''
    def __init__(self, sock):
        '''Constructor'''
        self.sock = sock
            
    def get_message(self):
        '''Function which is listening and waiting for a message'''
        while True:
            data, address = self.sock.recvfrom(BUFFER_SIZE)
            if data:
                raw_data = data.decode('ascii')
                print('Received:', raw_data)
                self.sock.sendto('Hello!\n'.encode(), address)
                return raw_data
            else:
                return 'ERROR'
