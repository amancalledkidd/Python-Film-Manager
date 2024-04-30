from library.film import Film

class FilmRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM films')
        films = []
        for row in rows:
            item = Film(row["id"], row["title"], row["genre"], row["rating"])
            films.append(item)
        return films


    def add(self, film):
        rows = self._connection.execute('INSERT INTO films (title, genre, rating) VALUES (?, ?, ?)', [film.title, film.genre, film.rating])
        return "Film added"


    def find_by_id(self, id):
        row = self._connection.execute('SELECT * FROM films where id = ?', [id])
        film = Film(row[0]["id"], row[0]["title"], row[0]["genre"], row[0]["rating"])
        return film


    def find_by_title(self, title):
        rows = self._connection.execute('SELECT * FROM films WHERE LOWER(title) = ?', [title])
        if not rows:
            return None
        else:
            row = rows[0]
            film = Film(row["id"], row["title"], row["genre"], row["rating"])
            return film


    def delete(self, id):
        self._connection.execute('DELETE FROM films where id = ?', [id])
        return None


