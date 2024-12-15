class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

        if not  isinstance (name, str):
            raise TypeError("Name must be a string")
        if len(name) < 2 or len(name) > 16: 
            raise ValueError("Name must be between 2 and 16 characters long")
        
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be between 2 and 16 characters long")

    @property
    def category( self, value) : 
        if isinstance (value, str) and len(value) > 0: 
            self._category = value
        else:
            raise ValueError("Category must be longer than 0 characters")





    def __repr__(self):
        return f'<Magazine {self.name}>'
