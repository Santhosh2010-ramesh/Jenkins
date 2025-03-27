from datetime import datetime

# Get current date and time
now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Print to console
print("Current Date and Time:", formatted_time)
