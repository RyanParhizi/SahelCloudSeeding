import matplotlib.pyplot as plt
import pandas as pd
import csv

df = pd.read_csv('Data/bfa-rainfall-subnat-full.csv')

df['time'] = pd.to_datetime(df['date'])
df = df.sort_values('time')

yearly_avg = (
    df.groupby(df['time'].dt.year)['rfh']
      .sum()
)

yearly_avg.plot(kind='bar')

plt.xlabel('Year')
plt.ylabel('Total Rainfall (mm)')
plt.title('Total Rainfall (mm) x Year')
plt.tight_layout()
plt.show()




