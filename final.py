#This code will not run on colab as we have used ktinker library
#save any image of name abc.webp in the current directory to add background

from PIL import Image, ImageTk
import csv
import pyttsx3
import tkinter as tk
from tkinter import PhotoImage
import speech_recognition as s 
#create a object of Recognizer
sr=s.Recognizer()
query='hello'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    # time.sleep(3)
    engine.say(audio)
    engine.runAndWait()


def exit_program(root):
    speak("Exiting gracefully")
    root.quit()
    exit(0)

def goMain(root):
    root.destroy()
    first()

def add(English, Alien, root):
    English = English[0:len(English)-1]
    Alien = Alien[0:len(Alien)-1]
    with open('python_project.csv', 'a') as new:  # Added 'newline='' to handle newlines properly
        newword = f"{English},{Alien}\n"
        print(newword)
        new.write(newword)
    goMain(root)

def AddWord(root):
    speak("opening ADD word page")
    root.destroy()
    new_root = tk.Tk()
    new_root.title("Adding new word to dictionary")
    img = Image.open("abc.webp")
    img = img.resize((600, 400), Image.LANCZOS)
    bg_img = ImageTk.PhotoImage(img)
    label = tk.Label(new_root, image=bg_img)
    label.pack(fill="both", expand="yes")
    label1 = tk.Label(new_root, text="Enter English word", font=("Helvetica", 16,'bold'), fg="white", bg="red", width=20, height=2, wraplength=300)
    label1.place(x=190, y=50)
    text = tk.Text(new_root,width=64,height=2,wrap=tk.WORD)
    text.place(x=40,y=120)
    label2 = tk.Label(new_root, text="Enter Alien word", font=("Helvetica", 16,'bold'), fg="white", bg="red", width=20, height=2, wraplength=300)
    label2.place(x=190, y=170)
    text1 = tk.Text(new_root,width=64,height=2,wrap=tk.WORD)
    text1.place(x=40,y=240)

    def adding(root):
        add(text.get("1.0", tk.END),text1.get("1.0",tk.END),root)

    button = tk.Button(new_root,text="Add and Return",fg="white",bg="blue",command=lambda: adding(new_root),width=15)
    button.config(font=('Helvetica',14,'bold'))
    button.config(activebackground="#ff6200")
    button.place(x=220, y=290)
    new_root.mainloop()


def printEngToAlien(output,root): #It shows and speaks the output for english to alien
    text_string = " ".join(output) # converts a list to a string
    root.destroy()
    new_root = tk.Tk()
    new_root.title("English to Alien output")
    img = Image.open("abc.webp")
    img = img.resize((600, 400), Image.LANCZOS)
    bg_img = ImageTk.PhotoImage(img)
    label = tk.Label(new_root, image=bg_img)
    label.pack(fill="both", expand="yes")
    label1 = tk.Label(new_root, text="Translated Alien Output", font=("Helvetica", 16,'bold'), fg="white", bg="yellow", width=20, height=2, wraplength=300)
    label1.place(x=190, y=50)
    text_box = tk.Text(new_root, height=5, width=50)
    text_box.insert("1.0", text_string)
    text_box.place(x=120,y=150)
    button = tk.Button(new_root,text="Return",fg="white",bg="blue",command=lambda: goMain(new_root),width=10)
    button.config(font=('Helvetica',14,'bold'))
    button.config(activebackground="#ff6200")
    button.place(x=240, y=250)
    speak(text_string)
    new_root.mainloop()

def printAlienToEng(output,root): #It shows and speaks the output for english to alien
    text_string = " ".join(output) # converts a list to a string
    root.destroy()
    new_root = tk.Tk()
    new_root.title("Alien To English Output")
    img = Image.open("abc.webp")
    img = img.resize((600, 400), Image.LANCZOS)
    bg_img = ImageTk.PhotoImage(img)
    label = tk.Label(new_root, image=bg_img)
    label.pack(fill="both", expand="yes")
    label1 = tk.Label(new_root, text="Translated English Output", font=("Helvetica", 16,'bold'), fg="white", bg="yellow", width=20, height=2, wraplength=300)
    label1.place(x=190, y=50)
    text_box = tk.Text(new_root, height=5, width=50)
    text_box.insert("1.0", text_string)
    text_box.place(x=120,y=150)
    button = tk.Button(new_root,text="Return",fg="white",bg="blue",command=lambda: goMain(new_root),width=10)
    button.config(font=('Helvetica',14,'bold'))
    button.config(activebackground="#ff6200")
    button.place(x=240, y=250)
    speak(text_string)
    new_root.mainloop()





