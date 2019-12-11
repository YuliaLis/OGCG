import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

with open('graphic.txt', 'r') as csvfile:

    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))



plt.title("Графік функції")

y = np.sqrt(x)


plt.plot(x,y,'r')

plt.xlabel('Вісь абсцис (X)')
plt.ylabel('Вісь ординат (Y)')
plt.grid(True, linestyle="-", color='0.75')
plt.show()

