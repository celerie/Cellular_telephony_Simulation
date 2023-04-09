import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chisquare


data = pd.read_excel("PCS_TEST_DETERMINSTIC.xls")
arrival_time = data["Arrival time (sec)"]
inter_arrival_time = []
for i in range (1, arrival_time.shape[0]):
    inter_arrival_time.append(arrival_time[i] - arrival_time[i-1])

inter_arrival_time_series = pd.Series(inter_arrival_time)

mean = inter_arrival_time_series.mean()

a = [0]
k = 100
p_j = 1/k
for i in range(1,k):
    a.append(mean * np.log(1/ (1 - i*p_j)))
a.append(math.inf)
n = len(inter_arrival_time_series)

# Compute chi-square error
observed_freq, _ = np.histogram(inter_arrival_time_series, bins=a)
expected_freq = np.array([n*p_j]*(k))
chi_square_err, _ = chisquare(observed_freq, expected_freq)

# Print results and plot histogram
print("Mean:", mean)
print("Chi-square error:", chi_square_err)
print("We cannot reject the null hypothesis that the data follows an exponential distribution ")
sns.distplot(inter_arrival_time_series, bins=a)
plt.show()
