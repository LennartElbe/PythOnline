"""movies, Aufgabe 1

Problem 1: movies.py

Authors:
    Lennart Elbe <lenni.elbe@gmail.com>

.. _`Python Standard Library`:
    https://docs.python.org/3.7/library
"""


class Movie:
    def __init__(self, title, year, rating):
        """Takes in arguments for title, year of release, and rating of a movie.

        Arguments:
            title {str} -- The title of the movie.
            year {int} -- The year of the movie's release
            rating {float} -- The movie's rating on a scale of 1-10.

        Notes: none

        Examples:
            >>> m = Movie("Groundhog Day", 1993, 8.0)
            >>> m.title, m.year, m.rating
            ('Groundhog Day', 1993, 8.0)
        """

        self.title = title
        self.year = year
        self.rating = rating


m = Movie('Groundhog day', 1993, 8.0)
print(m.title, m.year, m.rating)


def movie_str(movie):
    """Takes an object of class Movie and prints the attributes thereof.

    Arguments:
        movie {Movie} -- A movie with a title, a year, and a rating.

    Returns:
        str -- Prints human readable version of the movie information.
    """

    return "Movie('%s', %d, %.1f)" % (movie.title, movie.year, movie.rating)


print(movie_str(m))


def avg_score(movies):
    """Calculate average rating of a list of movies.

    Arguments:
        movies {list} -- Movies with a title, a year of release, and a rating.

    Returns:
        float -- The average rating of all the movies.

    Examples:
        >>> movies = [Movie("Groundhog Day", 1993, 8.0),
                     Movie('The Life Aquatic with Steve Zissou', 2004, 7.3),
                     Movie('Tootsie', 1982, 7.4)]
        >>> abs(avg_score(movies) - 7.566666) < 1e-4
        True
    """

    sum = 0
    for i in movies:
        sum += i.rating
    return sum/len(movies)


movies = [
    Movie("Groundhog Day", 1993, 8.0),
    Movie('The Life Aquatic with Steve Zissou', 2004, 7.3),
    Movie('Tootsie', 1982, 7.4)]

print(abs(avg_score(movies) - 7.566666) < 1e-4)


class Actor:
    def __init__(self, firstname, lastname, movies):
        """Creates a object of class Actor with attributes firstname, lastname,
        and list of movies.

        Arguments:
            firstname {str} -- The actor's first name.
            lastname {str} -- The actor's last name.
            movies {list} -- The list of movies the actor has played a part in.

        Examples:
            >>> bill = Actor('Bill', 'Murray', [Movie('Tootsie', 1982, 7.4)])
            >>> bill.firstname, bill.lastname, len(bill.movies)
            ('Bill', 'Murray', 1)
        """

        self.firstname = firstname
        self.lastname = lastname
        self.movies = movies


bill = Actor('Bill', 'Murray', [Movie('Tootsie', 1982, 7.4)])
print(bill.firstname, bill.lastname, len(bill.movies))


def worst_actor(actors):
    """Determines the actor with the lowest average movie rating.

    Arguments:
        actors {list} -- A list of actors containing the actor's first name,
        last name, and a list of movies they play in.

    Returns:
        Actor -- The actor with the lowest average movie rating.

    Examples:
        >>> actors = [
                Actor('Bill', 'Murray', [
                    Movie('Groundhog Day', 1993, 8.0),
                    Movie('The Life Aquatic with Steve Zissou', 2004, 7.3),
                    Movie('Tootsie', 1982, 7.4)]),
                Actor('Steven', 'Seagal', [
                    Movie('Black Dawn', 2005, 3.9),
                    Movie('Exit Wounds', 2001, 5.5),
                    Movie('The Patriot', 1998, 4.1)]),
                Actor('Ben', 'Kingsley', [
                    Movie('Sexy Beast', 2000, 7.3),
                    Movie('Lucky Number Slevin', 2006, 7.8)])]
        >>> worst_actor(actors).firstname
        'Steven'
    """

    min_score = avg_score(actors[0].movies)
    min_actor = actors[0]
    for i in actors:
        avgscore = avg_score(i.movies)
        if min_score > avgscore:
            min_score = avgscore
            min_actor = i
    return min_actor


actors = [Actor('Bill', 'Murray', [
    Movie('Groundhog Day', 1993, 8.0),
    Movie('The Life Aquatic with Steve Zissou', 2004, 7.3),
    Movie('Tootsie', 1982, 7.4)]),
    Actor('Steven', 'Seagal', [
        Movie('Black Dawn', 2005, 3.9),
        Movie('Exit Wounds', 2001, 5.5),
        Movie('The Patriot', 1998, 4.1)]),
    Actor('Ben', 'Kingsley', [
        Movie('Sexy Beast', 2000, 7.3),
        Movie('Lucky Number Slevin', 2006, 7.8)])]
print(worst_actor(actors).firstname)
