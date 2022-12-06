import random
import tkinter as tk
kalansure = 30
renkler = ['black-siyah', 'white-beyaz', 'red-kırmızı', 'green-yeşil', 'blue-mavi', 'yellow-sarı', 'brown-kahverengi', 'orange-turuncu', 'grey-gri', 'maroon-bordo', 'purple-mor', 'pink-pembe']
puan=0
def gerisayim(event=None):
    global kalansure
    if kalansure > 0:
      kalansure -= 1
      zamanLabel.config(text='Kalan Süre:'+str(kalansure))
      zamanLabel.after(1000, gerisayim)

def sonrakiRenk():
    global puan
    if kalansure>0:
        giris.focus()
        if giris.get().lower()==renkler[1][renkler[1].find('-')+1:].lower():
            puan += 1
        giris.delete(0,tk.END)
        random.shuffle(renkler)
        yazi.config(fg=str(renkler[1][:renkler[1].find('-')]),text=str(renkler[0][renkler[0].find('-')+1:]))
        puanLabel.config(text='Puan : '+str(puan))
def basla(event=None):
    if kalansure==30:
        gerisayim()
    sonrakiRenk()
pencere=tk.Tk()
pencere.title('Renk Oyunu')
genislik=pencere.winfo_screenwidth()//4
yukseklik=pencere.winfo_screenheight()//2
pencere.geometry(f'600x400+{genislik}+{yukseklik}')

bilgiLabel=tk.Label(master=pencere,fg='red',text='Yazının Rengini ',font=('Embrima 16'))
bilgiLabel.pack()

puanLabel=tk.Label(master=pencere,fg='green',text='Başlamak için Enter a basın ',font=('Embrima 16'))
puanLabel.pack()

zamanLabel=tk.Label(master=pencere,fg='blue',text=f'Kalan Süre:{kalansure}',font=('Embrima 16'))
zamanLabel.pack()

yazi=tk.Label(master=pencere,font=('Helvetica 40'))
yazi.pack()
giris=tk.Entry(pencere,bg='#3e2723',fg='#efebe9',font=('Consolas 18'),width=35)
giris.pack()
giris.focus()
giris.delete(0,tk.END)
#tuşa basılmasını kontrol etme.
pencere.bind('<Return>',basla)

#en altta
pencere.mainloop()