def convertEngToAlien(data,root): # converts the input english data string to alien output
    words = data.split(' ')
    output = []
    for i in range(0,len(words)):
      with open('python_project.csv','r') as eng:
        englu= csv.reader(eng)
        for line in englu:
            # if words[i][len(words[i])-1]!=' ':
            #     words[i]+=' '
            if i==len(words)-1:
                words[i]+=' '
            if str(line[0]) == str(words[i].lower()):
                output.append((line[1]))
    printEngToAlien(output,root)

def convertAlienToEnglish(data,root): # converts the input Alien data string to English output
    words = data.split(' ')
    output = []
    for i in range(0,len(words)):
      with open('python_project.csv','r') as eng:
        englu= csv.reader(eng)
        for line in englu:
            # if words[i][len(words[i])-1]!=' ':
            #     words[i]+=' '
            if i==len(words)-1:
                words[i]+=' '
            if str(line[1].lower()) == str(words[i].lower()):
                output.append((line[0]))
                print(line[0])
    printAlienToEng(output,root)


def EngToAlien(root):
    speak("opening english to alien page")
    root.destroy()
    new_root = tk.Tk()
    data = tk.StringVar()
    new_root.title("English to Alien")
    img = Image.open("abc.webp")
    img = img.resize((600, 400), Image.LANCZOS)
    bg_img = ImageTk.PhotoImage(img)
    label = tk.Label(new_root, image=bg_img)
    label.pack(fill="both", expand="yes")
    label1 = tk.Label(new_root, text="Enter English sentence", font=("Helvetica", 16,'bold'), fg="white", bg="red", width=20, height=2, wraplength=300)
    label1.place(x=190, y=50)
    text = tk.Text(new_root,width=64,height=5,wrap=tk.WORD)
    text.place(x=40,y=150)

    def printAlien(root):
        convertEngToAlien(text.get("1.0", tk.END),root)

    button = tk.Button(new_root,text="Translate",fg="white",bg="blue",command=lambda: printAlien(new_root),width=10)
    button.config(font=('Helvetica',14,'bold'))
    button.config(activebackground="#ff6200")
    button.place(x=240, y=250)
    new_root.mainloop()

def AlienToEng(root):
    speak("opening alien to english page")
    root.destroy()
    new_root = tk.Tk()
    data = tk.StringVar()
    new_root.title("Alien To English")
    img = Image.open("abc.gif")
    img = img.resize((600, 400), Image.LANCZOS)
    bg_img = ImageTk.PhotoImage(img)
    label = tk.Label(new_root, image=bg_img)
    label.pack(fill="both", expand="yes")
    label1 = tk.Label(new_root, text="Enter Alien sentence", font=("Helvetica", 16,'bold'), fg="white", bg="red", width=20, height=2, wraplength=300)
    label1.place(x=190, y=50)
    text = tk.Text(new_root,width=64,height=5,wrap=tk.WORD)
    text.place(x=40,y=150)

    def printEnglish(root):
        convertAlienToEnglish(text.get("1.0", tk.END),root)

    button = tk.Button(new_root,text="Translate",fg="white",bg="blue",command=lambda: printEnglish(new_root),width=10)
    button.config(font=('Helvetica',14,'bold'))
    button.config(activebackground="#ff6200")
    button.place(x=240, y=250)
    new_root.mainloop()

def first():
    speak("opening home page")
    root = tk.Tk()
    root.title("Hulien Translator")
    img = Image.open("abc.gif")
    img = img.resize((600, 400), Image.LANCZOS)
    bg_img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=bg_img)
    label.pack(fill="both", expand="yes")
    button1 = tk.Button(root,text="English to Alien",fg="white",bg="red",command=lambda:EngToAlien(root),width=20)
    button1.config(font=('Helvetica',20,'bold'))
    button1.config(activebackground="#ff6200")
    button1.place(x=140, y=40)
    button2 = tk.Button(root,text="Alien to English",fg="white",bg="red",command=lambda:AlienToEng(root),width=20)
    button2.config(font=('Helvetica',20,'bold'))
    button2.config(activebackground="#ff6200")
    button2.place(x=140, y=120)
    button3 = tk.Button(root,text="Add new word",fg="white",bg="red",command=lambda:AddWord(root),width=20)
    button3.config(font=('Helvetica',20,'bold'))
    button3.config(activebackground="#ff6200")
    button3.place(x=140, y=200)
    button4 = tk.Button(root,text="Exit",fg="white",bg="red",command=lambda:exit_program(root),width=20)
    button4.config(font=('Helvetica',20,'bold'))
    button4.config(activebackground="#ff6200")
    button4.place(x=140, y=280)
    root.mainloop()

   
if __name__=="__main__":
    first()

