from library.film_repository import FilmRepository
from library.film import Film
from library.database_connection import DatabaseConnection
import pytest


@pytest.fixture
def db_connection():
    conn = DatabaseConnection("test.db")
    yield conn


def test_fetch_all(db_connection):
    db_connection.seed("seeds/film_library.sql")
    repo = FilmRepository(db_connection)

    films = repo.all()
    assert films == [
        Film(1, 'The Grand Odyssey', 'Adventure', 8),
        Film(2, 'Mystery of the Blue Moon', 'Mystery', 7),
        Film(3, 'Gardens of Time', 'Sci-Fi', 9)
    ]


def test_add(db_connection):
    db_connection.seed("seeds/film_library.sql")
    repo = FilmRepository(db_connection)

    assert repo.add(Film(None, 'Pulp Fiction', 'Action', 9)) == "Film added"
    assert repo.all() == [
        Film(1, 'The Grand Odyssey', 'Adventure', 8),
        Film(2, 'Mystery of the Blue Moon', 'Mystery', 7),
        Film(3, 'Gardens of Time', 'Sci-Fi', 9),
        Film(4, 'Pulp Fiction', 'Action', 9 )
    ]


def test_find_by_id(db_connection):
    db_connection.seed("seeds/film_library.sql")
    repo = FilmRepository(db_connection)

    assert repo.find_by_id(2) == Film(2, 'Mystery of the Blue Moon', 'Mystery', 7)


def test_delete(db_connection):
    db_connection.seed("seeds/film_library.sql")
    repo = FilmRepository(db_connection)

    assert repo.delete(2) is None
    assert repo.all() == [
        Film(1, 'The Grand Odyssey', 'Adventure', 8),
        Film(3, 'Gardens of Time', 'Sci-Fi', 9)
    ]


def test_find_by_title(db_connection):
     db_connection.seed("seeds/film_library.sql")
     repo = FilmRepository(db_connection)

     assert repo.find_by_title('gardens of time') == Film(3, 'Gardens of Time', 'Sci-Fi', 9)


# def test_update(db_connection):
#     db_connection.seed("seeds/film_library.sql")
#     repo = FilmRepository(db_connection)

#     repo.update()

