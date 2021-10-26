s = []
s.append("eat")
s.append("sleep")
s.append("code")

print(s)
# ['eat', 'sleep', 'code']

print(s.pop())
# 'code'
print(s.pop())
# 'sleep'
print(s.pop())
# 'eat'

print(s.pop())
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: pop from empty list