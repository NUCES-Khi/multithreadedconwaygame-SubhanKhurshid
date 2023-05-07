import matplotlib.pyplot as plt


execution_times = [0.83, 0.47, 0.29, 0.19, 0.17]


speedup = [execution_times[0] / t for t in execution_times]


plt.plot([1, 2, 4, 8, 16], speedup, 'o-')


plt.xlabel('Number of threads')
plt.ylabel('Speedup')
plt.title('Speedup vs. number of threads')


plt.show()
