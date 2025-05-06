# s11111_2025.py
# PURPOSE:
# This program generates a random DNA sequence in FASTA format, including an inserted user-provided name (which is excluded from statistical calculations).
# The user specifies the length, sequence ID, description, and name.
# The program outputs the sequence to a FASTA file and displays nucleotide statistics.

import random

# Nucleotides used in DNA
NUCLEOTIDES = ['A', 'C', 'G', 'T']

# ORIGINAL:
# sequence_length = int(input("Enter the sequence length: "))
# MODIFIED (added input validation to handle non-integer or negative input [improves robustness]):
while True:
    try:
        sequence_length = int(input("Enter the sequence length: "))
        if sequence_length <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Get sequence ID and description from the user
sequence_id = input("Enter the sequence ID: ")
description = input("Provide a description of the sequence: ")
user_name = input("Enter your name: ")

# ORIGINAL:
# dna_sequence = ''.join(random.choices(NUCLEOTIDES, k=sequence_length))
# MODIFIED (switched from random.choices to random.choices with seed for reproducibility [helps testing]):
random.seed(42)  # Setting seed for reproducibility
dna_sequence = ''.join(random.choices(NUCLEOTIDES, k=sequence_length))

# Insert the user's name at a random position
insert_position = random.randint(0, len(dna_sequence))
# ORIGINAL:
# final_sequence = dna_sequence[:insert_position] + user_name + dna_sequence[insert_position:]
# MODIFIED (ensure name is clearly marked, e.g., with brackets, to separate non-DNA letters [improves readability]):
final_sequence = dna_sequence[:insert_position] + f"[{user_name}]" + dna_sequence[insert_position:]

# Calculate nucleotide statistics (excluding name)
counts = {nuc: dna_sequence.count(nuc) for nuc in NUCLEOTIDES}
percentages = {nuc: (counts[nuc] / sequence_length) * 100 for nuc in NUCLEOTIDES}
cg_ratio = ((counts['C'] + counts['G']) / (counts['A'] + counts['T'])) * 100 if (counts['A'] + counts['T']) > 0 else 0

# Write to FASTA file
filename = f"{sequence_id}.fasta"
with open(filename, 'w') as fasta_file:
    fasta_file.write(f">{sequence_id} {description}\n")
    fasta_file.write(final_sequence + "\n")

# Display confirmation and statistics
print(f"The sequence was saved to the file {filename}")
print("Sequence statistics:")
for nuc in NUCLEOTIDES:
    print(f"{nuc}: {percentages[nuc]:.1f}%")
print(f"%CG: {counts['C'] + counts['G'] / sequence_length * 100:.1f}")

# EXTRA IMPROVEMENT (added line wrapping in FASTA file [compliance with standard, improves readability]):
# By FASTA convention, sequences are usually wrapped at 60-80 characters per line.
# Here, we wrap at 60 characters.
wrapped_sequence = '\n'.join([final_sequence[i:i+60] for i in range(0, len(final_sequence), 60)])
with open(filename, 'w') as fasta_file:
    fasta_file.write(f">{sequence_id} {description}\n")
    fasta_file.write(wrapped_sequence + "\n")

# EXTRA COMMENTS:
# - We use a dictionary to calculate nucleotide counts efficiently.
# - We protect against division by zero when calculating %CG.
# - The random seed ensures results can be reproduced during testing.
# - The user's name is clearly bracketed to avoid confusion with DNA letters.
# - We handle invalid input gracefully by looping until a valid integer is entered.

# CONTEXT OF USE:
# This script can be used in bioinformatics coursework or simple simulations to generate random DNA sequences.
# It helps students practice with sequence formats and understand nucleotide composition.
# In real research, much stricter validation and larger datasets would be used.

# IMPORTANT:
# Upload this file in a GitHub folder named: 2025py_s11111 (replace s11111 with your ID)
# File name must be: s11111_2025.py (replace s11111 with your ID)
