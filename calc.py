from pydoc import visiblename
from tkinter import *
from tkinter import ttk

def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

root = Tk()
root.geometry("348x353")
root.minsize(348,353)   # минимальные размеры: ширина - 200, высота - 150
root.maxsize(800,800)

root.attributes("-alpha", 0.9)
root.attributes("-toolwindow", True)

entry = Entry(root, font=("Arial", 14), fg="black", bg="lightyellow")
entry.grid(row=0, column=0, columnspan=3, ipadx=11, ipady=6, padx=5, pady=3)

cancel = ttk.Button(text="Cancel")
cancel.grid(row=0, column=3, ipadx=1, ipady=11, padx=5, pady=3)

divis = ttk.Button(text="÷")
divis.grid(row=4, column=3, ipadx=1, ipady=20, padx=5, pady=3)

multi = ttk.Button(text="*")
multi.grid(row=3, column=3, ipadx=1, ipady=20, padx=5, pady=3)

subtr = ttk.Button(text="-")
subtr.grid(row=2, column=3, ipadx=1, ipady=20, padx=5, pady=3)

addit = ttk.Button(text="+")
addit.grid(row=1, column=3, ipadx=1, ipady=20, padx=5, pady=3)

btn1 = ttk.Button(text="1")
btn1.grid(row=1, column=0, ipadx=0, ipady=20, padx=1, pady=5)

btn3 = ttk.Button(text="4")
btn3.grid(row=2, column=0, ipadx=0, ipady=20, padx=5, pady=5)

btn4 = ttk.Button(text="7")
btn4.grid(row=3, column=0, ipadx=0, ipady=20, padx=5, pady=5)

btn5 = ttk.Button(text="2")
btn5.grid(row=1, column=1, ipadx=0, ipady=20, padx=5, pady=5)

btn6 = ttk.Button(text="5")
btn6.grid(row=2, column=1, ipadx=0, ipady=20, padx=5, pady=5)

btn7 = ttk.Button(text="8")
btn7.grid(row=3, column=1, ipadx=0, ipady=20, padx=5, pady=5)

btn8 = ttk.Button(text="3")
btn8.grid(row=1, column=2, ipadx=0, ipady=20, padx=5, pady=5)

btn9 = ttk.Button(text="6")
btn9.grid(row=2, column=2, ipadx=0, ipady=20, padx=5, pady=5)

btn10 = ttk.Button(text="9")
btn10.grid(row=3, column=2, ipadx=0, ipady=20, padx=5, pady=5)

btn11 = ttk.Button(text="0")
btn11.grid(row=4, column=0, ipadx=0, ipady=20, padx=5, pady=5)

btn12 = ttk.Button(text=",")
btn12.grid(row=4, column=1, ipadx=0, ipady=20, padx=5, pady=5)

btn12 = ttk.Button(text="=")
btn12.grid(row=4, column=2, ipadx=0, ipady=20, padx=5, pady=5)




#btn.place(relx=.5, rely=.4, anchor="n", relwidth=.6, relheight=0.25)
# устанавливаем параметр text

def print_info(widget, depth=0):
    widget_class = widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("   " * depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth + 1)


root.update()  # обновляем информацию о виджетах

print_info(root)

root.title("Таблица степеней")
icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)
root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()