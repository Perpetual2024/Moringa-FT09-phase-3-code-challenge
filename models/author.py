from database.connection import get_db_connection



class Author:
    def __init__(self, id, name):

        self._id = id
        self._name = name

        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        
        conn = get_db_connection()
        cursor = conn.cursor()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name cannot be changed")

    @property
    def id(self):
        if not isinstance(self._id, int):
            raise TypeError("ID must be of type int.")
        return self._id


    @id.setter
    def id(self, value):
        raise AttributeError("ID cannot be changed")


    def __repr__(self):
        return f'<Author {self.name}>'
   