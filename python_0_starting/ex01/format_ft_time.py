import time

# Get the current time machine
timestamp = time.time()

# Format the current date in the format "Month Day Year" 
current_date = time.strftime("%b %d %Y", time.localtime(timestamp))

# Output the results
print(f"Seconds since January 1, 1970: {timestamp:,.4f} or",
      f"{timestamp:.2e} in scientific notation")
print(current_date)
