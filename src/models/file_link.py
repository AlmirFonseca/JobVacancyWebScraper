class FileLink:
    def __init__(self, name: str, user_id: int, id: int = None):
        """
        Initialize the FileLink object
        self.name: file link name
        self.user_id: user id
        self._id: file link id used to identify the file link in the database
        """
        self.name = name
        self.user_id = user_id
        self._id = id