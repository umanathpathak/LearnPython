import datetime as dt

x = dt.datetime.now()
print(x)
print(type(x))

print(dt.datetime.utcnow())
print(dt.datetime.utcnow().strftime("%d-%b-%Y:%H-%M-%S"))

dtformat = "%d-%b-%Y:%H-%M-%S"
print(dt.datetime.now().strftime("%d-%b-%Y:%H-%M-%S"))

