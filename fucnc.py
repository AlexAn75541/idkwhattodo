



def add_movie(title, director, year):
    list_of_movies = []
    movie_info = f"{title} directed by {director} released in {year}"
    list_of_movies.append(movie_info)
    return list_of_movies




def search_movie(movies, title):
    for movie in movies:
        if title in movie:
            return movie
    return "Movie not found"