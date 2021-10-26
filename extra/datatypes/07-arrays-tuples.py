arr1 = (0, 1, 2, 3, 4, 5)

print(arr1)


def some_func():
    return "a func"


arr2 = (
    1,
    "one",
    (
        "nested",
        "tuple",
    ),
    ["a", "list"],
    some_func,
)

# arr2[1] = "changed value"
# del arr2[0]

# print(arr2)

# arr3 = ('some_string',) + arr2
# print(arr3)
#
#
# del arr2
