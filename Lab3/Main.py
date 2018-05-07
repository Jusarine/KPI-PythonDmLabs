from tkinter import *
from tkinter import messagebox

import networkx as nx
import matplotlib.pyplot as plt
import math


def open_window1():
    global root
    root = Tk()
    root.title("Window 1")
    root.attributes('-topmost', True)
    root.geometry("320x190")

    main_menu = Menu(root)
    root.config(menu=main_menu)

    open_menu = Menu(main_menu, tearoff=0)

    main_menu.add_cascade(label="Open", menu=open_menu)

    exit_menu = Menu(main_menu, tearoff=0)
    exit_menu.add_command(label="Exit", command=root.destroy)
    main_menu.add_cascade(label="Exit", menu=exit_menu)

    init_graph()

    Button(root, text="Draw graph", command=draw_graph).place(x=40, y=20)
    Button(root, text="Create new graph", command=create_new_graph).place(x=150, y=20)
    global ent1, ent2, ent3, ent4, ent5
    ent1 = Entry(root, width=4)  # v1
    ent1.place(x=40, y=60)

    ent2 = Entry(root, width=4)  # v2
    ent2.place(x=90, y=60)

    ent3 = Entry(root, width=4)  # weight
    ent3.place(x=140, y=60)

    Button(root, text="Add edge", command=add_edge).place(x=195, y=60)

    ent4 = Entry(root, width=4)  # v1
    ent4.place(x=40, y=100)

    ent5 = Entry(root, width=4)  # v2
    ent5.place(x=90, y=100)

    Button(root, text="Find shortest way", command=find_shortest_path).place(x=140, y=100)
    Button(root, text="Enter weight matrix", command=enter_weight_matrix).place(x=40, y=140)

    root.mainloop()


def init_graph():
    create_new_graph()

    weight_matrix = [
        [math.inf, 3, math.inf, 5, 6],
        [math.inf, 8, 9, 6, math.inf],
        [math.inf, 6, 9, math.inf, 7],
        [math.inf, 4, math.inf, 8, 3]
    ]

    weighted_edges = []
    for i in range(0, len(weight_matrix)):
        for j in range(0, len(weight_matrix[i])):
            if weight_matrix[i][j] != math.inf:
                weighted_edges.append([str(i+1), str(j+1), weight_matrix[i][j]])

    G.add_weighted_edges_from(weighted_edges)

    global colours
    colours = [
        "yellow",
        "gray",
        "pink",
        "blue",
        "violet",
        "red",
        "green",
        "brown",
        "white",
        "black"
    ]


def create_new_graph():
    global G
    G = nx.Graph()


def add_edge():
    G.add_weighted_edges_from([[ent1.get(), ent2.get(), int(ent3.get())]])
    draw_graph()


def draw_graph():
    pos = nx.circular_layout(G)

    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(G, pos)

    plt.savefig('graph.png')
    plt.show()
    plt.close()


def find_shortest_path():
    res = nx.algorithms.bellman_ford_path(G, ent4.get(), ent5.get())
    s = ""
    for i in res:
        s = s + "->" + i

    messagebox.showinfo("The shortest path from " + ent4.get() + " to " + ent5.get(),
                        "The shortest path " + s + "\n" + "The path length = " +
                        str(nx.algorithms.bellman_ford_path_length(G, ent4.get(), ent5.get())))


def enter_weight_matrix():
    win2 = Toplevel()
    win2.title("Window 2")
    win2.geometry("290x130")

    Label(win2, text="Number of nodes: ").place(x=40, y=20)
    Button(win2, text="Create matrix", command=create_matrix).place(x=40, y=70)
    global ent6
    ent6 = Entry(win2, width=4)
    ent6.place(x=170, y=20)
    Button(win2, text="Save matrix", command=save_matrix).place(x=155, y=70)
    win2.mainloop()


def create_matrix():
    win3 = Toplevel()
    win3.title("Window 3")

    global arr, n
    n = int(ent6.get())

    win3.geometry(str(n*36) + "x" + str(n*28))

    arr = []
    for i in range(0, n):
        for j in range(0, n):
            e = Entry(win3, width=3)
            e.grid(row=i, column=j, sticky=NSEW)
            arr.append(e)
    win3.mainloop()


def save_matrix():
    weighted_edges = []
    for i in range(0, n):
        for j in range(0, n):
            if arr[i*n+j].get() != '':
                weighted_edges.append([str(i+1), str(j+1), int(arr[i*n+j].get())])

    create_new_graph()
    G.add_weighted_edges_from(weighted_edges)


open_window1()


