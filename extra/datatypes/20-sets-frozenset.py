vowels = frozenset({"a", "e", "i", "o", "u"})

vowels.add("p")


d = {frozenset({1, 2, 3}): "hello"}
print(d[frozenset({1, 2, 3})])