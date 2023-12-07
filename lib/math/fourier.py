import numpy as np
import matplotlib.pyplot as plt

# Generate a sample time series of sales with noise
np.random.seed(42)
time = np.arange(0, 10, 0.1)
sales = 50 * np.sin(2 * np.pi * 0.5 * time) + np.random.normal(0, 10, len(time))

# Plot the original time series
plt.figure(figsize=(10, 4))
plt.plot(time, sales, label='Original Sales')
plt.title('Original Sales Time Series')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.legend()
plt.show()

# Apply a low-pass filter to smooth the time series (remove higher frequencies)
def low_pass_filter(data, alpha=0.1):
    filtered_data = np.zeros_like(data)
    filtered_data[0] = data[0]
    for i in range(1, len(data)):
        filtered_data[i] = alpha * data[i] + (1 - alpha) * filtered_data[i - 1]
    return filtered_data

# Set the alpha parameter for the low-pass filter (adjust as needed)
alpha_value = 0.5

# Apply the low-pass filter to the sales time series
smoothed_sales = low_pass_filter(sales, alpha=alpha_value)

# Plot the original and smoothed time series
plt.figure(figsize=(10, 4))
plt.plot(time, sales, label='Original Sales')
plt.plot(time, smoothed_sales, label=f'Smoothed (Alpha={alpha_value})', linestyle='dashed')
plt.title('Original and Smoothed Sales Time Series')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.legend()
plt.show()
