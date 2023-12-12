import tkinter as tk
import pandas as pd
import webbrowser
import secrets
import sys
sys.path.append('./src/emailer')
sys.path.append('./src/models')
sys.path.append('./src/daos')
sys.path.append('./src/job_scraper')
from emailer import Emailer
from tkinter import messagebox, ttk
from time import sleep
from uuid import uuid4
from smtplib import SMTPAuthenticationError
from job_scraper import JobScraper
from user import User
from file_link import FileLink
from user_dao import create, get_by_email, update
from file_link_dao import create_file_link, get_file_links_by_user_id, update_file_link
from skill_dao import get_skills
from user_skill_dao import create_user_skill, get_user_skills_by_user_id, delete_user_skill


logged_user = None


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        # Create a label and button
        label = ttk.Label(self, text="Start Page")

        # Change font size
        label.config(font=("Courier", 30))
        label.pack(pady=120, padx=10)       

        # Add an introduction text
        introduction = ttk.Label(self, text="Bem vindo ao nosso projeto...")
        introduction.pack(pady=10, padx=10)
    
        # Go to the login page
        button = ttk.Button(self, text="Vamos Começar!",
                            command=lambda: controller.show_frame("LoginPage"))

        button.pack(pady=40, padx=10, ipadx=20)


class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Create a label in left side
        label = ttk.Label(self, text="Iniciar sessão")
        
        # Change font size
        label.config(font=("Courier", 30))
        label.pack(pady=60, padx=10)        
    
        # Email label
        email_label = ttk.Label(self, text="Email")
        email_label.pack()

        # Email entry
        email_entry = ttk.Entry(self)
        email_entry.pack()

        # Password label
        password_label = ttk.Label(self, text="Senha")
        password_label.pack()

        # Password entry
        password_entry = ttk.Entry(self, show="*")
        password_entry.pack()

        # Forgot password
        forgot_password = tk.Label(self, text="Esqueceu sua senha?", fg="blue", background="#111")
        forgot_password.bind("<Button-1>", lambda _: controller.show_frame("ForgotPasswordPage"))
        forgot_password.pack(padx=20, pady=5)

        # Sign in button
        button = ttk.Button(self, text="Entrar",
                            command=lambda: self.login(email_entry.get(), password_entry.get()))
        # Change font
        button.pack(pady=10)

        # Sign up button
        button = ttk.Button(self, text="Não tem conta? Cadastre-se",
                            command=lambda: controller.show_frame("SignUpPage"))

        button.pack(padx=100, pady=100, ipadx=20)
    
    def login(self, email, password):
        if not Emailer.is_valid_email(email):
            messagebox.showerror("Erro", "Email inválido")
            return
    
        user = get_by_email(email)
        if user is None:
            messagebox.showerror("Erro", "Email não cadastrado")
            return

        if not user.check_password(password):
            messagebox.showerror("Erro", "Senha incorreta")
            return
        
        global logged_user
        logged_user = user
        self.controller.show_frame("HomePage")
    

class ForgotPasswordPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        # Create a label and button
        label = ttk.Label(self, text="Troque de senha")

        # Change font size
        label.config(font=("Courier", 30))
        label.pack(pady=60, padx=10)   

        # Frame for Email Address Input
        self.email_frame = ttk.Frame(self)
        self.reset_code = None
        ttk.Label(self.email_frame, text="Digite seu endereço e-mail").pack()
        self.email_entry = ttk.Entry(self.email_frame)
        self.email_entry.pack()
        self.email_submit = ttk.Button(self.email_frame, text="Submit",
                                 command=lambda: self.send_recovery_code())
        self.email_submit.pack(pady=50)
        self.email_frame.pack()
        
        button = ttk.Button(self, text="Voltar", command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=10, padx=10)

        # Frame for Code Verification
        self.code_frame = ttk.Frame(self)
        
        ttk.Label(self.code_frame, text="Digite o código recebido").pack() 
        self.recovery_code_label = ttk.Label(self.code_frame)
        self.recovery_code_label.pack()
        self.code_entry = ttk.Entry(self.code_frame) # Add a code structure validation callback
        self.code_entry.pack()
        code_submit = ttk.Button(self.code_frame, text="Submit",
                                command=lambda: self.verify_code())
        code_submit.pack()
        resend_code = ttk.Button(self.code_frame, text="Resend Code",
                                command=lambda: self.resend_recovery_code())
        resend_code.pack()
        
        button = ttk.Button(self, text="Voltar", command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=10, padx=10)

        # Frame for Password Reset
        self.reset_frame = ttk.Frame(self)
        tk.Label(self.reset_frame, text="Enter your new password").pack()
        self.new_password_entry = ttk.Entry(self.reset_frame, show="*")
        self.new_password_entry.pack() # TODO: add a password validation callback
        tk.Label(self.reset_frame, text="Confirm your new password").pack()
        self.confirm_password_entry = ttk.Entry(self.reset_frame, show="*")
        self.confirm_password_entry.pack()
        reset_submit = ttk.Button(self.reset_frame, text="Reset Password",
                                 command=lambda: self.reset_password())
        reset_submit.pack()
        
        button = ttk.Button(self, text="Voltar", command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=10, padx=10)

    def send_recovery_code(self):
        # disable the email_submit button
        self.email_submit.config(state="disabled")
        email = self.email_entry.get()
        emailer = Emailer()
        if emailer.is_valid_email(email):
            user = get_by_email(email)
            if user is None:
                messagebox.showerror("Erro", "Email não cadastrado")
                self.controller.show_frame("LoginPage")
                return
            
            global logged_user
            logged_user = user
            print('enviando e-mail')
            
            self.reset_code = secrets.randbelow(1_000_000)
            try:
                emailer.send_email(to_email=email, subject="Código de recuperação Job Scraper",
                                body=f"Código de recuperação: {self.reset_code:06d}\nVolte para o app e digite o código.")
                string_recovery_code = ''
            except SMTPAuthenticationError:
                # o provedor de email pode bloquear o email
                # nesse caso, usamos um mock para enviar o email só para simular a funcionalidade
                emailer.mock_send_email(to_email=email, subject="Código de recuperação Job Scraper",
                               body=f"Código de recuperação: {self.reset_code:06d}\nVolte para o app e digite o código.")
                string_recovery_code = f"Código: {self.reset_code:06d} (tivemos que usar um mock para enviar o e-mail)"
            # Hide the email frame and show the code frame
            self.email_frame.pack_forget()
            self.code_frame.pack()
            self.recovery_code_label.config(text=string_recovery_code)
        else:
            messagebox.showerror("Erro", "E-mail inválido")
        
        # enable the email_submit button
        self.email_submit.config(state="normal")

    def resend_recovery_code(self):
        self.code_frame.pack_forget()
        self.email_frame.pack()

    def verify_code(self):
        code = self.code_entry.get()
        if code != f"{self.reset_code:06d}":
            messagebox.showerror("Erro", "Código inválido")
        else:
            # Hide the code frame and show the reset frame
            self.code_frame.pack_forget()
            self.reset_frame.pack()

    def reset_password(self):
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if len(new_password) < 1:
            messagebox.showerror("Erro", "Senha inválida")
        if new_password == confirm_password:
            global logged_user
            logged_user.password = User.generate_key(new_password)
            logged_user = update(logged_user, token=logged_user.token)
            messagebox.showinfo("Successo", "Senha trocada com sucesso")
            self.reset_frame.pack_forget()
            self.email_frame.pack()
            self.controller.show_frame("LoginPage")
        else:
            messagebox.showerror("Error", "Senhas não são iguais")


