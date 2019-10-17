
import re
import operator
import threading
import subprocess
import time
import os


wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file




def brute_force(pw):
	cmd = "steghide extract -sf image_dup -xf out.txt -p " + pw


	# result = subprocess.run(cmd, stdout=subprocess.PIPE)  # returns the exit code in unix
	# print(result.stdout)
	# if "could not extract any data with that passphrase" in str(returned_value):
	# 	return False
	# else:
	# 	return True


if __name__ == '__main__':
	file = open(wordlist,"r")
	passwords = file.readlines()

	for pw in passwords:
		print("Trying: " + str(pw))
		brute_force(pw)
		break
		# if brute_force(pw):
		# 	print("PASSWORD GET: " + pw )
		# 	break
