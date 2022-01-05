# Add dependencies and import csv and os
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Create a total vote counter
total_votes = 0
#Create list of candidates
candidate_options = []
#Create a dictionary of candidate votes
candidate_votes = {}
#Create winner variables
winning_candidate = " "
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        total_votes += 1
        #add the candidate names to the list
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #begin tracking votes
            candidate_votes[candidate_name] = 0
        # Tally votes for each candidate and add to dictionary
        candidate_votes[candidate_name] +=1

#Save the results to the text file
with open(file_to_save, "w") as txt_file:
#Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")
    print(election_results, end="")

    #Save the final vote count to the text file
    txt_file.write(election_results)

    #Iterate through the candidate list
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        
        #calculate percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #save and write percentage results
        candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        
        #Loop through and determine highest votes and percentages
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #Save and write the winner and summary        
    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)




    