"""A collection of function for doing my project."""

def check_number(input_number):
    """
    Find the location of the book by checking the code number on the book.
    
    Parameters
    ---------------
    input_number: int
        Integer that is the code number of the book.
    
    Returns
    ----------
    output_book: str
        String that contains the location of the book.
    """
    
    #The input number must be a integer, not a float.
    if type(input_number) is not int:
        output_book = 'Sorry, please enter the right number.'
    
    #If the input number is in the range from 1000 to 5000, then the location will be the output.
    elif input_number <= 2000 and input_number > 1000:
        output_book = 'The book is on the left side on the first floor.'
    
    elif input_number <= 3000 and input_number > 2000:
        output_book = 'The book is on the right side on the first floor.'
    
    elif input_number <= 4000 and input_number > 3000:
        output_book = 'The book is on the left side on the second floor.'
        
    elif input_number <= 5000 and input_number > 4000:
        output_book = 'The book is on the right side on the second floor.'
    
    #If the input number is out of the range, then the book is not available now.
    else:
        output_book = 'Sorry, the book is now out of stock.'
        
    return output_book

def check_genre(input_genre):
    """
    Find the location of the book by checking the genre of the book.
    
    Parameters
    ---------------
    input_genre: str
        String that is the genre of the book, could be either a complete name or an abbreviation.
    
    Returns
    ----------
    output_book: str
        String that contains the location of the book.
    """
    
    #Check the location by checking the three main genres, can be abbreviation. 
    if input_genre in 'science':
        output_book = 'The book is on the blue shelves.'
    
    elif input_genre in 'humanities':
        output_book = 'The book is on the green shelves.'
    
    elif input_genre in 'art':
        output_book = 'The book is on the yellow shelves.'
    
    #For other genres, there are not specific shelves, so ask the staff.
    else:
        output_book ='Sorry, please ask the staff to check the location of the book.'
    
    return output_book

def check_price(price_list):
    """
    Calculate the price of the books you want to purchase.
        
    Parameters
    ---------------
    price_list: list
        List that contains the all the prices.
            
    Returns
    ----------
    total_price: int/float
        Number of the total price of the books people want to buy.
    """
        
    #Set the total price first at 0.
    total_price = 0
   
    #Loop all the prices in the list and add them together.
    for price in price_list:
        total_price = total_price + price
        
    #If the total price reaches a certain amount, there will be a discount on the total price.
    if total_price >= 100 and total_price < 200:
        total_price = total_price * 0.9
    
    elif total_price >= 200:
        total_price = total_price * 0.8
            
    return total_price
