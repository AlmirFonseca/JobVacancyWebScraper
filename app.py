import tkinter as tk

import sys
sys.path.append('./src/pages/')

from tkinter import ttk

from page_factory import PageFactory

DIMS = "800x600"


class AppController(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Apply dark theme globally
        self.apply_dark_theme()

        # Set the title
        self.title("Job Finder")

        # Set the dimensions of the window
        self.geometry(DIMS)
        self.resizable(0, 0)

        self.page_factory = PageFactory(container, self)

        self.show_frame("StartPage")

    def show_frame(self, cont: str) -> None:
        """
        Show frame
        Args:
            cont(str): Frame type
        """
        frame = self.page_factory.create_page(cont)
        frame.tkraise()

    def apply_dark_theme(self):
        # Create a style object
        style = ttk.Style(self)

        # Choose a theme
        style.theme_use("alt")  # 'clam', 'alt', 'default', or 'classic' might work well for dark themes
        

        # Configure the style
        style.configure('.', background='#111', foreground='white', padx=10, pady=10)
        style.configure('TButton', background='#6B1F1F', foreground='white', borderwidth=0)
        style.configure('TLabel', background='#111', foreground='white', padx=20, pady=5)
        style.configure('TEntry', fieldbackground='#111', foreground='white', bordercolor='#ffffff', borderwidth=0, padx=20)
        style.configure('TCheckbutton', background='#555', foreground='black', borderwidth=10, bordercolor='#a1a1a1', padx=20, pady=10, indicatoron=False, selectcolor='gray')
        style.configure('TRadiobutton', background='#555', foreground='black', borderwidth=10, bordercolor='#a1a1a1', padx=20, pady=10, indicatoron=False, selectcolor='gray')

        # Configure specific options for widgets like Button
        # font white when active, background light blue when active, etc
        style.map('TButton',
                  background=[('active', '#991010'), ('pressed', '#1C86EE'), ('disabled', '#7A7A7A')],
                    foreground=[('active', 'white'), ('pressed', 'white'), ('disabled', '#7A7A7A')])
        
        style.map('TCheckbutton',
                    background=[('active', '#991010'), ('pressed', '#1C86EE'), ('disabled', '#7A7A7A')],
                        foreground=[('active', 'black'), ('pressed', 'white'), ('disabled', '#7A7A7A')])
        
        style.map('TRadiobutton',
                    background=[('active', '#991010'), ('pressed', '#1C86EE'), ('disabled', '#7A7A7A')],
                        foreground=[('active', 'black'), ('pressed', 'white'), ('disabled', '#7A7A7A')])

        # Set the global font
        default_font = ('Helvetica', 10)
        big_font = ('Helvetica', 16)
        style.configure('.', font=default_font)
        style.configure('TButton', font=big_font)

if __name__ == "__main__":
    app = AppController()
    app.mainloop()