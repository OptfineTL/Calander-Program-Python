# Importing calendar module
import calendar

# Function to print calendar
def print_calendar(year, month):
    # Using calendar to print calendar
    print(calendar.month(year, month))

# Driver code
if __name__ == "__main__":
    # Taking input from user
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    # Printing calendar
    print_calendar(year, month)