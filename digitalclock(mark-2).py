from tkinter import * 
from tkinter.ttk import *
  
# importing strftime function to
# retrieve system's time
from time import strftime
  
# creating tkinter window
hulk = Tk()
hulk.title("HULK's Clock")
  
# This function is used to 
# display time on the label
def clock():
    tick = strftime('%H:%M:%S %p')
    clock_label.config(text = tick)
    clock_label.after(1000, clock)
  
# Styling the label widget so that clock
# will look more attractive
clock_label = Label(hulk, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
  
# Placing clock at the centre
# of the tkinter window
clock_label.pack(anchor = 'center')
clock()
  
mainloop()