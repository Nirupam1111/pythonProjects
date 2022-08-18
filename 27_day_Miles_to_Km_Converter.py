from tkinter import *


def miles_to_km():
    miles=float(myles_input.get())
    km=miles*1.60934
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20,pady=20)

myles_input = Entry(width=7)
myles_input.grid(column=1,row=0)

myles_label = Label(text="Miles")
myles_label.grid(column=2,row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0,row=1)

km_result_label = Label(text="")
km_result_label.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

button = Button(text="Calculate",command=miles_to_km)
button.grid(column=1,row=2)


window.mainloop()
