import pandas as pd
import math
import matplotlib.pyplot as plt
from scipy.stats import chi2

data = pd.read_excel("PCS_TEST_DETERMINSTIC.xls")
base_station = data["Base station "]

mean = base_station.mean()

observed = base_station.value_counts().sort_index()

expected = len(base_station) / 20
contributions = (observed - expected)**2 / expected
test_statistic = contributions.sum()

#Null hypothesis: the data follows a uniform distribution
#Using a significance value of 0.05, 20-1 degree of freedom
alpha = 0.05
df = 19
critical_value = chi2.ppf(1 - alpha, df)
if test_statistic > critical_value:
    print("Reject null hypothesis: the data does not follow a uniform distribution.")
else:
    print("Fail to reject null hypothesis: the data may follow a uniform distribution.")


print("Mean:",mean)
print("Test error:",test_statistic)
plt.hist(base_station, bins=20)
plt.title("Histogram of Base Station Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()