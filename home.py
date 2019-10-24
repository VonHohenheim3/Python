from tkinter import *
window = Tk()

btcad = Button(window, width=30, bg='red' , activebackground='white', text='tomanocu')
btcad.place(x=480, y=250)

window.configure(bg='black')
window.geometry('1280x768+300+300')
window.title('title')
window.mainloop()

