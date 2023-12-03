from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pywaffle import Waffle


df = pd.read_excel('fire time range from 2022-10 to 2023-09.xlsx')
df2 = df[['Type', 'type_description']]
result = df2.groupby(['Type', 'type_description']).size().reset_index(name='count')

di = dict()
di2 = dict()
di3 = dict()

li = list()
for i,j in zip(result['type_description'],result['count']):
    di[i]=j
for i,j in zip(result['Type'],di):
    di2[j]=i
new_data = defaultdict(list)
for key, val in di2.items():
    new_data[val].append(key)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_aspect(aspect="equal")

Waffle.make_waffle(
    ax= ax,  # pass axis to make_waffle
    rows= 28, 
    columns= 23, 
    values= di, 
    block_aspect_ratio=1.618,
    block_arranging_style='new-line',
    vertical=True,
    interval_ratio_y=0.5,    cmap_name="tab20c",
    labels=[f"{k} ({int(v / sum(di.values()) * 100)}%, {v})" for k, v in di.items()],
    legend={'loc': 'upper left', 'bbox_to_anchor': (1.03, 1.01)},
    title={"label": "Types of Fires Recorded in Pittsburgh from October 2022 to October 2023.", "loc": "Left",}
    
)
fig.savefig("plot3.png", bbox_inches="tight")

