MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movies():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director :")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year,
    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f'Title: {movie["title"]}')
    print(f'Director: {movie["director"]}')
    print(f'Year: {movie["year"]}')
    print('\n')


def find_movies():
    search_title = input("Enter the movie you're looking for: ")

    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)


user_options = {
    'a': add_movies,
    'l': show_movies,
    'f': find_movies,
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')
        selection = input(MENU_PROMPT)


menu()
