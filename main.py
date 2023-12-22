import matplotlib.pyplot as plt
def create_energy_consumption_graph():
    # Monthly energy consumption data (in kilowatt-hours)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    consumption = [.72, .74, .85, .86, 1.20, 1, 1.9, 1.22, 1, .80, .60, .40]

    # Create a bar graph
    plt.bar(months, consumption, color='blue')

    # Add labels and title
    plt.xlabel('Months')
    plt.ylabel('Energy Production (MWh)')
    plt.title('Monthly Energy Production of a Typical American Urban Household')

    # Display the graph
    plt.show()

# Call the function to create and display the graph
create_energy_consumption_graph()




