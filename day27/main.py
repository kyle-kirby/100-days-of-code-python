from tkinter import *

def button_clicked():
    print("I got clicked")
    result = float(input.get()) * 2.2
    label3.config(text=result)


window = Tk()
window.title("Kg(s) to Lbs Converter")
window.minsize(width=100, height=50)
window.config(padx=80, pady=10)

#Label
my_label = Label(text="Kg(s)")
my_label.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Lbs")
label4.grid(column=2, row=1)


#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


#Entry
input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)


window.mainloop()