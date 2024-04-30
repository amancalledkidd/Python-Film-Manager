import pytest
from project import list_films, add_film, delete_film
from library.film import Film

#Mock film repo to help test functions
class MockFilmRepo:
    def __init__(self, films):
        self.films = films

    def all(self):
        return self.films

    def add(self, film):
        self.films.append(film)

    def find_by_title(self, title):
        for film in self.films:
            if film.title.lower() == title.lower():
                return film
        return None

    def delete(self, film_id):
        for i, film in enumerate(self.films):
            if film.id == film_id:
                del self.films[i]
                return True
            return false


@pytest.fixture
def film_repo():
    films = [Film(1, "Film1", "Test", "5"), Film(2, "Film2", "Test", "7")]
    repo = MockFilmRepo(films)
    return repo


def test_list_films(film_repo):

    expected_result = (
        "Title    Genre      Rating\n"
        "-------  -------  --------\n"
        "Film1    Test            5\n"
        "Film2    Test            7"
        )
    assert list_films(film_repo) == expected_result

def test_add_film(film_repo):
    add_film(film_repo, "Film3", "Test", "10")
    expected_result = (
        "Title    Genre      Rating\n"
        "-------  -------  --------\n"
        "Film1    Test            5\n"
        "Film2    Test            7\n"
        "Film3    Test           10"
        )
    assert list_films(film_repo) == expected_result

def test_delete_film(film_repo):
    delete_film(film_repo, "Film1")
    expected_result = (
        "Title    Genre      Rating\n"
        "-------  -------  --------\n"
        "Film2    Test            7"
        )
    assert list_films(film_repo) == expected_result
    assert delete_film(film_repo, "Film1") == "\n'Film1' not found, please check spelling!"

