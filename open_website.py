import webbrowser
from tkinter import *

root = Tk()

root.title('Web Brouser')

root.geometry('300x200')

def myportfolio():
    webbrowser.open('https://no-zz.com')
def google():
    webbrowser.open('https://www.google.com')
    
myportfolio = Button(root, text='visit my portfolio', command=myportfolio, highlightbackground='black').pack(pady=20)
mygoogle = Button(root, text='open Google', command=google, highlightbackground='black').pack(pady=20)

root.mainloop()

