# get the number of hours, minutes, and seconds from the user
hours = int(input())
minutes = int(input())
seconds = int(input())

# calculate number of seconds from hours (3600 seconds in an hour)
seconds += hours * 3600

# calculate the number of seconds from minutes (60 seconds in a minute)
seconds += minutes * 60

print(f"Seconds: {seconds}")