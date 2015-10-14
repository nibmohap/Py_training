import socket
s=socket.socket()
host=socket.gethostname()
port=1234
s.bind((host,port))
print s.recv(786)
s.send("hii this is clint programe")
s.close
