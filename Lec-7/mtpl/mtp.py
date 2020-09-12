from matplotlib import pyplot as plt

year = [ 1990 , 2000 , 2010 , 2020 ]
sales = [ 200 , 300 , 150 , 350 ]

plt.plot(year, sales)
plt.xlabel("Year")
plt.ylabel("Sales in Cr.")
plt.title("Sales Trend")
plt.show()