import tkinter as tk
from playsound import playsound
pencere=tk.Tk()
pencere.title('Piyano Çalma Programı')
pencere.geometry('520x520')

def do_cal(event=None):
    btn_do.config(relief=tk.SUNKEN)
    playsound('nota-do.wav',False)
    btn_do.after(50,lambda:btn_do.config(relief=tk.RAISED))

def re_cal(event=None):
    btn_re.config(relief=tk.SUNKEN)
    playsound('nota-re.wav',False)
    btn_re.after(50,lambda :btn_re.config(relief=tk.RAISED))

def mi_cal(event=None):
    btn_mi.config(relief=tk.SUNKEN)
    playsound('nota-mi.wav',False)
    btn_mi.after(50,lambda:btn_mi.config(relief=tk.RAISED))

def fa_cal(event=None):
    btn_fa.config(relief=tk.SUNKEN)
    playsound('nota-fa.wav',False)
    btn_fa.after(50,lambda:btn_fa.config(relief=tk.RAISED))
def sol_cal(event=None):
    btn_sol.config(relief=tk.SUNKEN)
    playsound('nota-sol.wav',False)
    btn_sol.after(50, lambda: btn_sol.config(relief=tk.RAISED))
def la_cal(event=None):
    btn_la.config(relief=tk.SUNKEN)
    playsound('nota-la.wav',False)
    btn_la.after(50, lambda: btn_la.config(relief=tk.RAISED))

def si_cal(event=None):
    btn_si.config(relief=tk.SUNKEN)
    playsound('nota-si.wav',False)
    btn_si.after(50, lambda: btn_si.config(relief=tk.RAISED))

def ddo_cal(event=None):
    btn_do.config(relief=tk.SUNKEN)
    playsound('nota-do.wav',False)
    btn_do.after(50, lambda: btn_do.config(relief=tk.RAISED))

def otomatil_cal(event=None):
    f=open('nota.txt')
    s=f.readlines()
    def notalar(i):
        if i<len((s)):
            satir=s[i].split()
            def nota(j):
                if j<len(satir):
                    if satir[j].lower()=='do':
                        do_cal()
                    if satir[j].lower()=='re':
                        re_cal()
                    if satir[j].lower()=='mi':
                        mi_cal()
                    if satir[j].lower()=='fa':
                        fa_cal()
                    if satir[j].lower()=='sol':
                        sol_cal()
                    if satir[j].lower()=='la':
                        la_cal()
                    if satir[j].lower()=='si':
                        si_cal()
                    j=j+1
                    pencere.after(200,lambda :nota(j))
            nota(0)
            i=i+1
            pencere.after(200*len(satir)+1000,lambda :notalar(i))
            notalar(0)




btn_do=tk.Button(pencere,text='DO',font='Verdana 14 bold',bg='white',fg='black',height=8,width=3,command=do_cal)
btn_do.place(x=50,y=20)

btn_re=tk.Button(pencere,text='RE',font='Verdana 14 bold',bg='white',fg='black',height=8,width=3,command=re_cal)
btn_re.place(x=110,y=20)

btn_mi=tk.Button(pencere,text='Mİ',font='Verdana 14 bold',bg='white',fg='black',height=8,width=3,command=mi_cal)
btn_mi.place(x=170,y=20)

btn_fa=tk.Button(pencere,text='FA',font='Verdana 14 bold',bg='white',fg='black',height=8,width=3,command=fa_cal)
btn_fa.place(x=230,y=20)

btn_sol=tk.Button(pencere,text='SOL',font='Verdana 14 bold',bg='white',fg='black',height=8,width=3,command=sol_cal)
btn_sol.place(x=290,y=20)

btn_la=tk.Button(pencere,text='LA',font='Verdana 14 bold',bg='white',fg='black',height=8,width=3,command=la_cal)
btn_la.place(x=350,y=20)

btn_si=tk.Button(pencere,text='SI',font='Verdana 14 bold',bg='white',fg='black',height=8,width=3,command=si_cal)
btn_si.place(x=410,y=20)

btn_ddo=tk.Button(pencere,text='Otomatik Çal',font='Verdana 14 bold',bg='white',fg='black',height=1,width=12,command=do_cal)
btn_ddo.place(x=180,y=300)
pencere.bind('<a>',do_cal)
pencere.bind('<s>',re_cal)
pencere.bind('<d>',mi_cal)
pencere.bind('<f>',fa_cal)
pencere.bind('<g>',sol_cal)
pencere.bind('<h>',la_cal)
pencere.bind('<j>',do_cal)


pencere.mainloop()