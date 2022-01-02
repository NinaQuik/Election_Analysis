# Retrieve data
# calculate total number of votes
# Create list of candidates who received votes
# Determine the total number of votes each candidate won
# Calculate the percentage of votes each candidate won
# The winner of the popular vote
# Add dependencies and import csv and os
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:

#To do: perform analysis
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    print(headers)


#Use the with statement to open the file as a text file


    