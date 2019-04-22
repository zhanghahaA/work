import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.baidu.com',80))
s.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')
buffer=[]
while 1:
    b=s.recv(1024)
    if b:
        buffer.append(b)
    else:
        break
data=b''.join(buffer)
s.close()
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('baidu.com','wb') as f:
    f.write(html)