


class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

        if not isinstance(title, str):
          raise TypeError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise TypeError("Title must be between 5 and 50 characterslong")
        
        if not isinstance(content, str):
            raise TypeError("Content must be a string")
        if len(content) == 0:
            raise TypeError("Content must not be empty")
        


    def __repr__(self):
        return f'<Article {self.title}>'
