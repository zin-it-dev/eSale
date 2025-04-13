from ttkbootstrap import Window, Label, Combobox
from ttkbootstrap.constants import *

from dao import load_categories

root = Window(themename="morph")

root.title("eSale 🛒")
root.geometry("500x300")

title = Label(text="WELCOME TO eSale 🛒!!!", font=("Helvetica", 28))
title.pack(pady=50)

lb = Label(text="Categories:", font=("Helvetica", 14))
lb.pack(pady=10)

categories = Combobox(bootstyle=SUCCESS, values=load_categories())
categories.pack(pady=10)

root.mainloop()
