class Author:
    def __init__(self, id, name):

        self.id = id
        self.name = name

        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")

    @property
    def name(self):
        return self._name


    def __repr__(self):
        return f'<Author {self.name}>'
   