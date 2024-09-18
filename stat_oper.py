# import numpy as np
# import matplotlib.pyplot as plt

# # Mean :
# data = np.array([10, 20, 30, 40, 50]);
# mean = np.mean(data);

# plt.subplot(2,1,1);
# plt.plot(data, label = "Data points");
# plt.axhline(y = mean, color ='r', label ="Mean")
# plt.title("Mean of data");
# plt.legend();



# # Mean and SD :
# std = np.std(data);
# plt.subplot(2,1,2);
# plt.hist(data,bins = 5, alpha = 0.7);
# plt.axvline(mean,color = 'r', label = "Mean");
# plt.axvspan(mean-std,mean+std, alpha = 0.2, color = "green", label = "1 SD");
# plt.legend();
# plt.show();
#..........................................................................

import numpy as np
import matplotlib.pyplot as plt

# Example datasets
scores = np.array([70, 75, 80, 85, 90, 95, 85, 80, 75, 100])
hours_studied = np.array([1, 2, 2, 3, 4, 5, 3, 2, 1, 5])

# 1. Mean
mean_score = np.mean(scores)
print(f"Mean Score: {mean_score}")

# 2. Variance
variance_score = np.var(scores, ddof=0)  # Population variance
print(f"Variance Score: {variance_score}")

# 3. Standard Deviation
std_dev_score = np.sqrt(variance_score)
print(f"Standard Deviation Score: {std_dev_score}")

# 4. Standard Error
std_error_score = std_dev_score / np.sqrt(len(scores))
print(f"Standard Error Score: {std_error_score}")

# 5. Covariance
covariance = np.cov(scores, hours_studied, ddof=0)[0][1]
print(f"Covariance: {covariance}")

# 6. Correlation
correlation = np.corrcoef(scores, hours_studied)[0][1]
print(f"Correlation: {correlation}")

# Plotting graphs for each term

# Histogram of Scores
plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.hist(scores, bins=5, alpha=0.7, color='blue', edgecolor='black')
plt.title('Histogram of Exam Scores')
plt.xlabel('Scores')
plt.ylabel('Frequency')

# Variance and Standard Deviation
plt.subplot(3, 2, 2)
plt.bar(['Variance', 'Standard Deviation'], [variance_score, std_dev_score], color=['orange', 'green'])
plt.title('Variance and Standard Deviation of Scores')
plt.ylabel('Value')

# Standard Error
plt.subplot(3, 2, 3)
plt.bar(['Standard Error'], [std_error_score], color='purple')
plt.title('Standard Error of Scores')
plt.ylabel('Value')

# Covariance
plt.subplot(3, 2, 4)
plt.bar(['Covariance'], [covariance], color='red')
plt.title('Covariance between Scores and Hours Studied')
plt.ylabel('Value')

# Correlation
plt.subplot(3, 2, 5)
plt.bar(['Correlation'], [correlation], color='cyan')
plt.title('Correlation between Scores and Hours Studied')
plt.ylabel('Value')

plt.tight_layout()
plt.show()





