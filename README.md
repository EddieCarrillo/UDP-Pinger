# UDP-Pinger
Create a client ping program using Python. Receiving a correspoding pong message back from the server. Determine the amont of time between the ping message is send and the pong message arrives.This time is called the round trip time (RTT). Similar to ping programs found in modern OS's except they use the ICMP (Internet Message Control Protocol).

The program should...
1.) Send 10 ping messages to the target server of UDP and determine the RTT and print it out.
2.) Make sure client waits at most 1 second to receive response back. (UDP is unreliable and packet loss may occur)
3.) If the response takes more than a second assume packet loss and print out appropriate message.
