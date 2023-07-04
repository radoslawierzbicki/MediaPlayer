import time
from tkinter import *
from PIL import ImageTk, Image
import screeninfo
from tkinter import messagebox as mb
import json
import runpy
import cv2
import ctypes
import vlc
from threading import Thread
# coding: utf-8

class Quiz:
    global Plik
    Plik = open("wyniki.txt","a",encoding="utf-8")
    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_question()
        self.display_options()
        self.button()
        self.data_size = len(question)
        self.correct = 0
    def display_result(self):
        mb.showinfo("Dziękuję!")
    def check_ans(self, q_no):
            x = self.opt_selected.get()
            Plik.write(str(q_no+1)+"."+str(options[q_no][self.opt_selected.get()-1])[4:len(options[q_no][self.opt_selected.get()-1])])
            return True


    def next_btn(self):
        if(self.opt_selected.get() != 0):
            if self.check_ans(self.q_no):
                self.correct += 1
                self.q_no += 1
            if self.q_no == self.data_size:
                Plik.write("\n")
                Plik.close()
                self.display_result()
            else:
                self.display_question()
                self.display_options()

    def button(self):
        next_button = Button(root, text="Dalej", command=self.next_btn, width = 11, bg= "black", fg = "white", font=("Times New Roman", 20, "bold"))
        next_button.place(relx=0.75, rely=0.6, anchor=CENTER)
        #next_button.place(x=350, y=380)
        quit_button = Button(root, text="Wyjdź", command=root.destroy, width = 11, bg= "black", fg = "white", font=("Times New Roman", 20, "bold"))
        quit_button.place(relx=0.25, rely=0.6, anchor=CENTER)
    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1
    def display_question(self):
            q_no = Label(root, text=question[self.q_no], bg="white", fg="black", width=100, font=('Times New Roman', 18, 'bold'), anchor='w')
            q_no.place(relx=0.5, rely=0.15, anchor=CENTER)
    def display_title(self):
            title = Label(root, text="ANKIETA", width=50, bg="white", fg="black", font=("Times New Roman",20, "bold"))
            title.place(relx=0.5, rely=0.1, anchor=CENTER)
    def radio_buttons(self):
            q_list = []
            y_pos = 200
            while len(q_list)<5:
                radio_btn = Radiobutton(root, text="", variable=self.opt_selected, value=len(q_list)+1, font=("Times New Roman", 17))
                q_list.append(radio_btn)
                radio_btn.place(relx=0.3, y=y_pos)
                y_pos += 40
            return q_list
class MainWindow:

    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_introductrion()
        self.button()
    def run_demo_rec(self):
        runpy.run_path(path_name='C:/Users/asus/Desktop/projekt/Projekt/pythonProject3/demo_rec.py', run_name='__main__')
    def run_demo_send(self):
        runpy.run_path(path_name='C:/Users/asus/Desktop/projekt/Projekt/pythonProject3/demo_send.py', run_name='__main__')


    def create_form(self):
        thread_rec = Thread(target=self.run_demo_rec, daemon=True, name='rec')
        thread_rec.start()
        thread_send = Thread(target=self.run_demo_send, daemon=True, name='send')
        thread_send.start()

        quiz=Quiz()
        introduction.destroy()
        zdj.destroy()


    def button(self):
        next_button = Button(root, text="START", command=self.create_form, width=11, bg="blue", fg="white",font=("Times New Roman", 18, "bold"))
        next_button.place(relx=0.75, rely=0.6, anchor=CENTER)
        quit_button = Button(root, text="Wyjdź", command=root.destroy, width=11, bg="blue", fg="white", font=("Times New Roman", 18, "bold"))
        quit_button.place(relx=0.25, rely=0.6, anchor=CENTER)
    def display_title(self):
        title = Label(root, text="ANKIETA START", width=50, bg="white", fg="black", font=("Times New Roman", 20, "bold"))
        title.place(relx=0.5, rely=0.1, anchor=CENTER)
    def display_introductrion(self):
        global introduction, zdj

        introduction = Label(width=120, height=20, bg="white", fg="black", font=("Times New Roman", 18, "bold" ), text="OPIS BADANIA: Celem testu jest zbadanie postrzegania przez człowieka przesunięć między dźwiękiem a obrazem.\n\n"
                                                                                                                     "- W tym celu zostanie zaprezentowane 5 sekwencji, każda o długości trwania 27 sekund.\n"
                                                                                                                     "- Każda sekwenncja rozpoczyna się 1 sekundowym slajdem z literą A oznaczającym materiał nieopóźniony.\n"
                                                                                                                     "- Po slajdzie następuje prezentacja 10 sekundowego materiału nieopóźnionego.\n"
                                                                                                                     "- Następnie zostanie zaprezentowany 10 sekundowy materiał z przesuniętą ściężką dźwiękową poprzedzony 1 sekundowym slajdem z literą B.\n"
                                                                                                                     "- Dla każdej z pięciu sekwencji występuje 5-sekundowy czas na głosowanie oznaczony na ekranie napisem Vote.\n"
                                                                                                                     "- Dla kazdego pytania należy zaznaczyć odpowiedź i przejść do następnego pytania klikając przycisk Dalej \n"
                                                                                                                     "- W celu rozpoczęcia testu proszę kliknąć przycisk START",justify="left")


        self.img = ImageTk.PhotoImage(Image.open("DSIS.png"))
        zdj = Label(image=self.img)
        zdj.pack()
        zdj.place(relx=0.5, rely=0.7, anchor=CENTER)

        introduction.place(relx=0.5, rely=0.4, anchor=CENTER)


screen = screeninfo.get_monitors()


root = Tk()
if(len(screen) == 1):
    root.geometry("850x500")
else:
    # root.geometry(f"{screen[1].width}x{screen[1].height}-{screen[0].width}+0")
     # root.geometry(f"{screen[1].width}x{screen[1].height}+{screen[0].width}+0")
     # root.geometry(f"{screen[1].width}x{screen[1].height}+0+{screen[0].height}")
    root.geometry(f"{screen[1].width}x{screen[1].height}+0+{screen[0].height}")

root.title("ANKIETA")
root.configure(background="grey")
with open('ankieta.json',encoding='utf-8') as f:
    data = json.load(f)
question = (data['question'])
options = (data['options'])
mainwindow = MainWindow()
root.mainloop()