class SignUpPage(ttk.Frame):
    # Fields: Name, Surname, Username, Email, Password, Confirm Password

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Create a label and button
        label = ttk.Label(self, text="Sign Up")

        # Change font size
        label.config(font=("Courier", 30))
        label.grid(row=0, column=0, columnspan=3, sticky="n", pady=60, padx=10)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Name label
        name_label = ttk.Label(self, text="Nome")
        name_label.grid(row=1, column=0, sticky="e", padx=20, pady=5)

        # Name entry
        name_entry = ttk.Entry(self)
        name_entry.grid(row=2, column=0, sticky="e", pady=5, padx=20)

        # Surname label
        surname_label = ttk.Label(self, text="Sobrenome")
        surname_label.grid(row=1, column=1, sticky="e", padx=20, pady=5)

        # Surname entry
        surname_entry = ttk.Entry(self)
        surname_entry.grid(row=2, column=1, sticky="e", pady=5, padx=20)

        # Username label
        username_label = ttk.Label(self, text="Nome de usuário")
        username_label.grid(row=3, column=0, sticky="e", padx=20, pady=5)

        # Username entry
        username_entry = ttk.Entry(self)
        username_entry.grid(row=4, column=0, sticky="e", pady=5, padx=20)

        # Email label
        email_label = ttk.Label(self, text="Email")
        email_label.grid(row=3, column=1, sticky="e", padx=20, pady=5)

        # Email entry
        email_entry = ttk.Entry(self)
        email_entry.grid(row=4, column=1, sticky="e", pady=5, padx=20)

        # Password label
        password_label = ttk.Label(self, text="Senha")
        password_label.grid(row=5, column=0, sticky="e", padx=20, pady=5)

        # Password entry
        password_entry = ttk.Entry(self, show="*")
        password_entry.grid(row=6, column=0, sticky="e", pady=5, padx=20)

        # Confirm password label
        confirm_password_label = ttk.Label(self, text="Confirmar senha")
        confirm_password_label.grid(row=7, column=0, sticky="e", padx=20, pady=5)

        # Confirm password entry
        confirm_password_entry = ttk.Entry(self, show="*")
        confirm_password_entry.grid(row=8, column=0, sticky="e", pady=5, padx=20)

        # Sign up button
        button = ttk.Button(self, text="Cadastrar",
                            command=lambda: self.sign_up(name_entry.get(), 
                                                 surname_entry.get(), 
                                                 username_entry.get(), 
                                                 email_entry.get(), 
                                                 password_entry.get(), 
                                                 confirm_password_entry.get()))
        
        # Center the button
        button.grid(row=9, column=0, columnspan=3, sticky="n", pady=50, padx=10)

    def sign_up(self, name, surname, username, email, password, confirm_password):
        if not Emailer.is_valid_email(email):
            messagebox.showerror("Erro", "Email inválido")
            return

        if password != confirm_password:
            messagebox.showerror("Erro", "As senhas não são iguais")
            return
        
        token = str(uuid4())
        global logged_user
        logged_user = User(name, email, password, token, surname)
        logged_user = create(logged_user)
        
        # GO to the compentencies page
        self.controller.show_frame("CompentenciesPage")


class CompentenciesPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Create a label and button
        label = ttk.Label(self, text="Seleção de Competências")

        # Change font size
        label.config(font=("Courier", 30))
        label.grid(row=0, column=0, columnspan=3, sticky="n", pady=40, padx=10)

        # Create a description
        description = ttk.Label(self, text="Selecione as linguagens de programação que você domina:")
        description.grid(row=1, column=0, columnspan=3, sticky="n", pady=20, padx=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=2)

        # List of competencies
        compentencies_list = ["Python", "C", "C++", "C#", "JavaScript", "Java", "HTML", "CSS",
                              "PHP", "SQL", "Ruby", "Julia", "SPARQL", "Swift", "TypeScript", "R"]

        # Dict to store the selected competencies
        self.selected_compentencies = {}

        # Frame to hold the checkboxes
        checkboxes = ttk.Frame(self)
        checkboxes.grid(row=2, column=0, columnspan=4, pady=10)

        # Create checkboxes for each competency
        num_compentencies = len(compentencies_list)
        num_columns = 4
        num_rows = (num_compentencies + num_columns - 1) // num_columns

        for i, compentency in enumerate(compentencies_list):
            row = i // num_columns
            column = i % num_columns

            self.selected_compentencies[compentency] = tk.BooleanVar()
            ttk.Checkbutton(checkboxes, text=compentency, variable=self.selected_compentencies[compentency]).grid(row=row, column=column, sticky="w", pady=5, padx=25)

        # Confirm button
        button = ttk.Button(self, text="Confirmar", command=lambda: self.submit_selection())
        button.grid(row=num_rows + 3, column=0, columnspan=3, pady=50)

        # Button to go back to the login page
        button = ttk.Button(self, text="Voltar", command=lambda: controller.show_frame("HomePage"))
        button.grid(row=num_rows + 4, column=0, columnspan=3, pady=10)

    def submit_selection(self):

        selected_competencies =[compentency for compentency, value in self.selected_compentencies.items() if value.get()]

        # If there is no selected competency, show a message box with an error
        if len(selected_competencies) == 0:
            messagebox.showerror("Erro", "Selecione pelo menos uma competência")
            return

        skills = get_skills(token=logged_user.token)
        user_skills = get_user_skills_by_user_id(logged_user._id, token=logged_user.token)
        user_skill_ids = [user_skill[1] for user_skill in user_skills]
        for skill in skills:
            is_selected = skill.name in selected_competencies
            is_in_bd = skill._id in user_skill_ids
            if is_selected and not is_in_bd:
                create_user_skill(logged_user._id, skill._id, token=logged_user.token)
            elif not is_selected and is_in_bd:
                delete_user_skill(logged_user._id, skill._id, token=logged_user.token)
            
        # Go to the seniority level page
        self.controller.show_frame("SeniorityLevelPage")


class SeniorityLevelPage(ttk.Frame):
    
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Create a label and button
        label = ttk.Label(self, text="Nível de Senioriadade")

        # Change font size
        label.config(font=("Courier", 30))
        label.grid(row=0, column=0, columnspan=3, pady=40, padx=10)

        # Create a descritption
        description = ttk.Label(self, text="Selecione o seu nível de senioridade:")
        description.grid(row=1, column=0, columnspan=3, pady=20, padx=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=2)

        # List of seniority levels
        self.seniority_levels = ["Sem experiência", "Junior", "Pleno", "Sênior"]
        # Dict to store the selected seniority level
        self.selected_seniority_level = tk.IntVar()

        # Radio buttons to select the seniority level
        for i, seniority_level in enumerate(self.seniority_levels):
            ttk.Radiobutton(self, text=seniority_level, variable=self.selected_seniority_level, value=i).grid(row=i+2, column=0, columnspan=3, pady=5, padx=25, sticky="n")

        # Confirm button
        button = ttk.Button(self, text="Confirmar", command=lambda: self.submit_selection())
        button.grid(row=len(self.seniority_levels)+2, column=0, columnspan=3, pady=50, padx=10)

        # Button to go back to the login page
        button = ttk.Button(self, text="Voltar", command=lambda: controller.show_frame("HomePage"))
        button.grid(row=len(self.seniority_levels)+3,column=0, columnspan=3, pady=20, padx=10)
        
    def submit_selection(self):
        selected_seniority_level = self.selected_seniority_level.get()

        # If there is no selected seniority level, show a message box with an error
        if selected_seniority_level == -1:
            messagebox.showerror("Erro", "Selecione um nível de senioridade")
            return
        
        selected_seniority = self.seniority_levels[selected_seniority_level]
        
        global logged_user
        if logged_user.level != selected_seniority:
            logged_user.level = selected_seniority
            logged_user = update(logged_user, token=logged_user.token)
        
        # Go to the home page
        self.controller.show_frame("HomePage")


