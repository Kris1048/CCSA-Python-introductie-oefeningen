book_price = 24.95
discount_rate = 0.4
number_books = 60
shipping_cost = 3 + 0.75 * (number_books-1)
total_price = (number_books * book_price) * (1 - discount_rate) + shipping_cost

print(total_price)
