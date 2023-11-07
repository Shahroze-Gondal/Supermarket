import pandas as pd
import matplotlib.pyplot as plt

def piechart(data, title, label_text, save_as):
    plt.figure(figsize=(8, 8))
    gender_distribution = data['Gender'].value_counts()
    plt.pie(gender_distribution, labels=gender_distribution.index, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')

    # Add text to the chart
    plt.text(0.5, 0.5, label_text, horizontalalignment='center', verticalalignment='center', fontsize=12, transform=plt.gca().transAxes)

    # Save the plot as a PNG image
    plt.savefig("piechart.png")

    # Show the pie chart
    plt.show()

def main():
    # Load your data from a CSV file into a DataFrame
    data = pd.read_csv('supermarket.csv')

    # Call the piechart function to create and display the pie chart and save it
    label_text = 'Gender Distribution in the Supermarket'
    save_as = 'gender_distribution_piechart.png'
    piechart(data, 'Customer Gender Distribution', label_text, save_as)

if __name__ == "__main__":
    main()
