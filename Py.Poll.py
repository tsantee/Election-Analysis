# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who recieved votes
# 3. Total number of votes each candidate won
# 4. Percentage of votes each candidate won
# 5. The winner of the elction based on popular vote
#import the datetime class form the datetime module
import datetime as dt
now = dt.datetime.now()
print("The time right now is ", now)

# Open the election results and read the file
#Add Dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Cnadidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print Header row in the CSV file.
    headers = next(file_reader)

    
# Print each row in the CSV file.
    for row in file_reader:
        #Add the total vote count
        total_votes += 1
# Print the Candidate name from each row
        candidate_name = row[2]
# If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
# Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
    # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
# Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

#save the final vote count to the text file.
    txt_file.write(election_results)

# Determine the percentage of votes for each candidate by looping through the counts
#1. Iterate through the candidate list
    for candidate_name in candidate_votes:
    # get vote count of each candidate
        votes = candidate_votes[candidate_name]
    #calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    #print the candidate name and percentage of votes
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

        # If true then then set winning_count = votes and winning_percent.
        # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

        # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name


    #print out candidates voting percentage and votes
    

    # save the winning candidate results to our text file

    #print out the winning candidate, vote count and % to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

#print the winning candidate summary
    print(winning_candidate_summary)

#save to txt file
    txt_file.write(winning_candidate_summary)





# print the total votes

# To do: read and analyze the data here.

    


