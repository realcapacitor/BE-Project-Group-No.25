import pandas as pd
import matplotlib.pyplot as plt

# read CSV file into a pandas dataframe
df = pd.read_csv('dataMoisIrrig.csv')

# convert timestamp column to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# set timestamp column as the index of the dataframe
df.set_index('Timestamp', inplace=True)

# plot the dataframe
plt.plot(df.index, df['Moisture'])

# set the title and labels for the plot
plt.title('Timestamp vs Moisture Values')
plt.xlabel('Timestamp')
plt.ylabel('Moisture')

# display the plot
plt.show()

