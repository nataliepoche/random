# inputs
seconds = int(input())

# convert to hours (3600 seconds in an hour)
hours = seconds // 3600 # Gives the total hours
seconds = seconds % 3600 # Gives the excess seconds to convert to minutes

# convert to minutes (60 seconds is 1 minute)
minutes = seconds // 60 # Takes the seconds left over from hours and converts to minutes
seconds = seconds % 60 # Gives the excess seconds

print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")