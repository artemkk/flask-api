import matplotlib.pyplot as plt
import csv
import numpy as np

x0 = []
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
y = []

with open('raw-data\Concrete_Data.csv','r') as csvfile:
    
    next(csvfile)

    lines = csv.reader(csvfile, delimiter=',')

    for row in lines:
        x0.append(row[0])
        x1.append(row[1])
        x2.append(row[2])
        x3.append(row[3])
        x4.append(row[4])
        x5.append(row[5])
        x6.append(row[6])
        x7.append(row[7])
        y.append(row[8])

fig, ((ax0, ax1), (ax2, ax3), (ax4, ax5), (ax6, ax7)) = plt.subplots(4, 2)

ax0.scatter(np.asarray(x0, float), np.asarray(y, float), color = 'grey', s=None, label = "Cement Amount")
ax0.set_title('Cement Content vs Concrete Compressive Strength (MPa)', fontsize=10)
ax0.set_xlabel('Cement Content, kG/m^3')

ax1.scatter(np.asarray(x1, float), np.asarray(y, float), color = 'orange', s=None, label = "Blast Furance Slag")
ax1.set_title('Blast Furnace Slag vs Concrete Compressive Strength (MPa)', fontsize=10)
ax1.set_xlabel('Blast Furnace Slag Content, kG/m^3')

ax2.scatter(np.asarray(x2, float), np.asarray(y, float), color = 'yellow', s=None, label = "Fly Ash")
ax2.set_title('Fly Ash vs Concrete Compressive Strength (MPa)', fontsize=10)
ax2.set_xlabel('Fly Ash Content, kG/m^3')

ax3.scatter(np.asarray(x3, float), np.asarray(y, float), color = 'blue', s=None, label = "Water")
ax3.set_title('Water vs Concrete Compressive Strength (MPa)', fontsize=10)
ax3.set_xlabel('Water Content, kG/m^3')

ax4.scatter(np.asarray(x4, float), np.asarray(y, float), color = 'green', s=None, label = "Superplasticizer")
ax4.set_title('Superplasticizer vs Concrete Compressive Strength (MPa)', fontsize=10)
ax4.set_xlabel('Superplasticizer Content, kG/m^3')

ax5.scatter(np.asarray(x5, float), np.asarray(y, float), color = 'brown', s=None, label = "Coarse Aggregate")
ax5.set_title('Coarse Aggregate vs Concrete Compressive Strength (MPa)', fontsize=10)
ax5.set_xlabel('Coarse Aggregate Content, kG/m^3')

ax6.scatter(np.asarray(x6, float), np.asarray(y, float), color = 'beige', s=None, label = "Fine Aggregate")
ax6.set_title('Fine Aggregate vs Concrete Compressive Strength (MPa)', fontsize=10)
ax6.set_xlabel('Fine Aggregate, kG/m^3')

ax7.scatter(np.asarray(x7, float), np.asarray(y, float), color = 'black', s=None, label = "Age")
ax7.set_title('Age vs Concrete Compressive Strength (MPa)', fontsize=10)
ax7.set_xlabel('Age, Days')

plt.subplot_tool()
plt.show()
