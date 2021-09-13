from sys import argv 
from socket import socket, AF_INET, SOCK_STREAM  
from time import sleep 
 
def main(): 
    if len(argv) > 1:
        host = argv[1] 
    else:
        host = 'localhost' 
    if len(argv) > 2:
        port = int(argv[2])
    else: 
        port = 8080
        tcpSocket = socket(AF_INET, SOCK_STREAM) 
    destino = (host, port) 
    msg = 1 
    tcpSocket.connect(destino) 
    while True:
        tcpSocket.send(bytearray(str(msg), 'utf-8')) 
        msg += 1
        sleep(1)    # 1 segundo 
   
    return 
 
if __name__ == "__main__": 
    main()