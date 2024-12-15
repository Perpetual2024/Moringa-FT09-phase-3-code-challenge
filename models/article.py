from database.connection import get_db_connection


class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._idid = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id

        if not isinstance(title, str):
          raise TypeError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise TypeError("Title must be between 5 and 50 characterslong")
        
        if not isinstance(content, str):
            raise TypeError("Content must be a string.")
        if len(content) == 0:
            raise TypeError("Content must not be empty.")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ? ,?)", (title, content, author_id, magazine_id))
        conn.commit()
        conn.close()
        


    def __repr__(self):
        return f'<Article {self.title}>'
