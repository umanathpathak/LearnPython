from collections import deque
q = deque()
q.append("eat")
q.append("sleep")
q.append("code")

print(q)
# deque(['eat', 'sleep', 'code'])

print(q.popleft())
# 'eat'
print(q.popleft())
# 'sleep'
print(q.popleft())
# 'code'

q.popleft()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: pop from an empty deque