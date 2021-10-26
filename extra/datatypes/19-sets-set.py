vowels = {"a", "e", "i", "o", "u"}
print("e" in vowels)
# True

letters = set("alice")
print(letters.intersection(vowels))
# {'a', 'e', 'i'}

vowels.add("x")
print(vowels)
# {'i', 'a', 'u', 'o', 'x', 'e'}

print(len(vowels))
# 6

