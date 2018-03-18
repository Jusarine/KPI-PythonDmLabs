import random
from tkinter import *
from tkinter import messagebox

# -------------------------------------------------------------------------------------------------------------1
# -------------------------------------------------------------------------------------------------------------
import os

import D, Simple_D, Z
import myZ


def open_window1():
    global root, ent1, ent2, ent3, ent4, ent5, ent6, ent7, ent11, point
    root = Tk()
    root.title("Window 1")
    root.attributes('-topmost', True)
    root.geometry("405x290")

    main_menu = Menu(root)
    root.config(menu=main_menu)

    open_menu = Menu(main_menu, tearoff=0)
    open_menu.add_command(label="Assignment", command=show_assignment)
    open_menu.add_command(label="Window 2", command=open_window2)
    open_menu.add_command(label="Window 3", command=open_window3)
    open_menu.add_command(label="Window 4", command=open_window4)
    open_menu.add_command(label="Window 5", command=open_window5)

    main_menu.add_cascade(label="Open", menu=open_menu)

    about_menu = Menu(main_menu, tearoff=0)
    about_menu.add_command(label="About", command=print_info)
    main_menu.add_cascade(label="About", menu=about_menu)

    exit_menu = Menu(main_menu, tearoff=0)
    exit_menu.add_command(label="Exit", command=root.destroy)
    main_menu.add_cascade(label="Exit", menu=exit_menu)

    Label(root, text="The number of elements:").place(x=40, y=10)
    Label(root, text="A:").place(x=15, y=40)
    Label(root, text="B:").place(x=15, y=70)
    Label(root, text="C:").place(x=15, y=100)
    ent1 = Entry(root, width=20)
    ent2 = Entry(root, width=20)
    ent3 = Entry(root, width=20)
    ent1.place(x=40, y=40)
    ent2.place(x=40, y=70)
    ent3.place(x=40, y=100)

    Label(root, text="The sets:").place(x=240, y=10)
    ent4 = Entry(root, width=20)
    ent5 = Entry(root, width=20)
    ent6 = Entry(root, width=20)
    ent4.place(x=215, y=40)
    ent5.place(x=215, y=70)
    ent6.place(x=215, y=100)

    Label(root, text="Enter range for sets:").place(x=80, y=170)
    ent7 = Entry(root, width=20)
    ent7.place(x=215, y=165)

    Label(root, text="Enter universal set:").place(x=15, y=240)
    ent11 = Entry(root, width=20)
    ent11.place(x=140, y=240)

    point = IntVar()
    rad1 = Radiobutton(root, text="Generate sets", variable=point, value=1, command=init1)
    rad2 = Radiobutton(root, text="Enter sets manually", variable=point, value=2, command=init2)
    point.set(2)
    init2()
    rad1.place(x=15, y=150)
    rad2.place(x=15, y=130)

    but1 = Button(root, text="Save sets", command=save_sets)
    but1.place(x=45, y=200)

    but2 = Button(root, text="Clear", command=clear)
    but2.place(x=140, y=200)

    but3 = Button(root, text="Remove existing files", command=remove_existing_files)
    but3.place(x=210, y=200)
    root.mainloop()

# -------------------------------------------------------------------------------------------------------------


def remove_existing_files():
    if os.path.exists("d.txt"):
        os.remove("d.txt")
    if os.path.exists("z.txt"):
        os.remove("z.txt")
    if os.path.exists("simple_d.txt"):
        os.remove("simple_d.txt")


def print_info():
    g = 72
    n = 4
    var = (n + g % 60) % 30 + 1
    messagebox.showinfo("About", "Full name: Gladka Tatyana Anatoliivna\nGroup: IV-72\nList number: 4\nVariant: " + str(var))


def set_to_str(s):
    if s == set():
        return '{}'
    else:
        return str(s)


def rand_set_entry(entry, n, l, r):
    i = 0
    arr = set()
    while i < n:
        el = random.randint(l, r)
        if el not in arr:
            arr.add(str(el))
            i += 1
    entry.delete(0, END)
    entry.insert(END, str(arr).replace('{', '').replace('}', '').replace("'", ''))
    return arr


