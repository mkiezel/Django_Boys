import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['linii kodu',"stosunek ilości\nznaków", "średnia metoda", "Najgorsza metoda"]
v1 = [46,50, 7.5, 27]
vinf =[44,68.5/2, 3, 6 ]

x = np.arange(len(labels))
width = 0.4

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, v1, width, label='v1',color = "red")
rects2 = ax.bar(x + width/2, vinf, width, label='v∞',color = "green")

ax.set_ylabel('Wyniki')
ax.set_title('Porówanie wersji (im mniej tym lepiej)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
