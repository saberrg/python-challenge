import os
import csv

# Define CSV file path and variables
csvpath = os.path.join("python-challenge/PyPoll/Resources/election_data.csv")

totalVotes = 0
candidateVotes = {}
winner = ""
winnerVotes = 0

# Read the CSV file and gather information i.e. votes, names, etc.
with open(csvpath, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    header = next(csvReader)

    for row in csvReader:
        totalVotes += 1

        candidateName = row[2]

        # If the candidate is not in the dictionary, add them with an initial vote count of 0
        if candidateName not in candidateVotes:
            candidateVotes[candidateName] = 0

        # Increment the vote count for the candidate
        candidateVotes[candidateName] += 1

# Winner calculation
winnerVotes = 0

# Print the Election Results 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")

# Iterate over the candidates and calculate their vote percentage
for candidate, votes in candidateVotes.items():
    votePercentage = (votes / totalVotes) * 100
    votePercentageFormatted = "{:.2f}".format(votePercentage)
    print(f"{candidate}: {votePercentageFormatted}% ({votes})")

    # Determine the winner based on the highest vote count and print them
    if votes > winnerVotes:
        winner = candidate
        winnerVotes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the analysis as a text file
output_path = os.path.join("python-challenge/PyPoll/analysis/analysis.txt")

with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {totalVotes}\n")
    txtfile.write("-------------------------\n")

    for candidate, votes in candidateVotes.items():
        votePercentage = (votes / totalVotes) * 100
        votePercentageFormatted = "{:.2f}".format(votePercentage)
        txtfile.write(f"{candidate}: {votePercentageFormatted}% ({votes})\n")

    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print(f"Done! Results exported to {output_path}.")