def rand_set(n, l, r):
    i = 0
    arr = set()
    while i < n:
        el = random.randint(l, r)
        if el not in arr:
            arr.add(str(el))
            i += 1
    return arr


def get_set(s):
    s = s.replace(' ', '')
    bol = True
    if ',' in s:
        s = s.split(",")
        for i in s:
            if not i.isdigit():
                bol = False
                break
    else:
        for i in s:
            if not i.isdigit():
                bol = False
                break
    if bol:
        s = set(s)
        return s
    else:
        messagebox.showinfo("Error", "Enter correct set!")


def save_sets():

    global a, b, c, un

    un = get_set(ent11.get())

    if un == set():
        messagebox.showinfo("Error", "Enter the universal set!")

    if point.get() == 1:  # generate sets
        na = ent1.get()
        nb = ent2.get()
        nc = ent3.get()

        if na.isdigit() and nb.isdigit() and nc.isdigit():
            na = int(na)
            nb = int(nb)
            nc = int(nc)

            ran = ent7.get()
            bol = False
            if ',' in ran:
                ran = ran.split(",")
                if len(ran) == 2:
                    left, right = ran[0], ran[1]
                    if left.isdigit() and right.isdigit():
                        left, right = int(left), int(right)
                        if right-left+1 >= na and right-left+1 >= nb and right-left+1 >= nc:
                            bol = True

            if bol:
                ent4.delete(0, END)
                ent5.delete(0, END)
                ent6.delete(0, END)
                a = rand_set_entry(ent4, na, left, right)
                b = rand_set_entry(ent5, nb, left, right)
                c = rand_set_entry(ent6, nc, left, right)
            else:
                messagebox.showinfo("Error", "Enter correct range!")
        else:
            messagebox.showinfo("Error", "Enter correct number of elements!")

    elif point.get() == 2:  # enter sets manually

        if ent4.get() == '' or ent5.get() == '' or ent6.get() == '':
            messagebox.showinfo("Error", "Enter the sets!")
        else:
            a = get_set(ent4.get())
            b = get_set(ent5.get())
            c = get_set(ent6.get())


def init1():
    clear()
    ent1.insert(END, '4')
    ent2.insert(END, '5')
    ent3.insert(END, '3')
    ent7.insert(END, '1,9')
    ent11.insert(END, '1,3,5,6,8')


def init2():
    clear()
    ent4.insert(END, '2, 3, 1, 8')
    ent5.insert(END, '3, 8, 5, 6, 4')
    ent6.insert(END, '6, 3, 5, 7')
    ent11.insert(END, '1,3,5,6,8')


def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)
    ent11.delete(0, END)


def show_assignment():
    assign = Toplevel()
    assign.title("Assignment")
    assign.geometry("430x160")

    f1 = PhotoImage(file="p1.gif")
    f2 = PhotoImage(file="p2.gif")

    f1 = f1.subsample(5, 5)
    f2 = f2.subsample(3, 3)

    Label(assign, image=f1).place(x=15, y=10)
    Label(assign, image=f2).place(x=18, y=95)
    assign.mainloop()

# -------------------------------------------------------------------------------------------------------------2
# -------------------------------------------------------------------------------------------------------------


def open_window2():
    global win2
    win2 = Toplevel()
    win2.title("Window 2")
    win2.geometry("310x170")

    Button(win2, text="Show sets", command=init_sets_win2).place(x=160, y=15)
    Label(win2, text="A:").place(x=15, y=20)
    Label(win2, text="B:").place(x=15, y=50)
    Label(win2, text="C:").place(x=15, y=80)
    Label(win2, text="D:").place(x=15, y=110)

    global l1, l2, l3, l4
    l1 = Label(win2)
    l1.place(x=50, y=20)
    l2 = Label(win2)
    l2.place(x=50, y=50)
    l3 = Label(win2)
    l3.place(x=50, y=80)
    l4 = Label(win2)
    l4.place(x=50, y=110)

    Button(win2, text="Calculate D", command=calc_d).place(x=160, y=50)
    Button(win2, text="Show steps", command=calc_steps).place(x=160, y=85)
    Button(win2, text="Save D to file", command=write_d_to_file).place(x=160, y=120)

    win2.mainloop()

# -------------------------------------------------------------------------------------------------------------


