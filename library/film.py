class Film:
    def __init__(self, id, title, genre, rating):
        self.id = id
        self.title = title
        self.genre = genre
        self.rating = rating

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self) -> str:
        return f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}"
