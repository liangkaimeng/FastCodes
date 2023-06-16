# -*- coding: utf-8 -*-
# Author: lkm
# date: 2023/6/16 23:08

import seaborn as sns
import matplotlib.pyplot as plt

# Create a list of data labels
labels = ['Label 1', 'Label 2', 'Label 3', 'Label 4']

# Create a list of data values
sizes = [15, 30, 45, 10]

# Create a pie chart
sns.set(style="whitegrid")
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Pie Chart Example')
plt.show()
