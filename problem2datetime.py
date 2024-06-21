# Problem2: Write a program to find out the day from the given date in between 2000-2020

#import important libraries  
from datetime import date, datetime

# Get the current date
current_date = date.today()

# Define the given date in the 'DD-MM-YYYY' format
given_date_str = input("DD-MM-YYYY: ")
given_date = datetime.strptime(given_date_str, "%d-%m-%Y").date()

# Find the difference between the given date and the current date
delta = current_date - given_date

# Print the number of days
print(f"Number of days from today to {given_date}: {delta.days} days")

