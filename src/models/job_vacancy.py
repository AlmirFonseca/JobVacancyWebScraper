class JobVacancy:
    def __init__(self, name: str, email: str, link: str, id: int = None):
        """
        Initialize the JobVacancy object
        self.name: job vacancy name
        self.email: job vacancy email address
        self.link: job vacancy link
        self._id: job vacancy id used to identify the job vacancy in the database
        """
        self.name = name
        self.email = email
        self.link = link
        self._id = id