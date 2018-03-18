import random
from tkinter import *
from tkinter import messagebox

# -------------------------------------------------------------------------------------------------------------1
# -------------------------------------------------------------------------------------------------------------

girlNames = ("Emily", "Jane", "Alice", "Jessica", "Chloe", "Ann", "Mia", "Chrissy", "lily", "Sarah", "Erin", "Nancy", "Amber", "Katie", "Grace", "Olivia")
boyNames = ("Joshua", "James", "Ethan", "John", "Adrian", "Lucas", "Ryan", "Steven", "Thomas", "Kevin", "Jake", "Oliver", "Aidan", "Jeffery", "Nathan", "Daniel")


def open_window1():
    global root
    root = Tk()
    root.title("Window 1")
    root.attributes('-topmost', True)
    root.geometry("300x115")

    main_menu = Menu(root)
    root.config(menu=main_menu)

    open_menu = Menu(main_menu, tearoff=0)
    open_menu.add_command(label="Window 2", command=open_window2)
    open_menu.add_command(label="Window 3", command=open_window3)
    open_menu.add_command(label="Window 4", command=open_window4)

    main_menu.add_cascade(label="Open", menu=open_menu)

    exit_menu = Menu(main_menu, tearoff=0)
    exit_menu.add_command(label="Exit", command=root.destroy)
    main_menu.add_cascade(label="Exit", menu=exit_menu)

    print_info()

    root.mainloop()


# -------------------------------------------------------------------------------------------------------------

def print_info():
    l1 = Label(root)
    l1.place(x=20, y=20)
    g = 72
    n = 4
    var = (n + g % 60) % 30 + 1
    l1["text"] = "Full name: Gladka Tatyana Anatoliivna\nGroup: IV-72\nList number: 4\nVariant: " + str(var)

# -------------------------------------------------------------------------------------------------------------2
# -------------------------------------------------------------------------------------------------------------


def open_window2():
    global win2
    win2 = Toplevel()
    win2.title("Window 2")
    win2.geometry("520x320")

    Label(win2, text="Girl names").place(x=60, y=20)
    Label(win2, text="Boy names").place(x=250, y=20)

    global Lb1
    Lb1 = Listbox(win2, selectmode=MULTIPLE, height=14)

    for name in girlNames:
        Lb1.insert(END, name)
    Lb1.place(x=20, y=50)

    global Lb2
    Lb2 = Listbox(win2, selectmode=MULTIPLE, height=14)

    for name in boyNames:
        Lb2.insert(END, name)
    Lb2.place(x=200, y=50)

    global point
    point = IntVar()
    Rb1 = Radiobutton(win2, text="Copy to A", variable=point, value=1)
    Rb2 = Radiobutton(win2, text="Copy to B", variable=point, value=2)
    point.set(1)
    Rb1.place(x=380, y=50)
    Rb2.place(x=380, y=80)

    Button(win2, text="Copy", command=copy_names).place(x=380, y=20)
    Button(win2, text="Save A to file", command=save_a_to_file).place(x=380, y=110)
    Button(win2, text="Read A from file", command=read_a_from_file).place(x=380, y=140)
    Button(win2, text="Clear A", command=clear_a).place(x=380, y=170)

    Button(win2, text="Save B to file", command=save_b_to_file).place(x=380, y=200)
    Button(win2, text="Read B from file", command=read_b_from_file).place(x=380, y=230)
    Button(win2, text="Clear B", command=clear_b).place(x=380, y=260)

    win2.mainloop()


def read_a_from_file():
    try:
        file = open("A.txt", "r")
        for name in file.readlines():
            Lb3.insert(END, name)
    except FileNotFoundError:
         messagebox.showinfo("Error", "Checked that you saved A to file!")
    except NameError:
        messagebox.showinfo("Error", "Checked that you created A!")
    finally:
        file.close()


def read_b_from_file():
    try:
        file = open("B.txt", "r")
        for name in file.readlines():
            Lb4.insert(END, name)
    except FileNotFoundError:
        messagebox.showinfo("Error", "Checked that you saved B to file!")
    except NameError:
        messagebox.showinfo("Error", "Checked that you created B!")
    finally:
        file.close()


