import unittest
from booklover import booklover

class BookLoverTestSuite(unittest.TestCase):
    
    def setUp(self):
        self.book_lover = BookLover(name="Alice Cooper", email="alice@BillionDollarBabies.com", fav_genre="Horror")  
        
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        self.book_lover.add_book("The Shining", 5)  # Adds a book 
        self.assertTrue("The Shining" in self.book_lover.book_list['book_name'].values)  # Checks that the book is in the list

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        self.book_lover.add_book("The Shining", 5)  # Adds the book 
        self.book_lover.add_book("The Shining", 5)  # Attempt to add again
        self.assertEqual(len(self.book_lover.book_list[self.book_lover.book_list['book_name'] == "The Shining"]), 1)  # Checks 1 occurance
        
    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        self.book_lover.add_book("It", 4)  # Add a book
        self.assertTrue(self.book_lover.has_book("It"))  # Check that the book is in the list

    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        self.assertFalse(self.book_lover.has_book("Pet Semetary"))  # Check that the book is not in the list

    def test_5_num_book_read(self):
        # add some books to the list, and test num_books matches expected.
        self.book_lover.add_book("The Shining", 5)  # Add a book
        self.book_lover.add_book("It", 4)  # Add another book
        self.assertEqual(self.book_lover.num_books_read(), 2)  # Check that the number of books read = 2

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        self.book_lover.add_book("The Shining", 5)  # Add some books with ratings
        self.book_lover.add_book("It", 2)  
        self.book_lover.add_book("The Stand", 2)  
        self.book_lover.add_book("Cujo", 4)  
        self.book_lover.add_book("Salems Lot", 3)  
        fav_books = self.book_lover.fav_books()  # Gets the list of favorite books
        self.assertTrue(all(fav_books['book_rating'] >= 3))  # Check that all favorite books have a rating of 3 or more
        self.assertTrue("The Stand" not in fav_books['book_name'].values)  # Check that "The Stand" is not in the fav list
        self.assertTrue(all(fav_books['book_rating'] >= 3))  # Checks that all books in return list have a rating of 3 or more

if __name__ == '__main__':
    unittest.main(verbosity=3)