def calc_d():
    try:
        global d
        d = D.calc_d(a, b, c, un)

        if d == set():
            l4["text"] = '{}'
        else:
            l4["text"] = str(d).replace('{', '').replace('}', '').replace("'", '')

    except NameError:
        messagebox.showinfo("Error", "Check that you entered the sets!")
    except TypeError:
        messagebox.showinfo("Error", "Enter correct sets!")


def calc_steps():
    try:

        global d

        not_a = un - a
        not_b = un - b
        s1 = a | b
        s2 = not_a & b
        s3 = not_b | c
        not_s3 = un - s3
        s4 = s2 | not_s3
        not_s4 = un - s4

        d = s1 & not_s4

        if d == set():
            l4["text"] = '{}'
        else:
            l4["text"] = str(d).replace('{', '').replace('}', '').replace("'", '')

        messagebox.showinfo("Steps", "1. {not A} = " + set_to_str(not_a).replace("'", '') + "\n2. {not B} = " + set_to_str(not_b).replace("'", '')
                            + "\n3. {A | B} = " + set_to_str(s1).replace("'", '') + "\n4. {(1) & B} = " + set_to_str(s2).replace("'", '')
                            + "\n5. {(2) | C} = " + set_to_str(s3).replace("'", '') + "\n6. {not (5)} = " + set_to_str(not_s3).replace("'", '')
                            + "\n7. {(4) | (6)} = " + set_to_str(s4).replace("'", '') + "\n8. {not (7)} = " + set_to_str(not_s4).replace("'", '')
                            + "\n9. {(3) & (8)} = " + set_to_str(d).replace("'", '') + "\n\nAnswer: D = " + set_to_str(d).replace("'", ''))
    except NameError:
        messagebox.showinfo("Error", "Check that you entered the sets!")
    except TypeError:
        messagebox.showinfo("Error", "Enter correct sets!")


def init_sets_win2():
    try:
        if a is None or b is None or c is None:
            messagebox.showinfo("Error", "Enter correct sets!")
        else:
            l1["text"] = str(a).replace('{', '').replace('}', '').replace("'", '')
            l2["text"] = str(b).replace('{', '').replace('}', '').replace("'", '')
            l3["text"] = str(c).replace('{', '').replace('}', '').replace("'", '')

    except NameError:
        messagebox.showinfo("Error", "Check that you entered the sets!")


def write_d_to_file():
    try:
        file = open("d.txt", "w")
        file.write(set_to_str(d).replace("'", ''))
        file.close()
    except NameError:
        messagebox.showinfo("Error", "Check that you entered the sets and calculated steps!")

# -------------------------------------------------------------------------------------------------------------3
# -------------------------------------------------------------------------------------------------------------


def open_window3():
    global win3
    win3 = Toplevel()
    win3.title("Window 3")
    win3.geometry("350x170")

    Button(win3, text="Show sets", command=init_sets_win3).place(x=160, y=15)
    Label(win3, text="A:").place(x=15, y=20)
    Label(win3, text="B:").place(x=15, y=50)
    Label(win3, text="C:").place(x=15, y=80)
    Label(win3, text="D:").place(x=15, y=110)

    global l15, l16, l17, l18
    l15 = Label(win3)
    l15.place(x=50, y=20)
    l16 = Label(win3)
    l16.place(x=50, y=50)
    l17 = Label(win3)
    l17.place(x=50, y=80)
    l18 = Label(win3)
    l18.place(x=50, y=110)

    Button(win3, text="Calculate simple D", command=calc_simple_d).place(x=160, y=50)
    Button(win3, text="Show simple steps", command=calc_simple_steps).place(x=160, y=85)
    Button(win3, text="Save simple D to file", command=write_simple_d_to_file).place(x=160, y=120)

    win3.mainloop()

# -------------------------------------------------------------------------------------------------------------


def init_sets_win3():
    try:
        if a is None or b is None or c is None:
            messagebox.showinfo("Error", "Enter correct sets!")
        else:
            l15["text"] = str(a).replace('{', '').replace('}', '').replace("'", '')
            l16["text"] = str(b).replace('{', '').replace('}', '').replace("'", '')
            l17["text"] = str(c).replace('{', '').replace('}', '').replace("'", '')

    except NameError:
        messagebox.showinfo("Error", "Check that you entered the sets!")


