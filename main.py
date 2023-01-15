from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=400, height=300)
window.config(padx=50, pady=50)


def button_clicked():
    num = float(input.get())
    conversion = 1.609344
    total = num * conversion
    label3["text"] = total



input = Entry(width=10)
input.insert(END, string="0")
input.grid(row=0, column=1)

label = Label(text="Miles", font=("Arial", 12))
label.grid(row=0, column=2)

label2 = Label(text="is equal to", font=("Arial", 12))
label2.grid(row=1, column=0)

label3 = Label(text="0", font=("Arial", 12, "bold"))
label3.grid(row=1, column=1)

label4 = Label(text="Kilometres", font=("Arial", 12))
label4.grid(row=1, column=2)

button = Button(text="Click me", command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()