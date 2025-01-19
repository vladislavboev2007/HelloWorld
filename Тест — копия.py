from pydoc import visiblename
from tkinter import *
from tkinter import ttk


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

root = Tk()
root.geometry("348x353")
root.minsize(348,353)   # минимальные размеры: ширина - 200, высота - 150
#root.maxsize(800,800)

root.attributes("-alpha", 0.9)
root.attributes("-toolwindow", True)

lists = [IntVar(), IntVar(), IntVar()]

def select():
    rsg = 0
    for i in lists:
        rsg += i.get()
    result = f"Выбрано {rsg}: "
    if lists[0].get() == 1:
        result = f"{result} Python"
    if lists[1].get() == 1:
        result = f"{result} JavaScript"
    if lists[2].get() == 1:
        result = f"{result} Java"
    languages.set(result)

def answer():
    if lists[0].get() == 1 and lists[2].get() == 1 and lists[1].get() == 0:
        info["foreground"] = "Green"
        info["text"] = "Ответ правильный. "

        ButAns["state"] = "disabled"
    elif (lists[0].get() == 1 and lists[2].get() == 0 and lists[1].get() == 0) or lists[0].get() == 0 and lists[2].get() == 1 and lists[1].get() == 0:
        info["foreground"] = "#eb9c00"
        info["text"] = "Ответ частично верный"
    else:
        info["foreground"] = "Red"
        info["text"] = "Ответ неверный"

position = {"padx": 6, "pady": 6, "anchor": N}

question_label = ttk.Label(text="Какой язык программирования мы будем изучать на 3 курсе?")
question_label.pack(**position)

languages = StringVar()
languages_label = ttk.Label(textvariable=languages)
languages_label.pack(**position)


#lists[0] = IntVar()
python_checkbutton = ttk.Checkbutton(text="Python", variable=lists[0], command=select, width=10)
python_checkbutton.pack(**position)

#lists[1] = IntVar()
javascript_checkbutton = ttk.Checkbutton(text="JavaScript", variable=lists[1], command=select, width=10)
javascript_checkbutton.pack(**position)

#Java = IntVar()
java_checkbutton = ttk.Checkbutton(text="Java", variable=lists[2], command=select, width=10)
java_checkbutton.pack(**position)

info = ttk.Label()
info.pack()

ButAns = ttk.Button(text="Ответить", command=answer)
ButAns.pack()

print(lists[0].get() + lists[1].get() + lists[2].get())

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