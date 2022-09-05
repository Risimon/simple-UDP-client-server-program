import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((socket.gethostname(), 1234))

#while True:
#    msg = ''
#full_msg = ''
#while True:
#    msg = s.recv(8)
#    if len(msg) <= 0:
#        break
#    full_msg += msg.decode("ut f-8")

#print(full_msg)

msg = s.recvfrom(1024)
print(msg.decode("utf-8"))
