class Author:
    def __init__(self, id, name):

        self.id = id
        self.name = name

        if not isinstance(name, str):
            raise TypeError("Name must be a string")

    def __repr__(self):
        return f'<Author {self.name}>'
   