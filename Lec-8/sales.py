import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

salesdata = pd.read_csv(r'C:\Nilesh Indore\Projects\LearnPython\Lec-8\sales.csv')
salesnp = np.array(salesdata)
print(salesdata.columns)

plt.plot(salesnp)
#plt.xlabel("Year")
#plt.ylabel("Sales in Cr.")
#plt.title("Sales Trend")
plt.show()