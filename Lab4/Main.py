from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt


def open_window1():
    global root
    root = Tk()
    root.title("Window 1")
    root.attributes('-topmost', True)
    root.geometry("320x120")

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
    global ent1, ent2
    ent1 = Entry(root, width=4)
    ent1.place(x=40, y=60)

    ent2 = Entry(root, width=4)
    ent2.place(x=90, y=60)

    Button(root, text="Add edge", command=add_edge).place(x=150, y=60)

    root.mainloop()


def init_graph():
    create_new_graph()
    e = [('1', '2'), ('2', '3'), ('3', '4'), ('1', '5'), ('2', '5'), ('2', '6'), ('3', '6'), ('3', '7'), ('7', '4'),
         ('5', '8'), ('5', '6'), ('6', '8'), ('6', '9'), ('6', '7'), ('7', '9')]
    G.add_edges_from(e)

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
    G.add_edge(ent1.get(), ent2.get())


def draw_graph():
    c = nx.greedy_color(G)  # словарь вершина : цифра (номер цвета)

    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=[j for j in c], node_color=[colours[c[i]] for i in c])
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.savefig('graph.png')
    plt.show()
    plt.close()


open_window1()
