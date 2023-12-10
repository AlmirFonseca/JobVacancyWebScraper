import tkinter as tk

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Create a label and button
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)

        # Add an introduction text
        introduction = tk.Label(self, text="Bem vindo ao nosso projeto...")
    
        # Go to the login page
        button = tk.Button(self, text="Vamos Começar!",
                            command=lambda: controller.show_frame(LoginPage))

        button.pack()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Create a label and button
        label = tk.Label(self, text="Iniciar sessão")
        label.pack(pady=10, padx=10)
    
        # Email label
        email_label = tk.Label(self, text="Email")
        email_label.pack()

        # Email entry
        email_entry = tk.Entry(self)
        email_entry.pack()

        # Password label
        password_label = tk.Label(self, text="Senha")
        password_label.pack()

        # Password entry
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()

        # Forgot password
        forgot_password = tk.Label(self, text="Esqueceu sua senha?", fg="blue")
        forgot_password.bind("<Button-1>", lambda e: print("Forgot password clicked"))
        forgot_password.pack()

        # Sign in button
        button = tk.Button(self, text="Entrar",
                            command=lambda: print("Email: {}\nPassword: {}".format(email_entry.get(), password_entry.get())))
        button.pack()

        # Sign up button
        button = tk.Button(self, text="Não tem conta? Cadastre-se",
                            command=lambda: print("Sign up button clicked"))
        button.pack()

def ForgotPasswordPage(tk.Frame):
    pass

def SignUpPage(tk.Frame):
    pass

def UserPage(tk.Frame):
    

        