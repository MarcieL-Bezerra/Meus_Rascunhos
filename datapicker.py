from tkcalendar import Calendar, DateEntry
import datetime
import tkinter as tk
from tkinter import ttk

def print_sel():
    print(cal.selection_get())
    cal.see(datetime.date(year=2016, month=2, day=5))

def example1():
    
    global cal
    top = tk.Toplevel(root)
    top.title("Selecione a Data")

    
    today = datetime.date.today()

    mindate = datetime.date(year=2021, month=1, day=1)
    maxdate = today + datetime.timedelta(days=365)
    print(mindate, maxdate)

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='pt_BR',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()


def example2():

    top = tk.Toplevel(root)

    cal = Calendar(top, selectmode='none')
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, 'Hello World', 'message')
    cal.calevent_create(date, 'Reminder 2', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

    cal.tag_config('reminder', background='red', foreground='yellow')

    cal.pack(fill="both", expand=True)
    ttk.Label(top, text="Hover over the events.").pack()
    print(cal.selection_get())


#def example3():
    #top = tk.Toplevel(root)

    #ttk.Label(top, text='Selecione a Data').pack(padx=10, pady=10)



root = tk.Tk()
ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='Calendar with events', command=example2).pack(padx=10, pady=10)
#ttk.Button(root, text='DateEntry', command=example3).pack(padx=10, pady=10)

cal = DateEntry(root, width=12, background='darkblue', locale='pt_BR',foreground='white', borderwidth=8, year=2021)
cal.pack(padx=10, pady=10)

print(cal.get())

root.mainloop()