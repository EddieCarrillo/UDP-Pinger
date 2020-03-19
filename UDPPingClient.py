from time import gmtime, strftime
from os import environ
from socket import *
from time import *

#Much cleaner to read.
TimeoutException = timeout
#Convenience function for ping messages.
def ping_message(seqNumber):
    return f'Ping {seqNumber} {strftime("%H:%M:%S", gmtime())}'

def no_response_message():
    return f'Request timed out'

#Grab hostname from env var 
serverName = environ['UDP_PING_HOSTNAME']
serverPort = int(environ['UDP_PING_PORT'])
#Set up client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
#Set the client timeout to one second.
clientSocket.settimeout(1)
max_attempts = 10
seq_number = 1

#Start pings.
for i in range(max_attempts):
    try:
        message = ping_message(seq_number)
        pingTime = time_ns()
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        ret, addr = clientSocket.recvfrom(2048)
        pongTime = time_ns()

        rtt = (pongTime - pingTime)*10**-6
        print(f'The total round trip time for the ping/pong is {rtt} ms')
        seq_number = seq_number + 1
    except TimeoutException:
        print(no_response_message())

    #Only increment ping count if succesfully receive the pong message