'''
Basit resim düzenleme editörü. tkiner kullanılmıştır.

'''

import tkinter as tk
from PIL import ImageTk,Image,ImageFilter
from tkinter import filedialog,simpledialog
pencere=tk.Tk()
pencere.title('Resim Düzenleme Editörü')
pencere.geometry('1000x1000')

def openimage():
    global img
    file=filedialog.askopenfilename(title='Resim Aç')
    img=Image.open(file,mode='r')
   # resize_image=img.resize((width=panel.width,height=panel.height))
    islenenimg=ImageTk.PhotoImage(img)
    panel.configure(image=islenenimg)
    panel.image=islenenimg
    
    panel.place(x=50,y=50)
    
def resize_image():
    global imgresize2
    w=int(simpledialog.askstring(title='Resmi Boyutlandır', prompt='Yeni Genişlik Değeri:'))
    x,y=img.size
    imgresize=img.resize((w,int(w*y/x)))
    imgresize2=ImageTk.PhotoImage(imgresize)
    panel2.configure(image=imgresize2)
    panel2.image=imgresize2
    panel2.place(x=200,y=200)
def contour_image():
    try:
        imgcontour=imgresize2.filter(ImageFilter.CONTOUR())
    except:
        imgcontour=img.filter(ImageFilter.CONTOUR)
    imgcontour2=ImageTk.PhotoImage(imgcontour)
    panel2.configure(image=imgcontour2)
    panel2.image=imgcontour2
        
        
    
    
btn_open=tk.Button(master=pencere,text='Dosya Aç',command=openimage)
btn_open.place(x=50,y=10)
btn_boyutlandir=tk.Button(master=pencere,text='Boyutlandır',command=resize_image)
btn_boyutlandir.place(x=125,y=10)
btn_kontur=tk.Button(master=pencere,text='Kontur Uygula',command=contour_image)
btn_kontur.place(x=220,y=10)




panel=tk.Label(master=pencere,activebackground='blue',width=600,height=600)


panel2=tk.Label(master=pencere)
#panel.place(x=0,y=0)


pencere.mainloop()




