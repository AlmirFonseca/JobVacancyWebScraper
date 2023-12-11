from pages import (StartPage, LoginPage, ForgotPasswordPage, 
                   SignUpPage, CompentenciesPage, SeniorityLevelPage, 
                   HomePage, UserPage, AddCurriculumPage, JobListPage)


class PageFactory:
    def __init__(self, container, controller):
        self.container = container
        self.controller = controller

    def create_page(self, page_type):
        if page_type == "StartPage":
            frame = StartPage(self.container, self.controller)
            frame.grid(row=0, column=0, sticky="nsew")
            return frame
    
        elif page_type == "LoginPage":
            frame = LoginPage(self.container, self.controller)
            frame.grid(row=0, column=0, sticky="nsew")
            return frame
        
        elif page_type == "ForgotPasswordPage":
            frame = ForgotPasswordPage(self.container, self.controller)
            frame.grid(row=0, column=0, sticky="nsew")
            return frame
        
        elif page_type == "SignUpPage":
            frame = SignUpPage(self.container, self.controller)
            frame.grid(row=0, column=0, sticky="nsew")
            return frame
        
        elif page_type == "CompentenciesPage":
            frame = CompentenciesPage(self.container, self.controller)
            frame.grid(row=0, column=0, sticky="nsew")
            return frame
        
        elif page_type == "SeniorityLevelPage":
            frame = SeniorityLevelPage(self.container, self.controller)
            frame.grid(row=0, column=0, sticky="nsew")
            return frame
        
        elif page_type == "HomePage":
            frame = HomePage(self.container, self.controller)
            frame.grid(row=0, column=0, sticky="nsew")
            return frame
        
        elif page_type == "UserPage":
            frame = UserPage(self.container, self.controller)
            frame.grid(row=0, column=0, sticky="nsew")
            return frame
        
        elif page_type == "AddCurriculumPage":
            frame = AddCurriculumPage(self.container, self.controller)
            frame.grid(row=0, column=0, sticky="nsew")
            return frame
        
        elif page_type == "JobListPage":
            frame = JobListPage(self.container, self.controller)
            frame.grid(row=0, column=0, sticky="nsew")
            return frame
        
        else:
            raise ValueError("Invalid page type")