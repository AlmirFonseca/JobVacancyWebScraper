class Skill:
    def __init__(self, name: str, id: int = None):
        """
        Initialize the Skill object
        self.name: skill name
        self._id: skill id used to identify the skill in the database
        """
        self.name = name
        self._id = id