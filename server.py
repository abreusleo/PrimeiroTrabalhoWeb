from sys import argv, exit 
from socket import socket, AF_INET, SOCK_STREAM 
import os

def main(): 
    bufferSize = 1024 
    host = 'localhost' 
    if len(argv) > 1:
        port = int(argv[1])
    else: 
        port = 8080     
    tcpSocket = socket(AF_INET, SOCK_STREAM)     
    origem = (host, port)     
    tcpSocket.bind(origem)     
    tcpSocket.listen(1)    
    print("Servidor pronto", host, port) 
    while(True):         
        con, cliente = tcpSocket.accept() 
        pid = os.fork()
        if pid == 0:             
            tcpSocket.close() 
            print("Servidor connectado com ", cliente) 
            while True:                 
                msg = con.recv(bufferSize) 
                if not msg: 
                    break 
                print(cliente, msg)
            con.close() 
            exit()         
        else: 
            con.close() 
    return
    
if __name__ == "__main__": 
    main()