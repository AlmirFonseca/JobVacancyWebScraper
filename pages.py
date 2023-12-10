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
        forgot_password.bind("<Button-1>", lambda: controller.show_frame(ForgotPasswordPage))
        forgot_password.pack()

        # Sign in button
        button = tk.Button(self, text="Entrar",
                            command=lambda: print("Email: {}\nPassword: {}".format(email_entry.get(), password_entry.get())))
        button.pack()

        # TODO: add a login validation on database callback

        # Sign up button
        button = tk.Button(self, text="Não tem conta? Cadastre-se",
                            command=lambda: controller.show_frame(SignUpPage))
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
                                 command=lambda: self.send_recovery_code)
        email_submit.pack()
        self.email_frame.pack()

        # Frame for Code Verification
        self.code_frame = tk.Frame(self)
        tk.Label(self.code_frame, text="Enter the code you received").pack() 
        self.code_entry = tk.Entry(self.code_frame) # Add a code structure validation callback
        self.code_entry.pack()
        code_submit = tk.Button(self.code_frame, text="Submit",
                                command=lambda: self.verify_code)
        code_submit.pack()
        resend_code = tk.Button(self.code_frame, text="Resend Code",
                                command=lambda: self.send_recovery_code)
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
                                 command=lambda: self.reset_password)
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
    # Fields: Name, Surname, Username, Email, Password, Confirm Password

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create a label and button
        label = tk.Label(self, text="Sign Up Page")
        label.pack(pady=10, padx=10)

        # Name label
        name_label = tk.Label(self, text="Nome")
        name_label.pack()

        # Name entry
        name_entry = tk.Entry(self)
        name_entry.pack()

        # Surname label
        surname_label = tk.Label(self, text="Sobrenome")
        surname_label.pack()

        # Surname entry
        surname_entry = tk.Entry(self)
        surname_entry.pack()

        # Username label
        username_label = tk.Label(self, text="Nome de usuário")
        username_label.pack()

        # Username entry
        username_entry = tk.Entry(self)
        username_entry.pack()

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

        # Confirm password label
        confirm_password_label = tk.Label(self, text="Confirmar senha")
        confirm_password_label.pack()

        # Confirm password entry
        confirm_password_entry = tk.Entry(self, show="*")
        confirm_password_entry.pack()

        # Sign up button
        button = tk.Button(self, text="Cadastrar",
                            command=lambda: self.sign_up(name_entry.get(), 
                                                 surname_entry.get(), 
                                                 username_entry.get(), 
                                                 email_entry.get(), 
                                                 password_entry.get(), 
                                                 confirm_password_entry.get()))
        
        button.pack()

    def sign_up(self, name, surname, username, email, password, confirm_password):
        
        # TODO: add the sign up logic
        
        
        # GO to the compentencies page
        self.controller.show_frame(CompentenciesPage)

class CompentenciesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create a label and button
        label = tk.Label(self, text="Seleção de Competências")
        label.pack(pady=10, padx=10)

        # Create a descritption
        description = tk.Label(self, text="Selecione as linguagens de programação que você domina:")
        description.pack()

        # List fo compentencies
        compentencies_list = ["Python", "C", "C++", "C#", "JavaScript", "Java", "HTML", "CSS",
                              "PHP", "SQL", "Ruby", "Julia", "SPARQL", "Swift", "TypeScript", "R"]
        
        # Dict to store the selected compentencies
        self.selected_compentencies = {}

        # Frame to hold the checkboxes 
        checkboxes = tk.Frame(self)
        checkboxes.pack()

        # Create a checkbox for each compentency  
        for compentency in compentencies_list:
            self.selected_compentencies[compentency] = tk.BooleanVar()
            tk.Checkbutton(checkboxes, text=compentency, variable=self.selected_compentencies[compentency]).pack()

        # Confirm button
        button = tk.Button(self, text="Confirmar",
                            command=lambda: self.submit_selection())
        button.pack()

        # Button to go back to the login page
        button = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(LoginPage))

    def submit_selection(self):

        selected_competencies =[compentency for compentency, value in self.selected_compentencies.items() if value.get()]
        print(selected_competencies)

        # TODO: add the validation for no selected compentencies

        # Go to the seniority level page
        self.controller.show_frame(SeniorityLevelPage)

class SeniorityLevelPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create a label and button
        label = tk.Label(self, text="Nível de Senioridade")
        label.pack(pady=10, padx=10)

        # Create a descritption
        description = tk.Label(self, text="Selecione o seu nível de senioridade:")
        description.pack()

        # List of seniority levels
        seniority_levels = ["Sem experiência", "Junior", "Pleno", "Sênior"]
        # Dict to store the selected seniority level
        self.selected_seniority_level = tk.IntVar()

        # Radio buttons to select the seniority level
        for seniority_level in seniority_levels:
            tk.Radiobutton(self, text=seniority_level, variable=self.selected_seniority_level, value=seniority_levels.index(seniority_level)).pack()

        # Confirm button
        button = tk.Button(self, text="Confirmar",
                            command=lambda: self.submit_selection())
        
        button.pack()

        # Button to go back to the login page
        button = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(LoginPage))
        
    def submit_selection(self):
        selected_seniority_level = self.selected_seniority_level.get()

        # TODO: add the validation for no selected seniority level

        # Go to the home page
        self.controller.show_frame(HomePage)

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Create a header with buttons
        header = tk.Frame(self)
        header.pack()

        # Button to go to the user page
        button = tk.Button(header, text="Perfil",
                            command=lambda: controller.show_frame(UserPage))
        button.pack(side="left")

        # Button to go to the compentencies page
        button = tk.Button(header, text="Competências",
                            command=lambda: controller.show_frame(CompentenciesPage))
        button.pack(side="left")

        # Button to go to the seniority level page
        button = tk.Button(header, text="Nível de Senioridade",
                            command=lambda: controller.show_frame(SeniorityLevelPage))
        button.pack(side="left")

        # Create a label and button
        label = tk.Label(self, text="Home Page")
        label.pack(pady=10, padx=10)

        # Add an introduction text
        introduction = tk.Label(self, text="Bem vindo ao nosso projeto...")
        introduction.pack()
    
        # Button to add a curriculum
        button = tk.Button(self, text="Adicionar currículo",
                            # command=lambda: controller.show_frame(AddCurriculumPage))
                            command=lambda: print("Adicionar currículo"))
        button.pack()

        # Button to see the list of jobs
        button = tk.Button(self, text="Ver vagas",
                            # command=lambda: controller.show_frame(JobListPage))
                            command=lambda: print("Ver vagas"))
        button.pack()

# class UserPage(tk.Frame):
#     pass

# class AddCurriculumPage(tk.Frame):
#     pass

# class JobListPage(tk.Frame):
#     pass

# TODO: add placeholders on the entry fields (ex: email)