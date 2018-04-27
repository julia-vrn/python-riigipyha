from tkinter import *
import calendar


#класс для отрисовки канвы (канва+изображение)
class CanvasClass:
    def __init__(self, r, c, image):
        self.can = Canvas(width=100, height=100)
        self.can.grid(row=r, column=c)
        self.can.create_image(0, 0, image=image, anchor=NW)


#класс для создания радио-кнопки
class RdB:
    def __init__(self, master, stext, r, c, val):
        global vrb
        self.rdb = Radiobutton(master, text=stext, variable=vrb, value=val)
        self.rdb.grid(row=r, column=c)


def get_month(year, month):
    c = calendar.month(year, month)
    return c


def inserlbl(var, m, message):
    kuu = Label(text="Kuu", font="Courier 10")
    kuu.grid(row=10, column=0, columnspan=2)
    pyha = Label(text="Riigipüha", font="Courier 10")
    pyha.grid(row=10, column=2, columnspan=2)
    if var == m:
        c = get_month(2018, m)
        calb = Label(text=c, font="Courier 10")
        calb.grid(row=11, column=0, columnspan=2)
        txt = Text(width=22, height=9, font="Courier 8", wrap=WORD)
        txt.grid(row=11, column=2, columnspan=2)
        txt.insert(INSERT, message)
        txt.config(state=DISABLED)


root = Tk()
calendar_lab = Label(text="Riigipühad 2018", font="Courier 30")
calendar_lab.grid(row=0, column=0, columnspan=4, sticky='we')


vrb = IntVar()

january = PhotoImage(file="january.png")
jan = CanvasClass(1, 0, january)
janrb = RdB(root, "jaanuar", 2, 0, 1)
message_jan = "E 01. jaanuar 2018- UUSAASTA"


february = PhotoImage(file="february.png")
feb = CanvasClass(1, 1, february)
febrb = RdB(root, "veebruar", 2, 1, 2)
message_feb = "L 24. veebruar 2018 - Iseseisvuspäev, Eesti Vabariigi aastapäev"

march = PhotoImage(file="march.png")
mar = CanvasClass(1, 2, march)
marrb = RdB(root, "märts", 2, 2, 3)
message_mar = "R 30. märts 2018 - Suur Reede"

april = PhotoImage(file="april.png")
apr = CanvasClass(1, 3, april)
aprrb = RdB(root, "aprill", 2, 3, 4)
message_apr = "P 01. aprill 2018 - Ülestõusmispühade 1. püha"

may = PhotoImage(file="may.png")
my = CanvasClass(3, 0, may)
myrb = RdB(root, "mai", 4, 0, 5)
message_may = "T 01. mai 2018 - Kevadpüha"

june = PhotoImage(file="june.png")
jun = CanvasClass(3, 1, june)
junrb = RdB(root, "juuni", 4, 1, 6)
message_jun = "P 24. juuni 2018 - Jaanipäev"

july = PhotoImage(file="july.png")
jul = CanvasClass(3, 2, july)
julrb = RdB(root, "juuli", 4, 2, 7)
message_jul = ""

august = PhotoImage(file="august.png")
aug = CanvasClass(3, 3, august)
augrb = RdB(root, "august", 4, 3, 8)
message_aug = "E 20. august 2018 - Taasiseseisvumispäev"

september = PhotoImage(file="september.png")
sept = CanvasClass(5, 0, september)
septrb = RdB(root, "september", 6, 0, 9)
message_sept = ""

october = PhotoImage(file="october.png")
oct = CanvasClass(5, 1, october)
octrb = RdB(root, "oktoober", 6, 1, 10)
message_oct = ""

november = PhotoImage(file="november.png")
nov = CanvasClass(5, 2, november)
novrb = RdB(root, "november", 6, 2, 11)
message_nov = ""

december = PhotoImage(file="december.png")
dec = CanvasClass(5, 3, december)
decrb = RdB(root, "detsember", 6, 3, 12)
message_dec = "E 24. detsember 2018 - Jõululaupäev \n T 25. detsember 2018 - Esimene jõulupüha \n K 26. detsember 2018 - Teine jõulupüha"


def check_radio(event):
    inserlbl(vrb.get(), 1, message_jan)
    inserlbl(vrb.get(), 2, message_feb)
    inserlbl(vrb.get(), 3, message_mar)
    inserlbl(vrb.get(), 4, message_apr)
    inserlbl(vrb.get(), 5, message_may)
    inserlbl(vrb.get(), 6, message_jun)
    inserlbl(vrb.get(), 7, message_jul)
    inserlbl(vrb.get(), 8, message_aug)
    inserlbl(vrb.get(), 9, message_sept)
    inserlbl(vrb.get(), 10, message_oct)
    inserlbl(vrb.get(), 11, message_nov)
    inserlbl(vrb.get(), 12, message_dec)


btn = Button(text="Vaata riigipühi")
btn.grid(row=7, column=0, columnspan=4)
btn.bind("<Button-1>", check_radio)

root.minsize(width=415, height=460)
root.maxsize(width=415, height=680)
root.resizable(0, 0)

root.mainloop()

