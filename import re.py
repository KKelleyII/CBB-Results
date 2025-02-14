import re
import csv

# Define the file paths
input_file = '/Users/kkelley/Desktop/CBB Results/cbbga25.csv'  # Input CSV file
output_file = '/Users/kkelley/Desktop/CBB Results/cleaned_games.csv'  # Output CSV file (with full path)

# Read the input CSV
with open(input_file, mode='r') as infile:
    lines = infile.readlines()

# Prepare a list to store cleaned data
cleaned_data = []

# Define a regular expression to capture date, teams, and scores
game_pattern = re.compile(r'(\d{2}/\d{2}/\d{4})\s+(.+?)\s+(\d+)\s+(.+?)\s+(\d+)')

# Loop through each line and process
for line in lines:
    match = game_pattern.match(line.strip())
    
    if match:
        date = match.group(1)  # The date
        team1 = match.group(2)  # First team name
        score1 = match.group(3)  # First team's score
        team2 = match.group(4)  # Second team name
        score2 = match.group(5)  # Second team's score

        # Append the cleaned data to the list
        cleaned_data.append([date, team1, team2, score1, score2])

# Write the cleaned data to a new CSV file
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Date', 'Team 1', 'Team 2', 'Score 1', 'Score 2'])  # Header row
    writer.writerows(cleaned_data)

print(f"Cleaning complete! The data has been saved to '{output_file}'.")

