import csv

# Define file path (assuming the CSV file is in the same folder as the script)
csvpath = "budget_data.csv"

# Open CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # Read and store header row

    # Initialize variables
    total_months = 0
    total_profit = 0
    previous_profit = None
    changes = []

    # Process data rows
    for row in csvreader:
        # Count months
        total_months += 1

        # Calculate profit/loss
        current_profit = int(row[1])
        total_profit += current_profit

        # Calculate change in profit (skip first row)
        if previous_profit is not None:
            change = current_profit - previous_profit
            changes.append(change)
        previous_profit = current_profit

    # Calculate average change (avoid division by zero)
    if len(changes) > 0:
        average_change = sum(changes) / len(changes)
    else:
        average_change = 0

    # Find greatest increase and decrease
    greatest_increase = max(changes)
    greatest_decrease = min(changes)

    # Find corresponding dates for greatest changes
    greatest_increase_date = ""
    greatest_decrease_date = ""
    for row in csvreader:  # Loop through each row in the CSV reader
        if int(row[1]) == greatest_increase:
            greatest_increase_date = row[0]  # Assuming date is in the first column (index 0)
        elif int(row[1]) == greatest_decrease:
            greatest_decrease_date = row[0]

# Print analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")  # Format to 2 decimal places
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Write analysis to text file (optional)
with open("analysis.txt", "w") as textfile:  # Assuming the text file is in the same folder
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_profit}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
