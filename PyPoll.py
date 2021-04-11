# Add our dependencies.
import csv
import os

#Assign a variable for the absolute path. This is not covered in class.
mainpath = os.path.dirname(__file__)
# Assign a variable to load a file from a path.
file_to_load = os.path.join(mainpath, "Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join(mainpath, "analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    #print(election_data)
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
    
    # Read the header row.
    headers = next(file_reader)
    # Print the header row.
    #print(headers)

    # 2. Add to the total vote count.
    # Iterate through each row in the CSV file. 
    # Then assign total_votes as total of row
    for row in file_reader:
        total_votes += 1
# 3. Print total votes
print(total_votes)