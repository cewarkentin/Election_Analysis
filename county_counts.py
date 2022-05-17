# Goals:
    # X. The number of votes for each county precinct
    # Y. The percentage of votes for each county precinct
    # Z. Which county had the largest number of votes?


# import module for pulling data from external CSV files and perform operations on them
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = 'Resources\election_results (1).csv'

# Assign a variable to save the file to a path.
file_to_save = 'analysis\election_analysis.txt'

# Y. Initialize a total vote counter.
total_votes = 0

# X. County options
county_options = []

# X. Empty dictionary for county votes
county_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Y. Add to the total vote count.
        total_votes += 1

        # X. Print the county name from each row.
        county_name = row[1]

        # X. If the county name does not match any existing county ...
        if county_name not in county_options:

            # X. Add it to the list of counties
            county_options.append(county_name)

            # X. Begin tracking that county's vote count
            county_votes[county_name] = 0

        # X. Add a vote to that county's count
        county_votes[county_name] += 1

# Y. Print the total votes.
print(total_votes)

# X. Print the county list.
print(county_options)

# X. Print the county vote dictionary
print(county_votes)

# Y. Determine the percentage of votes for each county by looping through the counts
# Y. Iterate through the county list
for county_name in county_votes:

    # Y. Retrieve vote counts for a county
    cvotes = county_votes[county_name]

    # Y. Calculate percentage of votes
    cvote_percentage = float(cvotes) / float(total_votes) * 100

    # Y. Print the county name and percentage of votes.
    print(f"{county_name} contained {cvote_percentage:.1f}% of the total voters.")