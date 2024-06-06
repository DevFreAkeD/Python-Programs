import calendar

# Function to display a simple calendar for a given month and year
def display_calendar(year, month):
    # Create a TextCalendar object
    cal = calendar.TextCalendar(calendar.SUNDAY)  # Start week with Sunday

    # Get the calendar for the given month and year
    month_calendar = cal.formatmonth(year, month)

    # Print the calendar
    print("\n" + month_calendar)

# Get user input for the year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Display the calendar for the specified month and year
display_calendar(year, month)
