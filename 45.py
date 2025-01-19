from pydoc import visiblename
from tkinter import *
from tkinter import ttk

def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

root = Tk()
root.geometry("300x250")
root.minsize(200,150)   # минимальные размеры: ширина - 200, высота - 150
root.maxsize(400,250)

root.attributes("-alpha", 0.9)
root.attributes("-toolwindow", False)

txt = Label(root, text="The fragment copy limit has been reached", fg="#FF0000")

clicks = 0 # создаем переменную, где будет храниться кол-во нажатий

def click_button():
    global clicks
    clicks += 1
    # изменяем текст на кнопке
    btn["text"] = f"{clicks} fragments were copied."
    # Если условие выполняется, кнопку уже больше нельзя нажать
    if clicks >= 10:
        btn["state"] = "disabled"
        txt.pack(anchor="s")

btn = ttk.Button(text="Copy", command=click_button)
btn.pack(#padx=35,
         #pady=20,
         #ipadx=10,
         #ipady=10,
         #side=BOTTOM,
         #fill=X
    )
btn.place(relx=.5, rely=.4, anchor="n", relwidth=.6, relheight=0.25)
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

root.title("TextEditor")
icon = PhotoImage(file = "textedit.png")
root.iconphoto(False, icon)
root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()