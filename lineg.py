import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(["Anil", "Komal", "Ashok", "Aniket", "Aman"] )  
ypoints = np.array([90, 85, 100, 80, 75])


plt.title("Graph")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.subplot(5, 2, 1)
plt.plot(xpoints, ypoints, marker='o',linestyle='dotted', color='g')

plt.subplot(5, 2, 2)
plt.bar(xpoints,ypoints)

plt.subplot(5, 2, 5)
plt.scatter(xpoints, ypoints)

plt.subplot(5, 2, 6)
x = np.random.normal(170, 10, 250)
plt.hist(x)

plt.subplot(5, 2, 9)
y = np.array([35, 25, 25, 15])
plt.pie(y)  


plt.show()