import numpy as np
import matplotlib.pyplot as plt

# Generate a range of input sizes (n)
n = np.arange(1, 21)  # Limiting to n up to 20 to avoid overflow with factorial and exponential

# Define the time complexity functions
def O1(n):
    return np.ones_like(n)  # Constant time: O(1)

def Ologn(n):
    return np.log(n)  # Logarithmic time: O(log n)

def On(n):
    return n  # Linear time: O(n)

def Onlogn(n):
    return n * np.log(n)  # Linearithmic time: O(n log n)

def On2(n):
    return n**2  # Quadratic time: O(n^2)

def On3(n):
    return n**3  # Cubic time: O(n^3)

def O2n(n):
    # Limiting exponential to avoid overflow and crashes
    return np.clip(2**n, 0, 1e10)  # Clipping at a maximum value for visual purposes


def Onfact(n):
    # Limiting factorial to avoid overflow and crashes
    fact_values = np.array([np.math.factorial(i) if i <= 170 else 1e10 for i in n])  # 170! is the largest factorial that doesn't overflow
    return fact_values

# Plotting the graphs
plt.figure(figsize=(12, 8))

# Plot each time complexity
plt.plot(n, O1(n), label="O(1)", color='b')
plt.plot(n, Ologn(n), label="O(log n)", color='g')
plt.plot(n, On(n), label="O(n)", color='r')
plt.plot(n, Onlogn(n), label="O(n log n)", color='c')
plt.plot(n, On2(n), label="O(n^2)", color='m')
plt.plot(n, On3(n), label="O(n^3)", color='y')
plt.plot(n, O2n(n), label="O(2^n)", color='orange')
plt.plot(n, Onfact(n), label="O(n!)", color='purple')

# Set labels and title
plt.xlabel('Input Size (n)')
plt.ylabel('Operations / Time')
plt.title('Time Complexity Visualizations')

# Set axis limits for better visualization
plt.yscale('log')  # Using logarithmic scale to make it easier to visualize large values
plt.xlim(1, 20)  # Limiting x-axis range for factorial and exponential to avoid overflow

# Adjust the layout to prevent overlap of labels and ticks
plt.tight_layout()

# Show legend and grid
plt.legend()
plt.grid(True)

# Show plot
plt.show()
