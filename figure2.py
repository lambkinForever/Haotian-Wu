import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('fire time range from 2022-10 to 2023-09.xlsx')  
grouped = df.groupby(['fire_zone', 'type_description']).size().unstack(fill_value=0)
top_10_fire_zones = grouped.sum(axis=1).nlargest(10).index
top_10_data = grouped.loc[top_10_fire_zones]
top_10_data = top_10_data.reindex(index=top_10_fire_zones)
fig, ax = plt.subplots(figsize=(15, 8))
top_10_data.plot(kind='bar', stacked=True, ax=ax, colormap='tab20')

ax.set_title('Top 10 Fire Zones by Number of Incidents with Distinct Type Descriptions')
ax.set_xlabel('Fire Zone')
ax.set_ylabel('Number of Incidents')
plt.xticks(rotation=45)
plt.legend(title='Type Description', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
