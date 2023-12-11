import tkinter as tk

from tkinter import messagebox, ttk

class StartPage(tk.Frame):
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
                            command=lambda: controller.show_frame(LoginPage))

        button.pack(pady=40, padx=10, ipadx=20)

class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

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

        # TODO: add a email validation callback

        # Password label
        password_label = ttk.Label(self, text="Senha")
        password_label.pack()

        # Password entry
        password_entry = ttk.Entry(self, show="*")
        password_entry.pack()

        # Forgot password
        forgot_password = tk.Label(self, text="Esqueceu sua senha?", fg="blue", background="#111")
        forgot_password.bind("<Button-1>", lambda: controller.show_frame(ForgotPasswordPage))
        forgot_password.pack(padx=20, pady=5)

        # Sign in button
        button = ttk.Button(self, text="Entrar",
                            command=lambda: print("Email: {}\nPassword: {}".format(email_entry.get(), password_entry.get())))
        # Change font
        button.pack(pady=10)

        # TODO: add a login validation on database callback

        # Sign up button
        button = ttk.Button(self, text="Não tem conta? Cadastre-se",
                            command=lambda: controller.show_frame(SignUpPage))

        button.pack(padx=100, pady=100, ipadx=20)

class ForgotPasswordPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        # Create a label and button
        label = ttk.Label(self, text="Change Password")

        # Change font size
        label.config(font=("Courier", 30))
        label.pack(pady=60, padx=10)   

        # Frame for Email Address Input
        self.email_frame = ttk.Frame(self)
        ttk.Label(self.email_frame, text="Enter your email address").pack()
        self.email_entry = ttk.Entry(self.email_frame)  # TODO: add email validation callback
        self.email_entry.pack()
        email_submit = ttk.Button(self.email_frame, text="Submit",
                                 command=lambda: self.send_recovery_code)
        email_submit.pack(pady=50)
        self.email_frame.pack()

        # Frame for Code Verification
        self.code_frame = ttk.Frame(self)
        ttk.Label(self.code_frame, text="Enter the code you received").pack() 
        self.code_entry = ttk.Entry(self.code_frame) # Add a code structure validation callback
        self.code_entry.pack()
        code_submit = ttk.Button(self.code_frame, text="Submit",
                                command=lambda: self.verify_code)
        code_submit.pack()
        resend_code = ttk.Button(self.code_frame, text="Resend Code",
                                command=lambda: self.send_recovery_code)
        resend_code.pack()

        # Frame for Password Reset
        self.reset_frame = ttk.Frame(self)
        tk.Label(self.reset_frame, text="Enter your new password").pack()
        self.new_password_entry = ttk.Entry(self.reset_frame, show="*")
        self.new_password_entry.pack() # TODO: add a password validation callback
        tk.Label(self.reset_frame, text="Confirm your new password").pack()
        self.confirm_password_entry = ttk.Entry(self.reset_frame, show="*")
        self.confirm_password_entry.pack() # TODO: add a password match validation callback
        reset_submit = ttk.Button(self.reset_frame, text="Reset Password",
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
        
        # TODO: add the sign up logic
        
        
        # GO to the compentencies page
        self.controller.show_frame(CompentenciesPage)

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
        button = ttk.Button(self, text="Voltar", command=lambda: controller.show_frame(LoginPage))
        button.grid(row=num_rows + 4, column=0, columnspan=3, pady=10)

    def submit_selection(self):

        selected_competencies =[compentency for compentency, value in self.selected_compentencies.items() if value.get()]
        print(selected_competencies)

        # TODO: add the validation for no selected compentencies

        # Go to the seniority level page
        self.controller.show_frame(SeniorityLevelPage)

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
        seniority_levels = ["Sem experiência", "Junior", "Pleno", "Sênior"]
        # Dict to store the selected seniority level
        self.selected_seniority_level = tk.IntVar()

        # Radio buttons to select the seniority level
        for i, seniority_level in enumerate(seniority_levels):
            ttk.Radiobutton(self, text=seniority_level, variable=self.selected_seniority_level, value=i).grid(row=i+2, column=0, columnspan=3, pady=5, padx=25, sticky="n")

        # Confirm button
        button = ttk.Button(self, text="Confirmar", command=lambda: self.submit_selection())
        button.grid(row=len(seniority_levels)+2, column=0, columnspan=3, pady=50, padx=10)

        # Button to go back to the login page
        button = ttk.Button(self, text="Voltar", command=lambda: controller.show_frame(LoginPage))
        button.grid(row=len(seniority_levels)+3,column=0, columnspan=3, pady=20, padx=10)
        
    def submit_selection(self):
        selected_seniority_level = self.selected_seniority_level.get()

        # TODO: add the validation for no selected seniority level

        # Go to the home page
        self.controller.show_frame(HomePage)

class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        # Create a header with buttons
        header = ttk.Frame(self)
        header.pack()

        # Button to go to the user page
        button = ttk.Button(header, text="Perfil",
                            command=lambda: controller.show_frame(UserPage))
        button.pack(side="left", padx=30, pady=30)

        # Button to go to the compentencies page
        button = ttk.Button(header, text="Competências",
                            command=lambda: controller.show_frame(CompentenciesPage))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Button to go to the seniority level page
        button = ttk.Button(header, text="Nível de Senioridade",
                            command=lambda: controller.show_frame(SeniorityLevelPage))
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
                            command=lambda: controller.show_frame(AddCurriculumPage))
        button.pack(pady=60, padx=10)

        # Button to see the list of jobs
        button = ttk.Button(self, text="Ver vagas",
                            command=lambda: controller.show_frame(JobListPage))
        button.pack(pady=10, padx=10)

class UserPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        # Create a header with buttons
        header = ttk.Frame(self)
        header.pack()

        # Button to go to the user page
        button = ttk.Button(header, text="Home",
                            command=lambda: controller.show_frame(HomePage))
        button.pack(side="left", padx=30, pady=30)

        # Button to go to the compentencies page
        button = ttk.Button(header, text="Competências",
                            command=lambda: controller.show_frame(CompentenciesPage))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Button to go to the seniority level page
        button = ttk.Button(header, text="Nível de Senioridade",
                            command=lambda: controller.show_frame(SeniorityLevelPage))
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
        name = ttk.Label(user_info_frame, text="Nome completo: ")
        name.pack(pady=5)
        email = ttk.Label(user_info_frame, text="Email: ")
        email.pack(pady=5)

        # TODO: add the user information

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

        pass

        # TODO: add the logic to edit the user information, and show a message box with the result

class AddCurriculumPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        # Create a header with buttons
        header = ttk.Frame(self)
        header.pack()

        # Button to go to the user page
        button = ttk.Button(header, text="Home",
                            command=lambda: controller.show_frame(HomePage))
        button.pack(side="left", padx=30, pady=30)

        # Button to go to the compentencies page
        button = ttk.Button(header, text="Competências",
                            command=lambda: controller.show_frame(CompentenciesPage))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Button to go to the seniority level page
        button = ttk.Button(header, text="Nível de Senioridade",
                            command=lambda: controller.show_frame(SeniorityLevelPage))
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

        print(curriculum_link)

        # TODO: add the logic to add the curriculum, and show a message box with the result        

class JobListPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        # Create a header with buttons
        header = ttk.Frame(self)
        header.pack()

         # Button to go to the user page
        button = ttk.Button(header, text="Home",
                            command=lambda: controller.show_frame(HomePage))
        button.pack(side="left", padx=30, pady=30)

        # Button to go to the compentencies page
        button = ttk.Button(header, text="Competências",
                            command=lambda: controller.show_frame(CompentenciesPage))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Button to go to the seniority level page
        button = ttk.Button(header, text="Nível de Senioridade",
                            command=lambda: controller.show_frame(SeniorityLevelPage))
        button.pack(side="left", padx=30, pady=30, ipadx=10)

        # Create a label and button
        label = ttk.Label(self, text="Lista de vagas")

        # Change font size
        label.config(font=("Courier", 30))
        label.pack(pady=60, padx=10) 

        # TODO: add the logic to retrieve the jobs from the database (and show them on the screen)

# TODO: add placeholders on the entry fields (ex: email)