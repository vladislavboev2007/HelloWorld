from pydoc import visiblename
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

from numpy.f2py.rules import options


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

el = []

def create_frame(label_text):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    # добавляем на фрейм метку
    label = ttk.Label(frame, text=label_text)
    label.pack(anchor=NW)
    # добавляем на фрейм текстовое поле
    entry = ttk.Entry(frame, width=60)
    entry.pack(anchor=NW)
    el.append(entry)
    # возвращаем фрейм из функции
    return frame

def send():
    t = f'''
{el[0].get()}
{el[1].get()}
{el[2].get()}
{el[3].get()}
    '''
    showinfo(title="Анкета отправлена.", message=t)


root = Tk()
root.geometry("348x353")
root.minsize(348,353)   # минимальные размеры: ширина - 200, высота - 150
#root.maxsize(800,800)

root.attributes("-alpha", 0.9)
root.attributes("-toolwindow", True)


name_frame = create_frame("Введите ФИО")
name_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

email_frame = create_frame("Введите email")
email_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

email_frame = create_frame("Введите номер телефона")
email_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

email_frame = create_frame("Введите адрес")
email_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

button = ttk.Button(text="Отправить", command=send)
button.pack()


txt = ttk.Label(text="")
txt.pack()

root.title("VolgaExpress")
icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)
root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()