def calc_simple_d():
    try:
        global sd
        sd = Simple_D.calc_simple_d(a, b, c, un)

        if sd == set():
            l18["text"] = '{}'
        else:
            l18["text"] = str(sd).replace('{', '').replace('}', '').replace("'", '')

    except NameError:
        messagebox.showinfo("Error", "Check that you entered the sets!")
    except TypeError:
        messagebox.showinfo("Error", "Enter correct sets!")


def calc_simple_steps():
    try:
        global sd
        not_b = un - b
        s1 = not_b | c
        sd = a & s1

        if sd == set():
            l4["text"] = '{}'
        else:
            l4["text"] = str(sd).replace('{', '').replace('}', '').replace("'", '')

        messagebox.showinfo("Steps", "1. {not B} = " + set_to_str(not_b).replace("'", '') + "\n2. {(2) | C} = " + set_to_str(s1).replace("'", '')
                            + "\n3. {A & (2)} = " + set_to_str(sd).replace("'", '') + "\n\nAnswer: D = " + set_to_str(sd).replace("'", ''))
    except NameError:
        messagebox.showinfo("Error", "Check that you entered the sets!")
    except TypeError:
        messagebox.showinfo("Error", "Enter correct sets!")


def write_simple_d_to_file():
    try:
        file = open("simple_d.txt", "w")
        file.write(set_to_str(sd).replace("'", ''))
        file.close()
    except NameError:
        messagebox.showinfo("Error", "Check that you entered the sets and calculated steps!")

# -------------------------------------------------------------------------------------------------------------4
# -------------------------------------------------------------------------------------------------------------


def open_window4():
    global win4
    win4 = Toplevel()
    win4.title("Window 4")
    win4.geometry("335x210")

    Button(win4, text="Show D", command=show_d).place(x=200, y=20)
    Label(win4, text="D:").place(x=20, y=25)
    global l6
    l6 = Label(win4)
    l6.place(x=70, y=25)

    Button(win4, text="Show X", command=show_x).place(x=200, y=55)
    Label(win4, text="X:").place(x=20, y=60)
    global l5
    l5 = Label(win4)
    l5.place(x=70, y=60)

    Button(win4, text="Show Y", command=show_y).place(x=200, y=90)
    Label(win4, text="Y:").place(x=20, y=95)
    global l7
    l7 = Label(win4)
    l7.place(x=70, y=95)

    Button(win4, text="Calculate Z", command=calc_my_z).place(x=200, y=125)
    Label(win4, text="Z:").place(x=20, y=130)
    global l8
    l8 = Label(win4)
    l8.place(x=70, y=130)

    Button(win4, text="Save Z to file", command=write_z_to_file).place(x=200, y=160)

    win4.mainloop()

# -------------------------------------------------------------------------------------------------------------


def show_d():
    try:
        if d == set():
            l6["text"] = '{}'
        else:
            l6["text"] = str(d).replace('{', '').replace('}', '').replace("'", '')
    except NameError:
        messagebox.showinfo("Error", "Check that you calculated D!")


def show_y():
    try:
        global y
        y = un - b
        if y != set():
            l7["text"] = str(y).replace('{', '').replace('}', '').replace("'", '')
        else:
            l7["text"] = '{}'
    except NameError:
        messagebox.showinfo("Error", "Check that you entered the sets!")


def show_x():
    try:
        global x
        x = c
        if x != set():
            l5["text"] = str(x).replace('{', '').replace('}', '').replace("'", '')
        else:
            l5["text"] = '{}'

    except NameError:
        messagebox.showinfo("Error", "Check that you entered the sets!")


def calc_my_z():
    try:
        global z
        z = myZ.calc_my_z(b, c, un)

        if z == set():
            l8["text"] = '{}'
        else:
            l8["text"] = str(z).replace('{', '').replace('}', '').replace("'", '')

    except NameError:
        messagebox.showinfo("Error", "Check that you entered the sets!")
    except TypeError:
        messagebox.showinfo("Error", "Enter correct sets!")


