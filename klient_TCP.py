 
import socket

target_host ="www.google.pl"
target_port=80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send("GET\HTTP\1.1\R\nHOST:goofle.com\r\n")

response=client.recv(4000)
print(response.decode())
client.close()
