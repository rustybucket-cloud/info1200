import csv
import sys

FILENAME = "movies_test.csv"

# exits the program
def exit_program():
    print("Terminating program.")
    sys.exit()

# reads the movie file
def read_movies():
    # tests if file exists, returns movies if exists, returns empty if doesn't
    try:
        movies = []
        # adds each movie to movie list
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
                # returns movies
        return movies
    # runs if file not found
    except FileNotFoundError as e:
        """ print(f"Could not find {FILENAME} file.")
        exit_program() """
        # returns empty array
        return movies
    # runs on any other exception
    except Exception as e:
        # prints error and exits program
        print(type(e), e)
        exit_program()

# writes new movies to file
def write_movies(movies):
    # tries to write to file
    try:
        # writes movies to file
        with open(FILENAME, "w", newline="") as file:
            ## raise BlockingIOError("Testing the OSError exception")
            writer = csv.writer(file)
            writer.writerows(movies)
    # exception for OS errors
    except OSError as e:
        # prints error and exits program
        print(type(e), e)
        exit_program()
    # catches all exceptions
    except Exception as e:
        # print exception type and exit program
        print(type(e), e)
        exit_program()

# list all movies in file
def list_movies(movies):
    # prints each movie and year
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()
    
# adds new movie to array
def add_movie(movies):
    name = input("Name: ")
    while True:
        # tests if year input is an integer
        try:
            year = int(input("Year: "))
        # if year input is not an integer
        except ValueError:
            print("Enter a valid year.")
            continue
        # if year input is less than 0
        if year <= 0:
            print("year must be greater than or equal to 0.")
            continue
        # ends loop
        else :
            break

    # adds info to movie list
    movie = [name, year]
    movies.append(movie)
    write_movies(movies)
    print(f"{name} was added.\n")

# deletes movie from list
def delete_movie(movies):
    while True:
        # tests of user input is integer
        try:
            number = int(input("Number: "))
        # if input is not integer 
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        # if input matches movie
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        else:
            break
    # remove movie
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(f"{movie[0]} was deleted.\n")

# display menu items
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

# main function
def main():
    display_menu()
    movies = read_movies()
    while True:     
        # menu options   
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
