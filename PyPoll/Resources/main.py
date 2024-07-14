import csv

# Define file path (assuming the CSV file is in the same folder)
csvpath = "election_data.csv"

# Initialize variables
total_votes = 0
candidate_votes = {}  # Dictionary to store candidate votes
winner = ""
winning_vote_count = 0

# Open CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip header row

    # Process data rows
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Get candidate name
        candidate = row[2]

        # Update candidate votes (initialize if not present)
        if candidate not in candidate_votes.keys():
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Find winner based on most votes
for candidate, votes in candidate_votes.items():
    if votes > winning_vote_count:
        winner = candidate
        winning_vote_count = votes

# Print analysis results
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------")

# Print candidate votes with percentages
for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.2f}% ({votes})")

# Print winner
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")

# Write analysis to text file (optional)
with open("analysis.txt", "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("------------------------\n")
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        textfile.write(f"{candidate}: {vote_percentage:.2f}% ({votes})\n")
    textfile.write("------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("------------------------\n")
