import tkinter
from socket import *
from threading import *


clients=[]
names=[]


def clientThread(client):
   bayrak=True
   while True:
        try:
            message=client.recv(1024).decode('utf8')
            names.append(message)
            print(message,' bağlandı.')
            bayrak=False
            for c in clients:
                if c!=client:
                    index=clients.index(client)
                    name=names[index]
                    c.send((name+':'+message).encode('utf8'))
        except:
            index=clients.index(client)
            clients.remove(client)
            name=names[index]
            names.remove(name)
            print(name+' çıktı')
            break

server=socket(AF_INET,SOCK_STREAM)
ip='127.0.0.1'
port=5556
server.bind((ip,port))
server.listen()
print('Server dinlemede.')

while True:
    client,address=server.accept()
    clients.append(client)
    print('Bağlnatı yapıldı.',address[0]+':'+str(address[1]))
    thread=Thread(target=clientThread,args=(client,))
    thread.start()