"""A collection of class for doing my project."""

class MyBook():
    
    def __init__(self, name, author, genre, price):
        """Initialaize the characters.
        
        Parameters
        ---------------
        name: str
            String that is the name of the book.
        
        author: str
            String that is the author of the book.
        
        genre: str
            String that is the genre of the book.
        
        price: int/float
            Number that is the price of the book, can be either integer or float.
        """
        self.name = name
        self.author = author
        self.genre = genre
        self.price = price
        
    def print_receipt(self, name, author, price):
        """Print the receipt of the books people want to buy, including the information of name of the book, the author and the price.
        
        Parameters
        ---------------
        name: str
            String that is the name of the book.
        
        author: str
            String that is the author of the book.
        
        price: int/float
            Number that is the price of the book, can be an integer or a float.
        
        Returns
        ----------
        my_book: str
            String that contains the information of the book you buy.
        """
        
        my_book = self.name + ', written by ' + self.author + ', is ' + str(self.price) + ' $'
        
        print(my_book)
        
    def check_giftcard(self, genre, price):
        """Check whether you can get a gift card for the genre of art.
        
        Parameters
        ---------------
        genre: str
            String that is the genre of the book.
            
        price: int/float
            Number that is the price of the book, can be an integer or a float.
            
        Returns
        ----------
        gift_card: str
            String that says whether you can get a gift card or not.
        """
        
        #The condition of getting a gift card.
        if self.genre == 'art' and self.price > 30:
            gift_card = 'You can get a gift card!'
        
        else:
            gift_card = 'Sorry, there is no gift card available for you now.'
            
        return gift_card