def clear_a():
    try:
        Lb3.delete(0, Lb3.size()-1)
    except NameError:
        messagebox.showinfo("Error", "Checked that you created A!")


def clear_b():
    try:
        Lb4.delete(0, Lb4.size()-1)
    except NameError:
        messagebox.showinfo("Error", "Checked that you created B!")


def save_a_to_file():
    try:
        file = open("A.txt", "w")
        for name in Lb3.get(0, Lb3.size()-1):
            file.write(name)
            file.write('\n')
        file.close()
    except NameError:
        messagebox.showinfo("Error", "Checked that you created A!")


def save_b_to_file():
    try:
        file = open("B.txt", "w")
        for name in Lb4.get(0, Lb4.size()-1):
            file.write(name)
            file.write('\n')
        file.close()
    except NameError:
        messagebox.showinfo("Error", "Checked that you created B!")


def copy_names():
    try:
        for i in Lb1.curselection():
            if point.get() == 1:
                insert_unique_name(Lb3, girlNames[i])
            elif point.get() == 2:
                insert_unique_name(Lb4, girlNames[i])

        for i in Lb2.curselection():
            if point.get() == 1:
                insert_unique_name(Lb3, boyNames[i])
            elif point.get() == 2:
                insert_unique_name(Lb4, boyNames[i])
    except NameError:
        messagebox.showinfo("Error", "Checked that you created A and B!")


def insert_unique_name(Lb, name):
    for k in Lb.get(0, Lb.size()-1):
        if k == name:
            break
    else:
        Lb.insert(END, name)


# -------------------------------------------------------------------------------------------------------------3
# -------------------------------------------------------------------------------------------------------------


def open_window3():
    global win3, Lb3, Lb4
    win3 = Toplevel()
    win3.title("Window 3")
    win3.geometry("510x300")

    Label(win3, text="A").place(x=90, y=20)
    Label(win3, text="B").place(x=280, y=20)

    Lb3 = Listbox(win3, height=12)
    Lb3.place(x=20, y=50)

    Lb4 = Listbox(win3, height=12)
    Lb4.place(x=205, y=50)

    Lb3.insert(END, "Alice")
    Lb3.insert(END, "John")
    Lb3.insert(END, "Ann")
    Lb3.insert(END, "Lucas")
    Lb3.insert(END, "Kevin")
    Lb3.insert(END, "Erin")

    Lb4.insert(END, "Jake")
    Lb4.insert(END, "Jessica")
    Lb4.insert(END, "Mia")
    Lb4.insert(END, "Thomas")
    Lb4.insert(END, "Jeffery")

    Button(win3, text="Show aSb", command=show_s).place(x=390, y=50)
    Button(win3, text="Show aRb", command=show_r).place(x=390, y=80)

    win3.mainloop()

# -------------------------------------------------------------------------------------------------------------


def show_s():
    global s
    s = init_matrix()

    for i in range(0, Lb3.size()):
        for j in range(0, Lb4.size()):
            if Lb3.get(i) in boyNames and Lb3.get(i) != Lb4.get(j):
                s[i+1][j+1] = random.randint(0, 1)

    global win5
    win5 = Toplevel()
    win5.title("aSb")

    for m in range(0, Lb3.size()+1):
        for n in range(0, Lb4.size()+1):
            Label(win5, text=s[m][n], relief=RIDGE).grid(row=m, column=n, sticky=NSEW)

    win5.mainloop()

# -------------------------------------------------------------------------------------------------------------


def show_r():
    try:
        global r
        r = init_matrix()

        for i in range(0, Lb3.size()):
            for j in range(0, Lb4.size()):
                if s[i+1][j+1] != 1 and Lb3.get(i) in boyNames and Lb4.get(j) in girlNames:
                    r[i + 1][j + 1] = random.randint(0, 1)

        global win6
        win6 = Toplevel()
        win6.title("aRb")

        for m in range(0, Lb3.size()+1):
            for n in range(0, Lb4.size()+1):
                Label(win6, text=r[m][n], relief=RIDGE).grid(row=m, column=n, sticky=NSEW)
    except NameError:
        messagebox.showinfo("Error", "Check that you calculated aSb!")

    win6.mainloop()


