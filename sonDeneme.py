class App (object):
    def __init__(self):
        #Arayüzün değişkenleri ve tanımları
        self.root=Tk()
        self.root.geometry("300x300")
        self.variable=StringVar()
        #Burada ki i yerine stringimiz gelecek,
        #i olarak kalırsa değişken ismi daha kolay olur
        self.i=0
        #Etiketi tanımlıyor
        self.your_label=Label(self.root,textvariable=self.variable)

    def grid(self):
        #Etiketi yerleştiriyor, istenirse butonda konulabilir sonra
        self.your_label.pack()

    def update_label(self):
        #Denemek için i döngüyle arttırılıyor
        self.i=self.i+1
        #Stringe çeviriyor datayı
        self.variable.set(str(self.i))
        self.root.after(20,self.update_label)

        #Dosyayı açıp, stringi append ediyor
        with open("telemetry.txt", "a") as file:
            file.write(str(self.i))
            file.write("\n")

        print("i",self.i) #Denemek için yazdım silinebilir

    def run(self):
        #20 milisaniye bir güncelliyor, arayüzü açık tutuyor.
        self.grid()
        self.root.after(20,self.update_label)
        self.root.mainloop()

if __name__=='__main__':
    #Arayüzü başlatıyor ve sınıfın işi bitince, açtığı dosyayı kapatıyor
    from tkinter import *
    App().run()
    collectedData.close()

    #Oluşturduğu dosyayı PycharmProjects'e açıcak,
    #path koyarak başka bir yere de açabiliriz