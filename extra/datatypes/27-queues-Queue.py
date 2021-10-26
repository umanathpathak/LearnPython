from queue import Queue

s = Queue()
s.put("eat")
s.put("sleep")
s.put("code")

print(s)
# <queue.LifoQueue object at 0x108298dd8>

print(s.get())
# 'code'
print(s.get())
# 'sleep'
print(s.get())
# 'eat'

# print(s.get_nowait())
# queue.Empty

print(s.get())  # Blocks/waits forever...