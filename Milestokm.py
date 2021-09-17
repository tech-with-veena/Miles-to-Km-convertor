from tkinter import *
def convertion():
    miles=float(milesinput.get())
    km=miles*1.609
    kmresut.config(text=f"{km}")
window=Tk()
window.title("Miles to Kilometer convertor")
window.config(padx=20,pady=20)
milesinput=Entry(width=7)
milesinput.grid(column=1,row=0)
mileslabel=Label(text="Miles")
mileslabel.grid(column=2,row=0)
isequallabel=Label(text="is equal to")
isequallabel.grid(column=0,row=1)
kmresut=Label(text="0")
kmresut.grid(column=1,row=1)
kmname=Label(text="km")
kmname.grid(column=2,row=1)
calculate=Button(text="Calculate",command=convertion)
calculate.grid(column=1,row=2)





window.mainloop()