def write_z_to_file():
    try:
        file = open("z.txt", "w")
        file.write(set_to_str(z).replace("'", ''))
        file.close()
    except NameError:
        messagebox.showinfo("Error", "Check that you calculated the sets!")

# -------------------------------------------------------------------------------------------------------------5
# -------------------------------------------------------------------------------------------------------------


def open_window5():
    global win5
    win5 = Toplevel()
    win5.title("Window 5")
    win5.geometry("410x235")

    global l9, l10, l11, l12, l13, l14
    Button(win5, text="Read D", command=read_d_from_file).place(x=190, y=15)
    Label(win5, text="D:").place(x=20, y=15)
    l9 = Label(win5)
    l9.place(x=95, y=15)

    Button(win5, text="Read simple D", command=read_simple_d_from_file).place(x=190, y=50)
    Label(win5, text="Simple D:").place(x=20, y=50)
    l10 = Label(win5)
    l10.place(x=95, y=50)

    Button(win5, text="Compare D and simple D", command=compare_d_and_simple_d).place(x=190, y=85)
    Label(win5, text="Result:").place(x=20, y=85)
    l12 = Label(win5)
    l12.place(x=95, y=85)

    Button(win5, text="Read my Z", command=read_z_from_file).place(x=190, y=120)
    Label(win5, text="My Z:").place(x=20, y=120)
    l11 = Label(win5)
    l11.place(x=95, y=120)

    Button(win5, text="Calculate Python Z", command=calc_python_z).place(x=190, y=155)
    Label(win5, text="Python Z:").place(x=20, y=155)
    l14 = Label(win5)
    l14.place(x=95, y=155)

    Button(win5, text="Compare my Z and Python Z", command=compare_my_z_and_python_z).place(x=190, y=190)
    Label(win5, text="Result:").place(x=20, y=190)
    l13 = Label(win5)
    l13.place(x=95, y=190)

    win5.mainloop()

# -------------------------------------------------------------------------------------------------------------


def calc_python_z():
    try:
        text = Z.calc_z(b, c, un)

        if text == set():
            l14["text"] = '{}'
        else:
            l14["text"] = str(text).replace("'", '').replace('{', '').replace('}', '')

    except NameError:
        messagebox.showinfo("Error", "Check that you entered the sets!")
    except TypeError:
        messagebox.showinfo("Error", "Enter correct sets!")


def compare_my_z_and_python_z():
    d1 = l11["text"]
    d2 = l14["text"]

    if d1 == "" or d2 == "":
        messagebox.showinfo("Error", "Check that you read sets from file!")
    else:
        set1 = str_to_set(d1)
        set2 = str_to_set(d2)

        if set1 ^ set2 == set():
            l13["text"] = "equal"
        else:
            l13["text"] = "not equal"


def compare_d_and_simple_d():
    d1 = l9["text"]
    d2 = l10["text"]

    if d1 == "" or d2 == "":
        messagebox.showinfo("Error", "Check that you read sets from file!")
    else:
        set1 = str_to_set(d1)
        set2 = str_to_set(d2)

        if set1 ^ set2 == set():
            l12["text"] = "equal"
        else:
            l12["text"] = "not equal"


def read_d_from_file():
    try:
        f = open(r"d.txt", "r")
        text = f.read()
        l9["text"] = text.replace('{', '').replace('}', '')
        f.close()
    except FileNotFoundError:
        messagebox.showinfo("Error", "Check that you saved D to file!")


def read_simple_d_from_file():
    try:
        f = open(r"simple_d.txt", "r")
        text = f.read()
        l10["text"] = text.replace('{', '').replace('}', '')
        f.close()
    except FileNotFoundError:
        messagebox.showinfo("Error", "Check that you saved simple D to file!")


def read_z_from_file():
    try:
        f = open(r"z.txt", "r")
        text = f.read()
        l11["text"] = text.replace('{', '').replace('}', '')
        f.close()
    except FileNotFoundError:
        messagebox.showinfo("Error", "Check that you saved Z to file!")


def str_to_set(text):
    text = text.replace('{', '').replace('}', '').replace(' ', '') + ','
    prev = ''
    set1 = set()
    for i in text:
        if prev == '':
            prev = i
        elif i == ',':
            set1.add(prev)
            prev = ''
        else:
            prev += i
    return set1


open_window1()
