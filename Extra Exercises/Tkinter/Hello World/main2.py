import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.label = tk.Label(self, text="Hello World", padx=5, pady=5, anchor="center")
        self.label.pack(expand=True)

        self.geometry("600x400")
        self.title('Hello World')

if __name__ == "__main__":
    root = Root()
    root.mainloop()