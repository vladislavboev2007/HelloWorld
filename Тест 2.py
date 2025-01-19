from pydoc import visiblename
from tkinter import *
from tkinter import ttk

from sympy.printing.pretty.pretty_symbology import center


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

root = Tk()
root.geometry("348x353")
root.minsize(348,353)   # минимальные размеры: ширина - 200, высота - 150
#root.maxsize(800,800)

root.attributes("-alpha", 0.9)
root.attributes("-toolwindow", True)

def answer():
    if selected_language.get() == "Москва":
        info["text"] = "Ответ верный"
    else:
        info["text"] = "Ответ неверный"


position = {"padx": 6, "pady": 6, "anchor": CENTER}
languages = ["Санкт-Петербург", "Москва", "Новосибирск", "Казань"]

selected_language = StringVar()  # по умолчанию ничего не выборанно

header = ttk.Label(text="Какая столица России?")
header.pack(**position)

def select():
    header.config(text=f"Выбран {selected_language.get()}")


for lang in languages:
    lang_btn = ttk.Radiobutton(text=lang, value=lang, variable=selected_language, command=select, width=20)
    lang_btn.pack(**position)

info = ttk.Label(text="")
info.pack()

ButAns = ttk.Button(text="Ответить", command=answer)
ButAns.pack()


languagesPhoto = [
    {"name": "Тыва", "img": PhotoImage(file="./Tyiva.png")},
    {"name": "Россия", "img": PhotoImage(file="./Russia.png")},
    {"name": "Крым", "img": PhotoImage(file="./Crimea.png")},
    {"name": "Бурятия", "img": PhotoImage(file="./Buryatiya.png")}
]

langPhoto = StringVar(value=languagesPhoto[0]["name"])  # по умолчанию будет выбран элемент с value=python

header = ttk.Label(textvariable=langPhoto)
header.pack(**position)

for l in languagesPhoto:
    btn = ttk.Radiobutton(value=l["name"], text=l["name"], variable=langPhoto, image=l["img"], compound="top")
    btn.pack(**position)

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