import tkinter as tk
window=tk.Tk()
window.title('Hesap Makinesi')
windowwidth=window.winfo_screenwidth()//5
windowheight=window.winfo_screenheight()
window.geometry(f'300x400+{windowheight}+{windowwidth}')


def topla():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1+s2))
def cikar():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1-s2))
def carp():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1*s2))
def bol():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1/s2))
def tambol():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1//s2))

def modal():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1%s2))

sonuc=tk.Label(window,background='blue', foreground='white',text='Sonuç',font='Consolas 16 bold',width=30,justify='center')
sonuc.place(x=-50,y=20)
sayi1=tk.Entry(master=window,background='#212121',foreground='#FFCCBC',font='Consolas 16 bold',width=15,justify='right')
sayi1.place(x=70,y=55)

sayi2=tk.Entry(master=window,background='#E64A19',foreground='#FFCCBC',font='Consolas 16 bold',width=15,justify='right')
sayi2.place(x=70,y=85)

tus1=tk.Button(master=window,background='#9E9E9E',foreground='#795548',text=' + ',font='Consolas 16 bold',width=5,command=topla)
tus1.place(x=90,y=130)

tus2=tk.Button(master=window,background='#9E9E9E',foreground='#795548',text=' - ',font='Consolas 16 bold',width=5,command=cikar)
tus2.place(x=90,y=175)

tus3=tk.Button(master=window,background='#9E9E9E',foreground='#795548',text=' * ',font='Consolas 16 bold',width=5,command=carp)
tus3.place(x=90,y=215)

tus4=tk.Button(master=window,background='#9E9E9E',foreground='#795548',text=' / ',font='Consolas 16 bold',width=5,command=bol)
tus4.place(x=90,y=260)
tus4=tk.Button(master=window,background='#9E9E9E',foreground='#795548',text=' // ',font='Consolas 16 bold',width=5,command=tambol)
tus4.place(x=90,y=305)

tus5=tk.Button(master=window,background='#9E9E9E',foreground='#795548',text=' % ',font='Consolas 16 bold',width=5,command=modal)
tus5.place(x=90,y=350)


window.mainloop()

























































window.mainloop()