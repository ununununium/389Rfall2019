"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket

host = "wattsamp.net" # IP address here
port = 1337 # Port here

def execute_cmd(cmd):
    """
        Sockets: https://docs.python.org/3/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """
    print("IMPLEMENT ME")


if __name__ == '__main__':
    while True:
        #Process command from user input
        input = raw_input('> ')
        cmd = input.split()[0]

        if cmd == 'shell':
            print('cmd is shell')
        elif cmd == 'pull':
            print('cmd is pull')
        elif cmd == 'help':
            print('cmd is help')
        elif cmd == 'quit':
            print('cmd is help')
        else:
            print('Invalid Command')
