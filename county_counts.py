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

# B. Initialize a total vote counter
total_votes = 0

# A. Create a list to contain county names
county_options = []

# A. Declare an empty dictionary to count votes for each county
county_votes = {}

# C. County with the largest turnout
county_most_votes = ""
county_highest_count = 0
county_highest_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:

        # B. Add to the total vote count
        total_votes += 1

        # A. Find the county name from each row
        county_name = row[1]

        # A. If the county name does not match any existing county
        if county_name not in county_options:

            # A. Add it to the list of counties
            county_options.append(county_name)

            # A. Begin tracking that county's vote count
            county_votes[county_name] = 0

    # A. Add a vote to that county's count
    county_votes[county_name] += 1

election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
print(election_results, end="")

# D. Determine the percentage of votes in each county by looping through the counts.
# Iterate through the county list.
for county_name in county_votes:

    # D. Retrieve vote count of a county
    votes = county_votes[county_name]

    # D. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # E. Determine if the votes is greater than the winning_count
    if (votes > county_highest_count) and (vote_percentage > county_highest_percentage):

        # E. If true, reset winning count and winning percentage
        county_highest_count = votes
        county_highest_percentage = vote_percentage

        # E. Set the county-with-the-most-votes' name
        county_most_votes = county_name

    # Conclusion
    county_results = f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n"
    print(county_results)