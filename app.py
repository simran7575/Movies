MENU_PROMPT = "\n Enter 'a' to add movies, 'l' to see your movies, 'f' to find a movie by title, 'q' to quit: "
movies = []


def add_movie():
    title = input('Enter the movie title: ')
    director = input('Enter the movie director: ')
    year = input('Enter the movie release year: ')

    movies.append(
        {'title': title,
         'director': director,
         'year': year}
    )


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"title: {movie['title']}")
    print(f"director: {movie['director']}")
    print(f"year: {movie['year']}")


def find_movie():
    search_title = input('Enter movie title you are looking for: ')
    for movie in movies:
        if movie['title'] ==search_title:
            print_movie(movie)


user_option = {
    'a': add_movie,
    'l': show_movies,
    'f': find_movie
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_option:
            option = user_option[selection]
            option()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()
