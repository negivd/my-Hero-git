# Import the psutil library to get system performance information
import psutil
import time

# Define a CPU usage threshold (in percentage)
THRESHOLD = 80

# Print a startup message
print("Monitoring CPU usage...")

try:
    # Run indefinitely until the user stops the program (e.g., Ctrl+C)
    while True:
        # Get the current CPU usage percentage over a short interval
        cpu_usage = psutil.cpu_percent(interval=1)

        # Check if the CPU usage exceeds the threshold
        if cpu_usage > THRESHOLD:
            print(f"⚠️ Alert! CPU usage exceeds threshold: {cpu_usage}%")

        # Optional: wait for a short duration before checking again
        # (not strictly needed since interval=1 already adds a 1-second delay)
        time.sleep(1)

except KeyboardInterrupt:
    # Handle the case when the user manually stops the program
    print("\nMonitoring stopped by user.")

except Exception as e:
    # Handle any unexpected errors (e.g., permission issues, library errors)
    print(f"An error occurred during monitoring: {e}")
