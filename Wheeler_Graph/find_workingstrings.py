import os

# Directory containing the FASTA files
input_dir = "../Data/DMPK"

# Define the window sizes
window_sizes = [(2**10)-1]

# Create an output directory if desired (optional)
output_dir = "./output_substrings"
os.makedirs(output_dir, exist_ok=True)

# Iterate over each file in the /DMPK directory
for filename in os.listdir(input_dir):
    if filename.endswith(".fasta"):
        filepath = os.path.join(input_dir, filename)
        # Parse the file to get the sequence
        with open(filepath, "r") as f:
            lines = f.readlines()

        # The first line is a header
        # All subsequent lines are part of the sequence
        # Remove any whitespace and join them
        header = lines[0].strip()
        seq = "".join(line.strip() for line in lines[1:])

        # Extract an ID from the filename for naming output files
        # For example: dmpk_NC_000019.fasta -> ID = '000019'
        # We'll split on '.' and '_' and take the last part before '.fasta'
        # After splitting by '_', for dmpk_NC_000019.fasta:
        # ["dmpk", "NC", "000019.fasta"] -> "000019" after removing '.fasta'
        parts = filename.split("_")
        last_part = parts[-1] # e.g. "000019.fasta"
        seq_id = last_part.split(".")[0] # e.g. "000019"

        # For each window size, extract substrings and write to output file
        for w in window_sizes:
            output_filename = f"output_{w}_{seq_id}.txt"
            output_path = os.path.join(output_dir, output_filename)
        with open(output_path, "w") as out_f:
            # Generate all substrings of length w
            # Only do this if the sequence is long enough
            if len(seq) >= w:
                for i in range(len(seq) - w + 1):
                    substring = seq[i:i+w]
                    out_f.write(substring + "\n")
            else:
                # If the sequence is shorter than the window size,
                # it produces no substrings.
                pass

        print(f"Generated {output_path}")