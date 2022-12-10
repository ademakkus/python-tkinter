from socket import *
from threading import *
from tkinter import *

client=socket(AF_INET,SOCK_STREAM)
ip='127.0.0.1'
port=55556

client.connect((ip,port))

pencere=Tk()
pencere.title('Bağlandı :'+ip+' : '+str(port))

messages=Text(pencere,width=50)
messages.grid(row=0,column=0,padx=10,pady=10)

yourmessage=Entry(pencere,width=50)
yourmessage.focus()
yourmessage.grid(row=1,column=0,pady=10,padx=10)
yourmessage.insert(0,'İsminiz')
yourmessage.select_range(0,END)
def sendMessage():
    clientMessage=yourmessage.get()
    messages.insert(END,'\n'+'Sen : '+clientMessage)
    client.send(clientMessage.encode('utf8'))
    yourmessage.delete(0,END)
bmessageGonder=Button(pencere,text='Gönder',width=20,command=sendMessage)
bmessageGonder.grid(row=2,column=0,padx=10,pady=10)

def recvMessage():
    while True:
        serverMessage=client.recv(1024).decode('utf8')
        messages.insert(END,'\n'+serverMessage)
recvThread=Thread(target=recvMessage)
recvThread.daemon=True
recvThread.start()
pencere.mainloop()