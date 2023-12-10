import tkinter as tk

from tkinter import messagebox

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

        # TODO: add a email validation callback

        # Password label
        password_label = tk.Label(self, text="Senha")
        password_label.pack()

        # Password entry
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()

        # Forgot password
        forgot_password = tk.Label(self, text="Esqueceu sua senha?", fg="blue")
        forgot_password.bind("<Button-1>", lambda e: controller.show_frame(ForgotPasswordPage))
        forgot_password.pack()

        # Sign in button
        button = tk.Button(self, text="Entrar",
                            command=lambda: print("Email: {}\nPassword: {}".format(email_entry.get(), password_entry.get())))
        button.pack()

        # TODO: add a login validation on database callback

        # Sign up button
        button = tk.Button(self, text="Não tem conta? Cadastre-se",
                            command=lambda: print("Sign up button clicked"))
        button.pack()
class ForgotPasswordPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Frame for Email Address Input
        self.email_frame = tk.Frame(self)
        tk.Label(self.email_frame, text="Enter your email address").pack()
        self.email_entry = tk.Entry(self.email_frame)  # TODO: add email validation callback
        self.email_entry.pack()
        email_submit = tk.Button(self.email_frame, text="Submit",
                                 command=self.send_recovery_code)
        email_submit.pack()
        self.email_frame.pack()

        # Frame for Code Verification
        self.code_frame = tk.Frame(self)
        tk.Label(self.code_frame, text="Enter the code you received").pack() 
        self.code_entry = tk.Entry(self.code_frame) # Add a code structure validation callback
        self.code_entry.pack()
        code_submit = tk.Button(self.code_frame, text="Submit",
                                command=self.verify_code)
        code_submit.pack()
        resend_code = tk.Button(self.code_frame, text="Resend Code",
                                command=self.send_recovery_code)
        resend_code.pack()

        # Frame for Password Reset
        self.reset_frame = tk.Frame(self)
        tk.Label(self.reset_frame, text="Enter your new password").pack()
        self.new_password_entry = tk.Entry(self.reset_frame, show="*")
        self.new_password_entry.pack() # TODO: add a password validation callback
        tk.Label(self.reset_frame, text="Confirm your new password").pack()
        self.confirm_password_entry = tk.Entry(self.reset_frame, show="*")
        self.confirm_password_entry.pack() # TODO: add a password match validation callback
        reset_submit = tk.Button(self.reset_frame, text="Reset Password",
                                 command=self.reset_password)
        reset_submit.pack()

    def send_recovery_code(self):
        email = self.email_entry.get()
        # TODO: add sending recovery code logic

        # Hide the email frame and show the code frame
        self.email_frame.pack_forget()
        self.code_frame.pack()

    def verify_code(self):
        code = self.code_entry.get()
        # TODO: add code verification logic

        # Hide the code frame and show the reset frame
        self.code_frame.pack_forget()
        self.reset_frame.pack()

    def reset_password(self):
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if new_password == confirm_password:
            # TODO: add password reset logic
            messagebox.showinfo("Success", "Password reset successfully")
        else:
            messagebox.showerror("Error", "Passwords do not match")

class SignUpPage(tk.Frame):
    pass

class UserPage(tk.Frame):
    pass

# TODO: add placeholders on the entry fields (ex: email)