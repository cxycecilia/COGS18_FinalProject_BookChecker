"""Script to run some part of my project."""

# This adds the directory above to our Python path
# This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

from my_module.functions import check_number, check_genre, check_price
from my_module.classes import MyBook

book_1 = check_number(2546)
book_2 = check_genre('humanities')
book_3 = check_genre('hum')

my_book_1 = MyBook('The Origin of the Modern World', 'Robert Marks', 'humanities', 22.42)
my_book_2 = MyBook('Fundamentals of Physics', 'R. Shankar', 'science', 18.66)
my_book_3 = MyBook('Understanding Film Theory', 'Ruth Doughty', 'art', 37.99)

my_book_1.print_receipt('The Origin of the Modern World', 'Robert Marks', 22.42)
my_book_2.print_receipt('Fundamentals of Physics', 'R. Shankar', 18.66)
my_book_3.print_receipt('Understanding Film Theory', 'Ruth Doughty', 37.99)

gift_card = my_book_3.check_giftcard('art', 37.99)

price_1 = check_price([22.42, 18.66, 37.99])
price_2 = check_price([22.42, 18.66, 37.99, 103.56])

print(book_1)
print(book_2)
print(book_3)

print(gift_card)

print(price_1)
print(price_2)