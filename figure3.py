import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel('fire time range from 2022-10 to 2023-09.xlsx')  # Replace with the path to your dataset file

# Convert 'month' to a datetime format for sorting
df['month'] = pd.to_datetime(df['month'], format='%Y-%m')

# Count the number of incidents for each month
monthly_counts = df['month'].dt.to_period('M').value_counts().sort_index()

# Ensure all months from 2022-10 to 2023-09 are represented, including months with zero incidents
all_months = pd.period_range(start='2022-10', end='2023-09', freq='M')
monthly_counts_full = monthly_counts.reindex(all_months, fill_value=0)

# Creating a horizontal bar chart with royal blue color
plt.figure(figsize=(12, 8))
bars = plt.barh(monthly_counts_full.index.astype(str), monthly_counts_full.values, color='royalblue')

# Adding specific numbers above each bar
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 0.1
    plt.text(label_x_pos, bar.get_y() + bar.get_height()/2, str(width), va='center')

# Setting the labels and title
plt.xlabel('Number of Incidents')
plt.ylabel('Month')
plt.title('Monthly Fire Incidents from 2022-10 to 2023-10')

plt.show()
