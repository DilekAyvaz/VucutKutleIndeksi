import tkinter 
from tkinter import font

window = tkinter.Tk()
window.title("Vücut Kitle Endeksi Hesaplama")
window.config(padx=20, pady=20)

def vki_hesapla(vki):
     
    result_string=f"Your VKİ is:{vki}.you are "
    if vki<18.5:
            return "Zayıf","yellow"
    elif vki<25:
            return "Normal","red"
    elif vki<30:
            return "Fazla Kilolu","blue"
    else:
            return "Obez","pink"


def hesapla_button_clicked():
    kilo=kilo_entry.get()
    boy=boy_entry.get()

    if kilo=="" or boy=="": 
        result_label.config(text="Lütfen kilo ve boy bilgilerini giriniz")
    else:
        try:
            vki=float(kilo)/(float(boy)/100)**2
            kategori,renk =vki_hesapla(vki)
            result_label.config(text=f"Vücut Kitle Endeksi: {vki:.2f}→ {kategori}",fg=renk)

        except:
            result_label.config(text="Lütfen geçerli bir kilo ve boy bilgisi giriniz",fg="white")
            
    
#ui
kilo_label = tkinter.Label(text="Kilo (kg):" , font=("academy engraved let", 22, ))
kilo_label.pack()
kilo_entry = tkinter.Entry()
kilo_entry.pack()

boy_label = tkinter.Label(text="Boy (cm):" , font=("academy engraved let",22))
boy_label.pack()
boy_entry = tkinter.Entry()
boy_entry.pack()

hesapla_button = tkinter.Button(text="Hesapla" ,font=("academy engraved let", 22, ),command=hesapla_button_clicked)
hesapla_button.pack()

result_label = tkinter.Label(text="",font=("academy engraved let",19))
result_label.pack()

                
window.mainloop()



