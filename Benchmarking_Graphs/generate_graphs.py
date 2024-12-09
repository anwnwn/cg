import matplotlib.pyplot as plt
import re

# Define the function to parse the input file
def parse_file(file_path):
    lengths = []
    times = []

    with open(file_path, 'r') as file:
        content = file.readlines()

    # Skip the first two lines
    content = content[2:]

    # Extract length and time data
    for line in content:
        # Match the pattern of 'length: time'
        match = re.search(r"(\d+):\s*([\d\.]+)", line)
        if match:
            lengths.append(int(match.group(1)))
            times.append(float(match.group(2)) * 1000)  # Convert time to milliseconds

    return lengths, times

# Define the files to be processed and their corresponding labels
file_paths = [
    './K-mer_Index/kmer_output.txt', 
    './Suffix_Tree/st_implementation/st_output.txt',  
    './Suffix_Tree/st_package_implementation/st_output.txt', 
    './Wheeler_Graph/wheeler_output.txt'
]
labels = [
    'K-mer Index',  # Custom label for the first file
    'Custom Suffix Tree',  # Custom label for the second file
    'Package Suffix Tree',  # Custom label for the third file
    'Wheeler Graph'
]

# Plotting setup: Create two subplots (one for log scale and one for non-log scale)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Loop over each file and plot its data on both axes
for file_path, label in zip(file_paths, labels):
    lengths, times = parse_file(file_path)
    
    # Plot on log scale (base 2) for the first axis (ax1)
    ax1.plot(lengths, times, marker='o', linestyle='-', label=label)
    
    # Plot on non-log scale for the second axis (ax2)
    ax2.plot(lengths, times, marker='o', linestyle='-', label=label)

# Plot configuration for the log scale plot (ax1)
ax1.set_xscale('log', base=2)
ax1.set_yscale('log', base = 10)
ax1.set_title('Query Time vs Query Length (Log Scale)')
ax1.set_xlabel('Query Length')
ax1.set_ylabel('Query Time (milliseconds)')
#ax1.grid(True, which="both", ls="--", linewidth=0.5)
ax1.legend()

# Plot configuration for the non-log scale plot (ax2)
ax2.set_yscale('log', base = 10)
ax2.set_title('Query Time vs Query Length (Linear Scale)')
ax2.set_xlabel('Query Length')
ax2.set_ylabel('Query Time (milliseconds)')
#ax2.grid(True, which="both", ls="--", linewidth=0.5)
ax2.legend()

# Adjust layout for better spacing
plt.tight_layout()

# Display the plots
plt.show()
