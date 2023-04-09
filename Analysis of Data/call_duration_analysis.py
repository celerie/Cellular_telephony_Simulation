import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2, expon
import seaborn as sns

data = pd.read_excel("PCS_TEST_DETERMINSTIC.xls")
call_duration = data["Call duration (sec)"]

# Subtract the minimum value from all observations for more accurate proving of exponential distribution
call_duration_shifted = call_duration - call_duration.min()

null_dist = expon(scale=call_duration_shifted.mean())

bins = 20

# Calculate expected frequencies for each bins assuming null hypothesis
expected_freq = np.array([null_dist.cdf((i+1)*call_duration_shifted.max()/bins) -
                          null_dist.cdf(i*call_duration_shifted.max()/bins) for i in range(bins)]) * len(call_duration_shifted)

# Calculate the observed frequencies for each bins
observed_freq, _ = np.histogram(call_duration_shifted, bins=bins)

# Calculate the chi-squared test statistic
chi2_stat = sum((observed_freq - expected_freq)**2 / expected_freq)

# Calculate the critical value for the chi-squared distribution with 19 degrees of freedom and a significance level of 0.05
crit_val = chi2.ppf(0.995, bins-1)

print(call_duration.mean())
print(call_duration_shifted.mean())
# Compare the chi-squared statistic to the critical value
if chi2_stat < crit_val:
    print("We cannot reject the null hypothesis that the data follows an exponential distribution with unknown rate")
else:
    print("We reject the null hypothesis that the data follows an exponential distribution with unknown rate")

# Plot the histogram
print(chi2_stat)
sns.distplot(call_duration_shifted)
#plt.hist(call_duration_shifted, bins=20)
plt.xlabel("Shifted Call Duration (sec)")
plt.ylabel("Frequency")
plt.title("Distribution of Call duration")
#plt.title("Histogram of Shifted Call Duration")
plt.show()