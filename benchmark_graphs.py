import matplotlib.pyplot as plt
import numpy as np

# Define the data structure types
structures = ["K-mer index", "Suffix tree", "Wheeler graph"]

# Memory usage (in MB)
memory_usage = [8.59, None, None]

# Execution time (in seconds)
execution_time = [0.0183, None, None]

# Replace None with 0 for plotting purposes
memory_usage_plot = [m if m is not None else 0 for m in memory_usage]
execution_time_plot = [t if t is not None else 0 for t in execution_time]


bar_width = 0.6

plt.figure(figsize=(14, 7))
plt.bar(structures, memory_usage_plot, color='skyblue', width=bar_width)
plt.ylabel("Memory Usage (MB)")
plt.xlabel("Graph Type")
plt.xticks(rotation=20, ha='right')  
plt.title("Memory Usage for Finding Variants")
plt.ylim(0, max(memory_usage_plot) * 1.2)
plt.savefig("memory_usage_graph.png") 
plt.close() 

plt.figure(figsize=(14, 7))
plt.bar(structures, execution_time_plot, color='salmon', width=bar_width)
plt.ylabel("Execution Time (seconds)")
plt.xlabel("Graph Type")
plt.xticks(rotation=20, ha='right') 
plt.title("Execution Time for Finding Variants")
plt.ylim(0, max(execution_time_plot) * 1.2)
plt.savefig("execution_time_graph.png")  
plt.close() 
