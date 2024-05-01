# Film Database

#### Video Demo:
For a visual walkthrough of the Film Database in action, check out [video demo](https://www.youtube.com/watch?v=SsVoAMPXLeI).

#### Description:

## Overview
The Film Database is an interactive, user-friendly system designed to help movie lovers manage and track their personal movie collections.

## How It Works
At its core, the Film Database is built with a SQLite backend, Python’s object-oriented programming capabilities, and the principles of test-driven development. The goal was to create a reliable and efficient system to store and manage a user's film data with ease.

### Files and Functionality

#### `film.py`
The `film.py` file contains the `Film` class, which acts as the blueprint for creating and managing the information of each film. Each `Film` object holds the properties title, genre and rating.

#### `film_repository.py`
The `film_repository.py` file defines the `FilmRepository` class. This is where the logic for interfacing with the database lives. The class provides methods for adding, retrieving and deleting film records, managing the persistence of the film data.

#### `db_connection.py`
The `db_connection.py` file is home to the `DatabaseConnection` class. It's tasked with handling the lower-level operations like connecting to the SQLite database, executing SQL queries, and seeding the databases.

### Design Choices
One of the main design decisions was choosing SQLite over other database systems. The rationale was that it comes standard with python so it’s lightweight and requires zero-configuration, which makes it an ideal choice for smaller projects like this one. While I considered using a CSV file for simplicity, I wanted the opportunity to learn more about databases.

Another significant choice was to implement object-oriented programming. This approach promotes better organisation and scalability, allowing for future enhancements like integrating more complex features and allowed me to learn more about this programming style.

The most impactful design choice in this project was the adoption of Test-Driven Development (TDD). TDD was instrumental not just in ensuring a bug-free application, but also in helping me learn more about what I was building. It was a discipline that initially required restraint and patience but lead to a better quality of code.

### Conclusion
The development of this Film Database has been an instructive journey. It afforded me a valuable opportunity to engage with new concepts such as class structures, database connectivity, and the discipline of test-driven development. Each step, while challenging, contributed to a broader understanding of software development practices.

The progression from concept to functional tool was gradual and required careful consideration of each feature and its implementation. The choice to use test-driven development ensured dependable classes, reinforcing the importance of thorough testing and incremental progress.

In retrospect, the project not only served as a means to an end but also as a significant learning experience. It has laid a foundation for future endeavours in the field of software development and has reinforced the virtues of patience and precision in coding.

I take pride in the functionality and utility of the Film Database, which began as a simple idea and has evolved into a useful resource for film enthusiasts. The project encapsulates the technical skills and dedication applied throughout its creation and stands as a representation of both the challenges faced and the knowledge gained.

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/amancalledkidd/Python-Film-Manager.git
    ```

2. **Navigate to the project directory:**

    ```sh
    cd Python-Film-Manager
    ```

3. **Install dependencies:**

    Assuming you are using pip, run:

    ```sh
    pip install tabulate
    ```

4. **Run the project file:**

    ```sh
    python.py
    ```


