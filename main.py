from datetime import datetime

# Replace these values with your birthdate
birth_year = 2002
birth_month = 7
birth_day = 27

# Create a datetime object for your birthdate
birthdate = datetime(birth_year, birth_month, birth_day)

# Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
day_of_week = birthdate.weekday()

# List of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Print the result
print("You were born on a", days_of_week[day_of_week])
