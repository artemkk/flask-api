import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []

with open('raw-data\Concrete_Data.csv','r') as csvfile:
    next(csvfile)

    lines = csv.reader(csvfile, delimiter=',')
    
    for row in lines:
        x.append(row[0])
        y.append(float(row[8]))

x, y = zip(*sorted(zip(x, y)))

fig, ax = plt.subplots()
plt.scatter(x, y, color = 'g', s=None, label = "Cement Amount")

every_nth = 15
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)   

plt.xticks(rotation=90)
plt.tick_params(axis='x', which='both', bottom=False)

plt.xlabel('Cement, kG/m^3')
plt.ylabel('Compressive Strength, MPa')
plt.title('Compressive Strength as a Function of Cement', fontsize = 12)
plt.legend()
plt.show()
