import matplotlib.pyplot as plt
import numpy as np

labels = ['SLOC',"stosunek ilości\nznaków", "średnia metoda", "Najgorsza metoda"]
v1 = [46,50, 7.5, 27]
vinf =[44,68.5/2, 3, 6 ]

x = np.arange(len(labels))
width = 0.4

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, v1, width, label='v1',color = "red",edgecolor = "black")
rects2 = ax.bar(x + width/2, vinf, width, label='v∞',color = "green",edgecolor = "black")

ax.set_ylabel('Wyniki')
ax.set_title('Porówanie wersji')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()

names = ["v1","v2","v3","v4","v5","v6","v7",'v∞']
metoda = [26,22,17,16,13,9,5,6]
klasa = [15,13,10,10,8,6,4,5]

plt.plot(names, metoda,marker='o',label = 'metoda "update_quality"')
plt.plot(names, klasa,marker='o', label = 'klasa "GildedRose"')
plt.ylim(0,28)
plt.xlabel("wersja")
plt.ylabel("wynik testu")
plt.title("Zmiany złożoności cyklomatycznej na przestrzeni wersji")
plt.legend()
plt.show()


labels = ['SLOC',"stosunek ilości\nznaków", "średnia metoda", "Najgorsza metoda"]

v7 = [45,38.6,18/7,5]


x = np.arange(len(labels))
width = 0.3

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, v1, width, label='v1',color = "red",edgecolor = "black")
rects2 = ax.bar(x , v7, width, label='v7',color = "orange",edgecolor = "black")
rects3 = ax.bar(x + width, vinf, width, label='v∞',color = "green",edgecolor = "black")

ax.set_ylabel('Wyniki')
ax.set_title('Porówanie wersji')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()