import matplotlib.pyplot as plt
import csv
# data to display on plots
x = []
y = []

with open('airtravel.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		x.append(row[0])
		y.append(int(row[1]))


# This will plot a simple bar chart
plt.bar(x, y)

# Title to the plot
plt.title("Air Travel In 1958")

plt.xlabel('Months')
plt.ylabel('Number of Flights')
plt.show()
