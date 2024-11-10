import pandas as pd

class booklover:
    
    # Initializes BookLover with a name, email, favorite genre, and empty book list with num_book = 0
    def __init__(self, name, email, fav_genre):
        self.name = name  # Sets the name attribute (required)
        self.email = email  # Sets the email attribute (required)
        self.fav_genre = fav_genre  # Sets the favorite genre attribute (required)
        self.num_books = 0  # Initializes the number of books read = 0
        self.book_list = pd.DataFrame(columns=['book_name', 'book_rating'])  # Initializes an empty DataFrame for the book list

    # Method 1: Adds a book to the book list; tells the user if the book is already in the list
    def add_book(self, book_name, book_rating):
        new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})  # Creates a new df with book name and rating
        if book_name not in self.book_list['book_name'].values:  # Checks if the book is not already in book list
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)  # Adds the new book to the book list
            self.num_books += 1  # Increment num_books
        else:
            print("Book already in list")  # Prints message if the book is already in list

    # Method 2: Determines if the person has read a book
    def has_book(self, book_name):
        if book_name in self.book_list['book_name'].values:  # Checks if the book is in the book list
            return True  # Returns True if the book is in list
        else:
            return False  # Returns False if the book is not in list

    # Method 3: Simply returns the number of books read
    def num_books_read(self):
        return self.num_books  # Returns the number of books read

    # Method 4: Returns a list of books read with ratings of 3 or more
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] >= 3]  # Returns a df of books with a rating of 3 or more