import os
from tkinter import Tk, Menu
from tkinter import ttk
from datetime import date

def Welcome():

   os.popen("python Welcome.py")

def about():

    os.popen("python about.py")

def rules():

    os.popen("python rules.py")

def atr_sl_tp_pl():

    os.popen("python atr_sl_tp_pl.py")

def ml_ds():
    os.popen("python ml_ds.py")

def Analysis_Sheet():
    os.popen("python Analysis_Sheet.py")

def Trading_log():
    os.popen("python Trading_log.py")

# root window
root = Tk()
root.geometry('240x80')
root.resizable(False, False)
#label = Label(root, text="This is the main window")
root.title('PRO TRADING INC')

#zaman = date.today()
date_info = ttk.Label(
    root,
    text= "Instructions for use"+'\n'+"1-Rules"+'\n'+"2-Analysis Sheet"
    +'\n'+"3-ATR-SL-TP-PL"+'\n'+"4-Trading_log",
    font=("Times New Roman", 9))

date_info.place(relx= 0.5, rely= 0.5, anchor='ne')
date_info.pack()

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
Menu_menu = Menu(
    menubar,
    tearoff=0
)

Menu_menu.add_command(
    label='Rules',
    command= rules
)

# add menu items to the File menu
Menu_menu.add_command(
    label='ATR-SL-TP-PL',
    command= atr_sl_tp_pl
)

Menu_menu.add_command(
    label='ML/DS',
    command= ml_ds
)

Menu_menu.add_command(
    label='Trading_log',
    command= Trading_log
)

#Menu_menu.add_command(label='PL')
#Menu_menu.add_command(label='Futures-ELIS')
#Menu_menu.add_separator()

# add a submenu
#sub_menu = Menu(Menu_menu, tearoff=0)
#sub_menu.add_command(label='Intraday')
#sub_menu.add_command(label='Swing')
#sub_menu.add_command(label='Value')

# add the File menu to the menubar
#Menu_menu.add_cascade(
#    label="Spot-Trading",
#    menu=sub_menu
#)

# add Exit menu item
#Menu_menu.add_separator()
Menu_menu.add_command(
    label='Exit',
    command=root.destroy
)


menubar.add_cascade(
    label="Menu",
    menu=Menu_menu,
    underline=0
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(
    label='Welcome',
    command= Welcome
)

help_menu.add_command(
    label='about...',
    command= about
)

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu,
    underline=0
)

analysis_sheet_menu = Menu(
    menubar,
    tearoff=0
)

analysis_sheet_menu.add_command(
    label='Analysis Sheet',
    command= Analysis_Sheet
)

menubar.add_cascade(
    label="Analysis Sheet",
    menu=analysis_sheet_menu,
    underline=0
)
root.mainloop()