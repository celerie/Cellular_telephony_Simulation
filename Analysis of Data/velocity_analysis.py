import pandas as pd
import numpy as np
from scipy.stats import norm, chi2

data = pd.read_excel("PCS_TEST_DETERMINSTIC.xls")
velocity = data["velocity (km/h)"]
n_bins = 20  # number of bins
alpha = 0.05  # significance level

# Calculate observed frequencies and bin edges
observed_freq, bin_edges = np.histogram(velocity, bins=n_bins)

# Calculate expected frequencies
mean, std = norm.fit(velocity)
expected_freq = len(velocity) * np.diff(norm.cdf(bin_edges, mean, std))

# Calculate the chi-square test statistic
chi_square = np.sum((observed_freq - expected_freq)**2 / expected_freq)

# Calculate the critical value for the given significance level and degrees of freedom
crit_val = chi2.ppf(1 - alpha, n_bins - 1)

print(chi_square)
print(crit_val)
# Compare the chi-square test statistic with the critical value
if chi_square < crit_val:
    print("The null hypothesis that the data follows a normal distribution is accepted.")
else:
    print("The null hypothesis that the data follows a normal distribution is rejected.")
