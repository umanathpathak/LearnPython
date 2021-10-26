address_book = {"batman": 911001, "spiderman": 11991, "ironman": 88272}

print(address_book["batman"])

# dict comprehension
squares = {n: n * n for n in range(6)}

# unhashable
# example_key = [1,2,3]
# address_book[example_key] = "some_value"


print(hash(address_book["batman"]))

# updating a dictionary - 1
address_book["shaktiman"] = 1111

address_book_indian = {"krish": 2345, "shaktiman": 1234, "salman khan": 0}
#
# address_book.update(address_book_indian)  # works in place only
# print(address_book)

# a more pythonic way
# global_address_book = dict(address_book, **address_book_indian)
# # or
# global_address_book2 = {**address_book, **address_book_indian}
# print(global_address_book)
#
# # union operators for 3.9
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "b": 9999}
# d3 = d1 | d2
# print(d3)
# # {'a': 1, 'b': 9999, 'c': 3}
#
# d1 |= d2
# print(d1)
# # {'a': 1, 'b': 9999, 'c': 3}
