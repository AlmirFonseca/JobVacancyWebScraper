import tkinter as tk
from pages import StartPage, LoginPage, ForgotPasswordPage, SignUpPage, CompentenciesPage, SeniorityLevelPage

class AppController(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Set the title
        self.title("Job Finder")

        # Set the dimensions of the window
        self.geometry("800x600")

        self.frames = {}
        # for F in (StartPage, LoginPage, SignUpPage, UserPage):
        for F in (StartPage, LoginPage, ForgotPasswordPage, SignUpPage, CompentenciesPage, SeniorityLevelPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = AppController()
    app.mainloop()