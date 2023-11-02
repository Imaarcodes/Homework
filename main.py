
import matplotlib.pyplot as plt
import csv
import numpy as np
t=np.arange(0,5,0.2)


Names = []
Values = []

with open('Icecreamscoop_three.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		Names.append(row[0])
		Values.append(int(row[1]))


plt.scatter(Names, Values, color = 'g',s = 100)
plt.xticks(rotation = 25)
plt.xlabel('Number of Scoops')
plt.ylabel('Number of People')
plt.title('Consumption Per Number of Scoops', fontsize = 20)

plt.show()