class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        # Create a header with buttons
        header = ttk.Frame(self)
        header.pack()

        # Button to go to the user page
        button = ttk.Button(header, text="Perfil",
                            command=lambda: controller.show_frame("UserPage"))
        button.pack(side="left", padx=30, pady=30)

        # Button to go to the compentencies page
        button = ttk.Button(header, text="Competências",
                            command=lambda: controller.show_frame("CompentenciesPage"))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Button to go to the seniority level page
        button = ttk.Button(header, text="Nível de Senioridade",
                            command=lambda: controller.show_frame("SeniorityLevelPage"))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Create a label and button
        label = ttk.Label(self, text="Home Page")

        # Change font size
        label.config(font=("Courier", 30))
        label.pack(pady=30, padx=10)    

        # Add an introduction text
        introduction = ttk.Label(self, text="Bem vindo ao nosso projeto...")
        introduction.pack(pady=10, padx=10)

        # Button to add a curriculum
        button = ttk.Button(self, text="Adicionar currículo",
                            command=lambda: controller.show_frame("AddCurriculumPage"))
        button.pack(pady=60, padx=10)

        # Button to see the list of jobs
        button = ttk.Button(self, text="Ver vagas",
                            command=lambda: controller.show_frame("JobListPage"))
        button.pack(pady=10, padx=10)


class UserPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        # Create a header with buttons
        header = ttk.Frame(self)
        header.pack()

        # Button to go to the user page
        button = ttk.Button(header, text="Home",
                            command=lambda: controller.show_frame("HomePage"))
        button.pack(side="left", padx=30, pady=30)

        # Button to go to the compentencies page
        button = ttk.Button(header, text="Competências",
                            command=lambda: controller.show_frame("CompentenciesPage"))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Button to go to the seniority level page
        button = ttk.Button(header, text="Nível de Senioridade",
                            command=lambda: controller.show_frame("SeniorityLevelPage"))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Create a label and button
        label = ttk.Label(self, text="Perfil")

        # Change font size
        label.config(font=("Courier", 30))
        label.pack(pady=30, padx=10)    

        # Frame to hold the user information
        user_info_frame = ttk.Frame(self)
        user_info_frame.pack()

        # Show the username, name and email
        username = ttk.Label(user_info_frame, text="Nome de usuário: ")
        username.pack(pady=5)
        self.name = ttk.Label(user_info_frame, text=f"Nome completo: {logged_user.name} {logged_user.last_name}")
        self.name.pack(pady=5)
        self.email = ttk.Label(user_info_frame, text=f"Email: {logged_user.email}")
        self.email.pack(pady=5)

        # Frame to edit the user information (name, surname, username, email, password, confirm password)
        edit_user_frame = ttk.Frame(self)
        edit_user_frame.pack()

        # Create two columns for the fields
        left_column = ttk.Frame(edit_user_frame)
        left_column.pack(side="left", padx=10)
        right_column = ttk.Frame(edit_user_frame)
        right_column.pack(side="left", padx=10)

        # Name label
        name_label = ttk.Label(left_column, text="Nome")
        name_label.pack()

        # Name entry
        name_entry = ttk.Entry(left_column)
        name_entry.pack()

        # Surname label
        surname_label = ttk.Label(left_column, text="Sobrenome")
        surname_label.pack()

        # Surname entry
        surname_entry = ttk.Entry(left_column)
        surname_entry.pack()

        # Username label
        username_label = ttk.Label(right_column, text="Nome de usuário")
        username_label.pack()

        # Username entry
        username_entry = ttk.Entry(right_column)
        username_entry.pack()

        # Email label
        email_label = ttk.Label(right_column, text="Email")
        email_label.pack()

        # Email entry
        email_entry = ttk.Entry(right_column)
        email_entry.pack()

        # Password label
        password_label = ttk.Label(left_column, text="Senha")
        password_label.pack()

        # Password entry
        password_entry = ttk.Entry(left_column, show="*")
        password_entry.pack()

        # Confirm password label
        confirm_password_label = ttk.Label(left_column, text="Confirmar senha")
        confirm_password_label.pack()

        # Confirm password entry
        confirm_password_entry = ttk.Entry(left_column, show="*")
        confirm_password_entry.pack()

        # Confirm button
        button = ttk.Button(edit_user_frame, text="Confirmar",
                            command=lambda: self.edit_user(name_entry.get(), 
                                                 surname_entry.get(), 
                                                 username_entry.get(), 
                                                 email_entry.get(), 
                                                 password_entry.get(), 
                                                 confirm_password_entry.get()))
        
        button.pack(pady=100, padx=50)
        
    def edit_user(self, name, surname, username, email, password, confirm_password):
        if not Emailer.is_valid_email(email):
            messagebox.showerror("Erro", "Email inválido")
            return
        
        if password != confirm_password:
            messagebox.showerror("Erro", "As senhas não são iguais")
            return
        
        global logged_user
        logged_user.name = name
        logged_user.last_name = surname
        logged_user.username = username
        logged_user.email = email
        logged_user.password = User.generate_key(password)
        
        logged_user = update(logged_user)

        messagebox.showinfo("Sucesso", "Usuário editado com sucesso")


class AddCurriculumPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        # Create a header with buttons
        header = ttk.Frame(self)
        header.pack()

        # Button to go to the user page
        button = ttk.Button(header, text="Home",
                            command=lambda: controller.show_frame("HomePage"))
        button.pack(side="left", padx=30, pady=30)

        # Button to go to the compentencies page
        button = ttk.Button(header, text="Competências",
                            command=lambda: controller.show_frame("CompentenciesPage"))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Button to go to the seniority level page
        button = ttk.Button(header, text="Nível de Senioridade",
                            command=lambda: controller.show_frame("SeniorityLevelPage"))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Create a label and button
        label = ttk.Label(self, text="Adicionar currículo")

        # Change font size
        label.config(font=("Courier", 30))
        label.pack(pady=60, padx=10)    

        # Curriculum link label
        curriculum_link_label = ttk.Label(self, text="Link do currículo")
        curriculum_link_label.pack(pady=10, padx=10)

        # Curriculum link entry
        curriculum_link_entry = ttk.Entry(self)
        curriculum_link_entry.pack(pady=10, padx=10)

        # Add curriculum button
        button = ttk.Button(self, text="Adicionar",
                            command=lambda: self.add_curriculum(curriculum_link_entry.get()))
        
        button.pack(pady=60, padx=10)

    def add_curriculum(self, curriculum_link):
        file_link = get_file_links_by_user_id(logged_user._id, token=logged_user.token)
        if file_link is not None and len(file_link) > 0:
            file_link = file_link[0]
            file_link.link = curriculum_link
            file_link = update_file_link(file_link, token=logged_user.token)
        else:
            file_link = FileLink(curriculum_link, logged_user._id)
            file_link = create_file_link(file_link, token=logged_user.token)
        
        messagebox.showinfo("Sucesso", "Currículo adicionado com sucesso")


class JobListPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
         
        # Create a header with buttons
        header = ttk.Frame(self)
        header.pack()

        # Button to go to the user page
        button = ttk.Button(header, text="Home",
                            command=lambda: controller.show_frame("HomePage"))
        button.pack(side="left", padx=30, pady=30)

        # Button to go to the compentencies page
        button = ttk.Button(header, text="Competências",
                            command=lambda: controller.show_frame("CompentenciesPage"))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Button to go to the seniority level page
        button = ttk.Button(header, text="Nível de Senioridade",
                            command=lambda: controller.show_frame("SeniorityLevelPage"))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Divide the frame into left and right panels
        self.left_panel = ttk.Frame(self, width=400)
        self.right_panel = ttk.Frame(self)

        self.left_panel.pack(side='left', fill='y')
        self.right_panel.pack(side='right', fill='both', expand=True)

        # Create a label to be used while the job list dataframe is being made
        self.loading_label = ttk.Label(self.left_panel, text="Buscando as melhores vagas para você...")
        self.loading_label.pack(pady=10)

        # Simulate asking for a dataframe of jobs
        self.after(2000, self.load_data)

    def load_data(self):
        """Load the data from the dataframe into the GUI"""
        user_skill_ids = get_user_skills_by_user_id(logged_user._id, token=logged_user.token)
        skills_and_competency = [logged_user.level]
        for user_skill_id in user_skill_ids:
            skill_id = user_skill_id[1]
            skill = get_skills(skill_id, token=logged_user.token)
            skills_and_competency.append(skill)
        
        scraper = JobScraper()
        scraper.set_options("site_names", ["LinkedIn", "Indeed"])
        scraper.set_options("job_types", ["Tempo integral"])
        scraper.set_options("locations", ["Rio de Janeiro"])
        scraper.set_options("keywords", skills_and_competency)
        scraper.set_options("remote_options", ["Trabalho remoto"])
        scraper.get_jobs()
        
        jobs = scraper.jobs
        
        # Remove the loading label
        self.loading_label.destroy()

        # Call the function to display the data
        self.display_data(jobs)

        # Create widgets for the right panel
        self.setup_right_panel()

    def display_data(self, jobs):
        """Display the data in the GUI as cards on the left panel"""
        # Create a canvas and a scrollbar on the left panel
        canvas = tk.Canvas(self.left_panel)
        scrollbar = ttk.Scrollbar(self.left_panel, orient='vertical', command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw', width=400)

        # Pack the canvas and scrollbar on the left panel
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        self.emails = []
        # Add job data to the scrollable frame as cards
        for _, job in jobs.iterrows():
            self.create_job_card(job)

    def create_job_card(self, job):
        """Create a card for each job."""
        card_frame = ttk.Frame(self.scrollable_frame, borderwidth=1, relief='solid', padding=10)
        card_frame.pack(padx=10, pady=10, fill='x', expand=True)

        ttk.Label(card_frame, text=job['title'], font=('Arial', 16, 'bold')).pack(anchor='w', fill='x')
        ttk.Label(card_frame, text=job['company'], font=('Arial', 14)).pack(anchor='w', fill='x')
        ttk.Label(card_frame, text=job['location'], font=('Arial', 12)).pack(anchor='w', fill='x')
        if "emails" in job and job['emails'] is not None:
            self.emails.append(job['emails'])
        link_label = ttk.Label(card_frame, text=job['job_url'], font=('Arial', 10), foreground='blue', cursor='hand2')
        link_label.pack(anchor='w', fill='x')
        link_label.bind("<Button-1>", lambda e, link=job['job_url']: self.open_link(link))

    def open_link(self, link):
        """Open a link in the web browser."""
        webbrowser.open_new(link)

    def setup_right_panel(self):
        """Set up the right panel with a label, text entry, and a button."""
        ttk.Label(self.right_panel, text="Envie um e-mail para as vagas selecionadas:").pack(pady=(20, 10))
        self.email_text = tk.Text(self.right_panel, height=10)
        self.email_text.pack(padx=20, pady=10, fill='x', expand=False)
        self.send_email_button = ttk.Button(self.right_panel, text="Enviar", command=self.send_email)
        self.send_email_button.pack(pady=10)

    def send_email(self):
        """Function to handle sending an email."""
        # Here you would implement the functionality to send an email
        # For now, it will simply print the email text to the console
        email_content = self.email_text.get('1.0', tk.END)
        if logged_user is not None:
            curriculum = get_file_links_by_user_id(logged_user._id,token=logged_user.token)
            if curriculum is not None:
                email_content +="\nLink para o meu currículo: "+curriculum[0].name
        
        emailer = Emailer()
        if len(self.emails)>0: 
            for email in self.emails:
                try:
                    emailer.mock_send_email(to_email=email, subject="Encontrei sua vaga Usando o Job Scraper",
                                    body=email_content)
                    string_recovery_code = ''
                except SMTPAuthenticationError:
                    # o provedor de email pode bloquear o email
                    # nesse caso, usamos um mock para enviar o email só para simular a funcionalidade
                    emailer.mock_send_email(to_email=email, subject="Encontrei sua vaga Usando o Job Scraper",
                                    body=email_content)
                messagebox.showinfo("Email", f"Email enviado com sucesso para {email}")
        else: 
            messagebox.showerror("Erro", "nenhuma empresa tem email registrado.")
                

# TODO: add placeholders on the entry fields (ex: email)