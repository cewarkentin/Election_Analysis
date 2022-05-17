# Election Analysis

## Overview of Project

A Colorado Board of Elections employee has given us the following tasks to complete the election audit of a recent local congressional election: 

- Calculate the total number of votes cast
- Get a complete list of candidates who received votes.
- Calculate the total number of votes each candidate received.
- Calculate the percentage of votes each candidate won.
- Determine the winner of the election based on popular vote.

### Resources

- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.67.1

### Output Summary

The analysis of the election shows:
- There were "x" votes cast in the election.
- The candidates were:
  - Candidate 1
  - Candidate 2
  - Candidate 3
- The candidate results were:
  - Candidate 1 received "y%" of the vote and "z" number of votes.
  - Candidate 2 received "y%" of the vote and "z" number of votes.
  - Candidate 3 received "y%" of the vote and "z" number of votes.
- The winner of the election was:
  - Candidate (1, 2, or 3), who received "y%" of the vote and "z" number of votes.

## Election Audit Results

![Candidate_results](https://github.com/cewarkentin/Election_Analysis/blob/main/Candidate%20results.png)

- There were 369,711 total votes cast in this congressional election.
  - Charles Casper Stockham received 23.0% of the vote and 85,213 individual votes.
  - Diana DeGette received 73.8% of the vote and 272,892 individual votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 individual votes.
- Diana DeGette won the congressional election with 73.8% of the vote and 272,892 individual votes.

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Which county had the largest number of votes?

## Election Audit Summary

In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

Given that the incoming data is a CVS file of a similar format for data storage, this Python script is ready for use for future elections. With modification, this script can be used to analyze data in other file types or formatting. 

The same logic can be used to analyze data for elections beyond just selecting a candidate--if there are ballot measures or other proposals, the output script can be adjusted to appropriately announce the winners for those votes as well.

If an election is determined by something other than popular vote, the logic for determining a winner can be adjusted to appropriately select the winner according to whatever rules are required. To do so, all we would have to do is adjust the

if (votes > winning_count) and (vote_percentage > winning_percentage):

statement.
