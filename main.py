import matplotlib.pyplot as plt

# initializing the data
x = [11, 33, 45, 67]
y = [20, 30, 40, 50]

# plotting the data
plt.plot(x, y)

# Adding the title
plt.title("Simple Plot")

# Adding the labels
plt.ylabel("Price of Pizzas")
plt.xlabel("Amount of Pizzas")



import matplotlib.pyplot as plt
# data to display on plots
x = [4, 2, 1]
y = [3, 2, 1]
z = [5, 6, 7]

# Creating figure object
plt.figure()

# adding first subplot
plt.subplot(121)
plt.plot(x, y)

# adding second subplot
plt.subplot(122)
plt.plot(z, y)



plt.show()