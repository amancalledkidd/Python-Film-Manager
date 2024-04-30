from library.database_connection import DatabaseConnection
from library.film_repository import FilmRepository
from library.film import Film
from tabulate import tabulate



def main():
    db_conn = DatabaseConnection("project.db")
    db_conn.seed("seeds/film_library.sql")
    film_repo = FilmRepository(db_conn)
    print("\n\nWelcome to the Film Manager 3000")
    shutdown = False

    while not shutdown:
        action = input("\n\nWhat would you like to do? \n\n1) List all films\n2) Add new film\n3) Delete film\n4) Shutdown\n")
        if action == "1":
            print(f"\n\n{list_films(film_repo)}")
        elif action == "2":
            title = input("Please enter name of film: ").strip()
            genre = input("Please enter genre: ").strip()
            rating = input("Please rate the film 1(Bad) to 10(Good): ").strip()
            print(add_film(film_repo, title, genre, rating))
        elif action == "3":
            film_title = input("Film title: ")
            print(delete_film(film_repo, film_title))
        elif action == "4":
            print("\n\n....\n\nFilm Manager shutting down.\n\n")
            shutdown = True



def list_films(film_repo):
    films = film_repo.all()
    data =[["Title", "Genre", "Rating"]]
    for film in films:
        data.append([film.title, film.genre, film.rating])

    table = tabulate(data, headers='firstrow')
    return table



def add_film(film_repo, title, genre, rating):
    return film_repo.add(Film(None, title, genre, rating))




def delete_film(film_repo, film_title):
    film_data = film_repo.find_by_title(film_title.lower().strip())

    if film_data is not None:
        film_repo.delete(film_data.id)
        return f"\n{film_data.title} deleted!"
    else:
        return f"\n'{film_title}' not found, please check spelling!"




if __name__ == "__main__":
    main()