# -------------------------------------------------------------------------------------------------------------4
# -------------------------------------------------------------------------------------------------------------


def open_window4():
    global win4
    win4 = Toplevel()
    win4.title("Window 4")
    win4.geometry("270x140")

    Button(win4, text="Union", command=r_union_s).place(x=20, y=20)
    Button(win4, text="Intersection", command=r_intersection_s).place(x=20, y=50)
    Button(win4, text="Difference", command=r_difference_s).place(x=20, y=80)
    Button(win4, text="Addition R", command=addition_r).place(x=150, y=20)
    Button(win4, text="Reverse S", command=reverse_s).place(x=150, y=50)

    win4.mainloop()

# -------------------------------------------------------------------------------------------------------------


def addition_r():
    try:
        a = init_matrix()

        for i in range(0, Lb3.size()):
            for j in range(0, Lb4.size()):
                if r[i+1][j+1] == 0:
                    a[i + 1][j + 1] = 1

        win9 = Toplevel()
        win9.title("Addition R")

        for m in range(0, Lb3.size()+1):
            for n in range(0, Lb4.size()+1):
                Label(win9, text=a[m][n], relief=RIDGE).grid(row=m, column=n, sticky=NSEW)
    except NameError:
        messagebox.showinfo("Error", "Checked that you calculated R!")


def reverse_s():
    try:
        v = init_matrix()

        for i in range(0, Lb3.size()):
            for j in range(0, Lb4.size()):
                if s[i+1][j+1] == 0:
                    v[i + 1][j + 1] = 1

        win11 = Toplevel()
        win11.title("Reverse S")

        for m in range(0, Lb3.size()+1):
            for n in range(0, Lb4.size()+1):
                Label(win11, text=v[m][n], relief=RIDGE).grid(row=m, column=n, sticky=NSEW)
    except NameError:
        messagebox.showinfo("Error", "Checked that you calculated S!")


def r_union_s():
    try:
        u = init_matrix()

        for i in range(0, Lb3.size()):
            for j in range(0, Lb4.size()):
                if r[i+1][j+1] == 1 or s[i + 1][j + 1] == 1:
                    u[i + 1][j + 1] = 1

        win7 = Toplevel()
        win7.title("Union")

        for m in range(0, Lb3.size()+1):
            for n in range(0, Lb4.size()+1):
                Label(win7, text=u[m][n], relief=RIDGE).grid(row=m, column=n, sticky=NSEW)
    except NameError:
        messagebox.showinfo("Error", "Checked that you calculated R and S!")


def r_intersection_s():
    try:
        t = init_matrix()

        for i in range(0, Lb3.size()):
            for j in range(0, Lb4.size()):
                if r[i+1][j+1] == 1 and s[i + 1][j + 1] == 1:
                    t[i + 1][j + 1] = 1

        win8 = Toplevel()
        win8.title("Intersection")

        for m in range(0, Lb3.size()+1):
            for n in range(0, Lb4.size()+1):
                Label(win8, text=t[m][n], relief=RIDGE).grid(row=m, column=n, sticky=NSEW)
    except NameError:
        messagebox.showinfo("Error", "Checked that you calculated R and S!")


def r_difference_s():
    try:
        d = init_matrix()

        for i in range(0, Lb3.size()):
            for j in range(0, Lb4.size()):
                if r[i+1][j+1] == 1 and s[i + 1][j + 1] != 1:
                    d[i + 1][j + 1] = 1

        win10 = Toplevel()
        win10.title("Difference")

        for m in range(0, Lb3.size()+1):
            for n in range(0, Lb4.size()+1):
                Label(win10, text=d[m][n], relief=RIDGE).grid(row=m, column=n, sticky=NSEW)
    except NameError:
        messagebox.showinfo("Error", "Checked that you calculated R and S!")


def init_matrix():
    matrix = [[0 for i in range(0, Lb4.size() + 1)] for j in range(0, Lb3.size() + 1)]

    i = 1
    for name in Lb3.get(0, Lb3.size()-1):
        matrix[i][0] = name
        i += 1

    i = 1
    for name in Lb4.get(0, Lb4.size()-1):
        matrix[0][i] = name
        i += 1
    return matrix


open_window1()
