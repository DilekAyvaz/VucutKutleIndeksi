import tkinter 

window = tkinter.Tk()
window.title("Vücut Kitle Endeksi Hesaplama")
window.config(padx=20, pady=20)

def hesapla_button_clicked():
    kilo=kilo_entry.get()
    boy=boy_entry.get()

    if kilo=="" or boy=="": 
        result_label.config(text="Lütfen kilo ve boy bilgilerini giriniz")
    else:
        try:
            vki=float(kilo)/(float(boy)/100)**2
            result = f"Vücut Kitle Endeksi: {round(vki, 2)}.you are"
        except:
            result_label.config(text="Lütfen geçerli bir kilo ve boy bilgisi giriniz")
            
    def vki_hesapla(vki):
     
        if vki<18.5:
            return "Zayıf"
        elif vki<25:
            return "Normal"
        elif vki<30:
            return "Fazla Kilolu"
        else:
            return "Obez"
                
    result_label.config(text=vki_hesapla(vki))
    
#ui
kilo_label = tkinter.Label(text="Kilo (kg):" , font=("fredoka one", 16, ))
kilo_label.pack()

kilo_entry = tkinter.Entry()
kilo_entry.pack()

boy_label = tkinter.Label(text="Boy (cm):")
boy_label.pack()

boy_entry = tkinter.Entry()
boy_entry.pack()

hesapla_button = tkinter.Button(text="Hesapla" ,command=hesapla_button_clicked)
hesapla_button.pack()

result_label = tkinter.Label(text="")
result_label.pack()


window.mainloop()