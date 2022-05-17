# Goals:
    # A. The number of votes for each county precinct
    # B. The percentage of votes for each county precinct
    # C. Which county had the largest number of votes?


# import module for pulling data from external CSV files and perform operations on them
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = 'Resources\election_results (1).csv'

# Assign a variable to save the file to a path.
file_to_save = 'analysis\election_analysis.txt'

# Initialize a total vote counter.
total_votes = 0

# A. County options
county_options = []

# A. Empty dictionary for county votes
county_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # A. Print the county name from each row.
        county_name = row[1]

        # If the county name does not match any existing county ...
        if county_name not in county_options:

            # Add it to the list of counties
            county_options.append(county_name)

            # A. Begin tracking that county's vote count
            county_votes[county_name] = 0

        # A. Add a vote to that county's count
        county_votes[county_name] += 1

# Print the total votes.
print(total_votes)

# Print the candidate list.
print(county_options)

# Print the county vote dictionary
print(county_votes)