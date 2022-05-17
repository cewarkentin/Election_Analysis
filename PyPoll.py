# Goals:
    # A. The total number of votes cast
    # B. A complete list of candidates who received votes
    # C. The total number of votes each candidate won
    # D. The percentage of votes each candidate won
    # E. The winner of the election based on popular vote

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

# A/Y. Initialize a total vote counter
total_votes = 0

# B. Create a list to contain candidate names
candidate_options = []

# C. Declare an empty dictionary to count votes for each candidate
candidate_votes = {}

# E. Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# X. County options
county_options = []

# X. Empty dictionary for county votes
county_votes = {}

# Z. Determine the county with the most votes
top_voting_county = ""
top_voting_county_count = 0
top_voting_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:

        # A/Y. Add to the total vote count
        total_votes += 1

        # B. Find the candidate name from each row
        candidate_name = row[2]

        # X. Print the county name from each row.
        county_name = row[1]

        # B. If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # B. Add it to the list of candidates
            candidate_options.append(candidate_name)

            # C. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # C. Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # X. If the county name does not match any existing county ...
        if county_name not in county_options:

            # X. Add it to the list of counties
            county_options.append(county_name)

            # X. Begin tracking that county's vote count
            county_votes[county_name] = 0

        # X. Add a vote to that county's count
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    # Y. Determine the percentage of votes for each county by looping through the counts
    # # Y. Iterate through the county list
    for county_name in county_votes:
        # Y. Retrieve vote counts for a county
        cvotes = county_votes[county_name]

        # Y. Calculate percentage of votes
        cvote_percentage = float(cvotes) / float(total_votes) * 100

        # Z. Determine the top voting county
        # Z. Determine which county has the largest number of votes
        if (cvotes > top_voting_county_count) and (cvote_percentage > top_voting_county_percentage):
            # If true, set top_voting_county_count and top_voting_county_percentage
            top_voting_county_count = cvotes
            top_voting_county_percentage = cvote_percentage

            # Set top voting county name
            top_voting_county = county_name
        
        # Print counties, percentages, and votes
        county_script = f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n"
        txt_file.write(county_script)
        
        top_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {top_voting_county}\n"
        f"-------------------------\n")
    
    print(top_county_summary)
    txt_file.write(top_county_summary)

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

        # Conclusion
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
    
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)    