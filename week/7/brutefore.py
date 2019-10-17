
import re
import operator
import threading
import subprocess
import time

wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

pw_find = False

def create_threads(t, passwords):
	n = len(passwords)
	x = n // t
	m = n % t
	xs = [passwords[i:i+x] for i in range(0, n, x)]
	if m:
		xs[t-1:] = [passwords[-m-x:]]
	assert(sum([len(l) for l in xs]) == n)
	return [threading.Thread(target=run_brute_force, args=(l)) for l in xs]

def run_brute_force(*passwords):
	global pw_find

	for pw in passwords:
		if pw_find:
			break
		else:
			if brute_force(pw.rstrip()):
				pw_find = True

def brute_force(pw):
	cmd = "steghide extract -sf image_dup -xf out.txt"
	returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
	time.sleep(0.5)
	res = subprocess.call(pw,shell=True)
	if "could not extract any data with that passphrase" in res:
		return False
	else:
		return True


if __name__ == '__main__':
	file = open(wordlist,"r")
	passwords = file.readlines()
	thread_list = create_threads(100,passwords)

	for thread in thread_list:
		print('[*] Running thread: {}.'.format(thread.getName()))
		thread.start()

	for thread in thread_list:
		print('[*] Wating for {} to join.'.format(thread.getName()))
		thread.join()
