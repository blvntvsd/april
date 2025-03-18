from tkinter import *
from tkinter import ttk
import tkinter as tk
import random

# Список первоапрельских поздравлений
congratulations = [
    "Поздравляю! Сегодня можно всех разыгрывать!",
    "С 1 апреля! Будь бодр и счастлив!",
    "Сегодня день шуток и смеха!",
    "Улыбнись! Ты только что выиграл в лотерею...\nшутка!",
    "Пусть этот день будет полон смеха и радости!",
    "Если тебе сказали, что ты выиграл миллион,\nпроверь дату!",
    "Осторожно! Сегодня день весёлых ловушек!",
    "С 1 апреля! Шутка – это искусство!",
    "Главное не забыть, что сегодня\n1 апреля!",
    "Смейся, шути и будь счастлив!"
]

# Список ASCII-картинок
ascii_art = [
    '''  
      \\   /  
     -- * --  Весеннее солнце
      /   \\  
    ''',
    ''' 
     (\\_/)
     (o.o)  Весенний зайчик
     (> <) 
    ''',
    '''  
      \\ | /  
       \\|/   Цветущий бутон
       (🌸)  
    '''
]


class App:
    def Button1_Click(self):
        self.Memo1.delete('1.0', END)
        greeting = random.choice(congratulations)
        art = random.choice(ascii_art)
        self.Memo1.insert(END, f"{greeting}\n{art}\n\n")
        
    def Button2_Click(self):
        self.Memo1.delete('1.0', END)
        greeting = random.choice(congratulations)
        art = random.choice(ascii_art)
        self.Memo1.insert(END, f"{self.Edit1.get()}, {greeting}\n{art}\n\n")

    def __init__(self, Window):
        Window.title('1 апреля - поздравления')
        
        AppWidth = 430
        AppHeight = 396
        
        ScreenWidth = Window.winfo_screenwidth()
        ScreenHeight = Window.winfo_screenheight()
        Window.geometry('%dx%d+%d+%d' % (AppWidth, AppHeight, (ScreenWidth - AppWidth) / 2, (ScreenHeight - AppHeight) / 2))
        Window.resizable(width=False, height=False)

        self.Label1 = ttk.Label(Window, text='Введите имя:', anchor='nw')
        self.Label1.place(x=5, y=6, width=100, height=18)
        
        self.Edit1 = ttk.Entry(Window)
        self.Edit1.place(x=8, y=24, width=121, height=21, anchor='nw')
        
        self.Button1 = ttk.Button(Window, text='Случ. поздравление', command=self.Button1_Click)
        self.Button1.place(x=8, y=56, width=130, height=25)
        
        self.Button2 = ttk.Button(Window, text='Перс. поздравление', command=self.Button2_Click)
        self.Button2.place(x=140, y=56, width=130, height=25)
        
        self.Memo1 = Text(Window, wrap=NONE)
        self.Memo1.place(x=8, y=88, width=397, height=283)
        
        self.Memo1YScroll = Scrollbar(command=self.Memo1.yview)
        self.Memo1YScroll.place(x=405, y=88, width=14, height=283)
        
        self.Memo1XScroll = Scrollbar(Window, orient=HORIZONTAL, command=self.Memo1.xview)
        self.Memo1XScroll.place(x=8, y=371, width=397, height=14)
        
        self.Memo1.config(yscrollcommand=self.Memo1YScroll.set, xscrollcommand=self.Memo1XScroll.set)

if __name__ == '__main__':
    Window = tk.Tk()
    app = App(Window)
    Window.mainloop()