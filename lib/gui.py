import tkinter as tk
from .vote_helper import randomizer


class VoteGUI:
    def __init__(self, master):
        self.master = master
        master.title("Фотон курильщика")

        master.geometry("640x240")

        self.result_label = tk.Label(master, text="Выбираем за кого голосовать 17.03 в 12:00", font=("Arial", 16))
        self.result_label.pack(pady=20)

        self.button = tk.Button(master, text="Стрельнуть временнЫм рандомом", command=self.show_result)
        self.button.pack()

    def show_result(self):
        result = randomizer()
        self.result_label.config(text=result)


if __name__ == "__main__":
    root = tk.Tk()
    app = VoteGUI(root)
    root.mainloop()
