# Goals:
    # A. The total number of votes cast
    # B. A complete list of candidates who received votes
    # C. The total number of votes each candidate won
    # D. The percentage of votes each candidate won
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

# C. Declare an empty dictionary to count votes for each candidate
candidate_votes = {}

# E. Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
            # B. Add it to the list of candidates
            candidate_options.append(candidate_name)

            # C. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # C. Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # D. Determine the percentage of votes for each candidate by looping through the counts.
    # E. Determine the winning vote count and candidate.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:

        # D. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # D. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # E. Determine if the votes is greater than the winning_count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # E. If true, reset winning count and winning percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # E. Set the winning candidate's name
            winning_candidate = candidate_name

        # E. Conclusion
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Conclusion
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )

    print(winning_candidate_summary)