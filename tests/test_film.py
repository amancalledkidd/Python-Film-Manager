from library.film import Film

def test_init():
    film = Film(5, "Matrix", "Sci-Fi", 9)
    assert film.id == 5
    assert film.title == "Matrix"
    assert film.genre == "Sci-Fi"
    assert film.rating == 9

def test_equality():
    film_1 = Film(5, "Matrix", "Sci-Fi", 9)
    film_2 = Film(5, "Matrix", "Sci-Fi", 9)
    assert film_1 == film_2


def test_string_format():
    film_1 = Film(5, "Matrix", "Sci-Fi", 9)
    assert str(film_1) == "Title: Matrix, Genre: Sci-Fi, Rating: 9"
