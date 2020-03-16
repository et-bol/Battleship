import tkinter as tk

class Battleship:
    def __init__(self, master):
        self.master = master
        self.master.title("Mine Sweeper")
        self.master.resizable(False, False)
        self.mainframe = tk.Frame(self.master, bg='white', width=500, height=500)
        self.mainframe.pack(fill=tk.BOTH, expand=True)
        self.generate_menu()

        self.field = tk.Frame(self.mainframe, bg='black', width=200, height=200)
        self.text = tk.Text(self.field)
        self.text.insert(tk.END, "Field board")
        self.text.pack()
        self.shots = tk.Frame(self.mainframe, bg='blue', width=200, height=200)
        self.text2 = tk.Text(self.shots)
        self.text2.insert(tk.END, "Shots board")
        self.text2.pack()

        self.field.pack(side='left')
        self.shots.pack(side='left')

    def generate_menu(self):
        menubar = tk.Menu(self.master)

        game = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game)
        menubar.add_separator()

        display = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Display", menu=display)
        menubar.add_separator()

        self.master.config(menu=menubar)


if __name__ == '__main__':
    root = tk.Tk()
    Battleship(root)
    root.mainloop()
