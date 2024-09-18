import numpy as np
import matplotlib.pyplot as plt

# Example datasets
scores = np.array([70, 75, 80, 85, 90, 95, 85, 80, 75, 100])
hours_studied = np.array([1, 2, 2, 3, 4, 5, 3, 2, 1, 5])

# Calculating statistical measures
mean_score = np.mean(scores)
variance_score = np.var(scores, ddof=0)
std_dev_score = np.std(scores)
std_error_score = std_dev_score / np.sqrt(len(scores))
covariance = np.cov(scores, hours_studied)[0][1]
correlation = np.corrcoef(scores, hours_studied)[0][1]

# Measures to plot
measures = [mean_score, variance_score, std_dev_score, std_error_score, covariance, correlation]
labels = ['Mean', 'Variance', 'Std Dev', 'Std Error', 'Covariance', 'Correlation']
colors = ['blue', 'orange', 'green', 'purple', 'red', 'cyan']

# Plotting
plt.bar(labels, measures, color=colors)
plt.title('Statistical Measures of Exam Scores')
plt.ylabel('Value')
plt.show()
