import tkinter as tk

from tkinter import messagebox
pencere=tk.Tk()
pencere.title('Yapılacaklar Listesi - To Do')
pencere.geometry('600x600')

frame_ust=tk.Frame(pencere)
frame_ust.pack(side='top')
frame_alt=tk.Frame(pencere)
frame_alt.pack(side='top')


box=tk.Listbox(master=frame_ust,width=40,height=10)
box.pack(side='left')
box_null=tk.Listbox(master=frame_ust,width=40,height=10)
box_null.pack(side='left')

giris=tk.Entry(master=frame_alt,width=40,font='Consolas 16',fg='red')
giris.pack()
giris.focus()

def gorev_ekle(event=None):
    if len(giris.get().strip())>0: #boşlukları basma
        box.insert(tk.END, giris.get())
        giris.delete(0, tk.END)
    else:
        messagebox.showwarning('Null To Do','Please enter the to do item.')
def gorev_sil():
    if len(box.curselection())>0:
        index=box.curselection()[0]
        result = messagebox.askyesno('Delete To Do Item','Are you sure to delete item')
        if result:
            box.delete(index)
def gorev_kaydet():
    try:
        dosya = open('yaz.txt', 'w', encoding='utf-8')
        gorevler = box.get(0, tk.END)
        dosya.writelines('\n'.join(gorevler))
        dosya.close()
        messagebox.showinfo('Succes','You can saved.')
    except:
        messagebox.showerror('File Writing Error','You cannot save the document')
#görevleri okuyup listbox a aktar
def gorev_yukle(event=None):
    dosya=open('yaz.txt','r',encoding='utf-8')
    gorevler=dosya.readlines()
    box_null.delete(0,tk.END)
    for gorev in gorevler:
        gorev=gorev.replace('\n','')
        box_null.insert(tk.END,gorev)

btn_bekle=tk.Button(master=frame_alt,text='Görev Ekle',width=40,command=gorev_ekle)
btn_bekle.pack()

btn_sil=tk.Button(master=frame_alt,text='Görev Sil',width=40,command=gorev_sil)
btn_sil.pack()

btn_kaydet=tk.Button(master=frame_alt,text='Görev Kaydet',width=40,command=gorev_kaydet)
btn_kaydet.pack()
btn_yukle=tk.Button(master=frame_alt,text='Görevleri Yükle',width=40,command=gorev_yukle)
btn_yukle.pack()

pencere.bind('<Return>',gorev_ekle)
pencere.bind('<Control-s>',gorev_yukle)

pencere.mainloop()
