class User():
    """ User class for TomeRater application, defines characteristics of the User
    and adds useful methods for working with Users """

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        """ Returns the User email """
        return self.email

    def change_email(self, address):
        """ takes in a new email and updates the User email """
        self.email = address
        print(self.name, "\'s email was changed to", address)

    def __repr__(self):
        return "User " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books))

    def __eq__(self, other_user):
        if self.email == other_user.get_email():
            return True
        else:
            return False
    
    def read_book(self, book, rating=None):
        """ Will 'read' a book and add it, and a rating if provided, to the dictionary of books for this User"""
        self.books[book] = rating
    
    def get_average_rating(self):
        """ Calculate the average rating of all the books read by this User """
        total_rating = 0
        for rating in self.books.values():
            if rating is not None:
                total_rating += rating
        return total_rating/len(self.books)


class Book():
    """ An object that collects information on Books for our Users to read and provides 
    helpful methods for working with those books. """
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        """ Returns the title of the Book """
        return self.title

    def get_isbn(self):
        """ Returns the ISBN of the Book """
        return self.isbn

    def set_isbn(self, new_isbn):
        """ Changes the ISBN of the book and gives a message that this was done """
        self.isbn = new_isbn
        print(self.title, "ISBN changed to", new_isbn)

    def add_rating(self, rating):
        """ Will confirm is rating is between 0 and 4 and, if it is, will add it to the ratings list, otherwise 
        it will kick out an error message. """
        if rating > 0 and rating < 5:
            self.ratings.append(rating)
        else:
            print("Invalid Rating!")

    def __eq__(self, other_book):
        if self.title == other_book.get_title() and self.isbn == other_book.get_isbn():
            return True
        else:
            return False
    
    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_average_rating(self):
        """ Calculate the average rating of all the books read by this User """
        total_rating = 0
        for rating in self.ratings:
            total_rating += rating
        return total_rating/len(self.ratings)

    def __repr__(self):
        return self.title

class Fiction(Book):
    """ Creates a sub-class Book for fiction titles"""
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        """ Returns the author of this Fiction Book """
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author

class Non_Fiction(Book):
    """ Creates a sub-class of Book for non-fiction books """
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        """ Returns the subject of the book """
        return self.subject

    def get_level(self):
        """ Returns the level of the book """
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(
            title=self.title, level=self.level, subject=self.subject)

class TomeRater():
    """ Our application that will use the User and Book classes created above. """
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        """ Creates a new Book """
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        """ Creates a new Fiction """
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        """ Creates a new Fiction """
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        """ Add a book to the User """
        if email not in self.users:
            print("No user with email {email}".format(email=email))
        else:
            self.users[email].read_book(book, rating)
            if rating is not None:
                book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1

    def add_user(self, name, email, user_books=None):
        """" Create a user """
        self.users[email] = User(name, email)
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        """Prints out all of the keys from the books dict"""
        for book in self.books:
            print(book)

    def print_users(self):
        """Prints out all of the keys from the users dict"""
        for user in self.users.keys():
            print(user)

    def most_read_book(self):
        """ Reviews the list of books and prints out the most read one. """
        most_read = 0
        most_read_book = ""

        for book, times_read in self.books.items():
            if times_read > most_read:
                most_read = times_read
                most_read_book = book
        
        return most_read_book

    def highest_rated_book(self):
        """ Gives use the highest rated book """
        highest_rated_book = ""
        highest_rating = 0
        for book in self.books:
            if book.get_average_rating() > highest_rating:
                highest_rating = book.get_average_rating()
                highest_rated_book = book

        return highest_rated_book

    def most_positive_user(self):
        """ gives us the most positive user """
        highest_rated_user = ""
        highest_rating = 0
        for user in self.users.values():
            if user.get_average_rating() > highest_rating:
                highest_rating = user.get_average_rating()
                highest_rated_user = user

        return highest_rated_user.name
