import pandas as pd
import matplotlib.pyplot as plt

def bar_chart(data, x_column, y_column, title, x_label, y_label, label_text):
    plt.figure(figsize=(10, 6))
    data.plot(kind='bar')

    # Set labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Add labels and text to the chart
    for i, v in enumerate(data):
        plt.text(i, v, label_text[i], horizontalalignment='center', verticalalignment='bottom', fontsize=12)

    # Show the bar chart
    plt.xticks(rotation=0)  # Rotate x-axis labels if needed
    plt.tight_layout()

    # Save the plot as a PNG image
    plt.savefig("bar_chart.png")
    plt.show()

def main():
    # Load your data from a CSV file into a DataFrame
    data = pd.read_csv('supermarket.csv')

    # Group the data by 'City' and calculate the count of customers in each city
    city_wise_customers = data['City'].value_counts()

    # Call the bar_chart function to create and display the bar chart
    label_text = city_wise_customers.values
    bar_chart(city_wise_customers, city_wise_customers.index, city_wise_customers.values, 'City-wise Customers', 'City', 'Number of Customers', label_text)

if __name__ == "__main__":
    main()
