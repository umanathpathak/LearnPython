q = []
q.append((2, "code"))
q.append((1, "eat"))
q.append((3, "sleep"))
# Remember to re-sort every time a new element is inserted,
# or use bisect.insort()
q.sort(reverse=True)

while q:
     next_item = q.pop()
     print(next_item)

# (1, 'eat')
# (2, 'code')
# (3, 'sleep')