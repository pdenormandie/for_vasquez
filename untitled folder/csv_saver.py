"""Pathways to Success Part 2."""
# Import the csv library
import csv
from pathlib import Path
def save_loan_values():
    # Create a path to the csv file called daily_rate_sheet.csv
    csvpath = "daily_rate_sheet.csv"
    # Open the csv path, read the data, and print each row
    with open(csvpath) as csvfile:
        data = csv.reader(csvfile)
        
    """Extension.

    Create a variable above the `for` loop named `Counter`
    and set it equal to zero. Then, every time a new row
    is read within the `for` loop, add a value of 1 to
    this variable.
    """

    csvpath = Path("daily_rate_sheet.csv")
    counter = 0
    with open(csvpath) as csvfile:
        data = csv.reader(csvfile)
        
            # For every new row, add one to `counter`
        

            # Print the row counter and then the row
        
        

    import csv
    from pathlib import Path

    data = [
        {
            
        },
        {
            "first_name": "Samantha",
            "last_name": "Jones",
            "pin": 456
        }
    ]

    csvpath = Path("my_output.csv")
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in data:
            csvwriter.writerow(row.values())
