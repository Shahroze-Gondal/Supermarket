
import pandas as pd
import matplotlib.pyplot as plt

def lineplot(df, x_column, y1_column, y2_column, title, x_label, y_label, legend_labels):
    plt.figure(figsize=(12, 8))
    plt.plot(df[x_column], df[y1_column], marker='o', linestyle='-', color='b', label=legend_labels[0])
    plt.plot(df[x_column], df[y2_column], marker='o', linestyle='-', color='g', label=legend_labels[1])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    
    # Save the plot as a PNG image
    plt.savefig("lineplot.png")
    plt.show()

    return

def main():
    # Load your data from a CSV file into a DataFrame
    data = pd.read_csv('supermarket.csv')

    # Convert the 'Date' column to a datetime data type
    data['Date'] = pd.to_datetime(data['Date'])

    # Group the data by 'Date' and calculate the sum of 'Total' and 'Tax 5%' sales for each date
    total_sales_by_date = data.groupby('Date').agg({'Total': 'sum', 'Tax 5%': 'sum'}).reset_index()

    # Create a line plot
    lineplot(total_sales_by_date, 'Date', 'Total', 'Tax 5%', 'Total Sales and Tax 5% Over Time', 'Date', 'Sales Amount', ['Total Sales', 'Tax 5%'])

if __name__ == "__main__":
    main()
