# Goals:
    # A. The total number of votes cast
    # B. A complete list of candidates who received votes
    # C. The percentage of votes each candidate won
    # D. The total number of votes each candidate won
    # E. The winner of the election based on popular vote


# import module for pulling data from external CSV files and perform operations on them
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = 'Resources\election_results (1).csv'

# Assign a variable to save the file to a path.
file_to_save = 'analysis\election_analysis.txt'

# A. Initialize a total vote counter
total_votes = 0

# B. Create a list to contain candidate names
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:

        # A. Add to the total vote count
        total_votes += 1

        # B. Find the candidate name from each row
        candidate_name = row[2]

        # B. If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
    
    # A. Print the total votes
    print(total_votes)

    # B. Print the candidate list.
    print(candidate_options)