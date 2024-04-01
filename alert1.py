import subprocess
import time
from win10toast import ToastNotifier

# Initialize ToastNotifier
toaster = ToastNotifier()
# URL to monitor
url = 'https://wsedc.ca/immigration-application/'
# Temporary file to store curl output
tmp_file = 'tmp.txt'

# Function to check the application status
def check_status():
    try:
        # Use curl to fetch webpage and save output to tmp.txt
        subprocess.run(['curl', '-s', url, '-o', tmp_file])
        # Check if the output contains the text "Application Status: CLOSED."
        with open(tmp_file, 'r') as f:
            content = f.read()
            if "Application Status: CLOSED." not in content:
                print("OOOOOOOOOOOOOOOOOOOOOOOOOOPEN")
                toaster.show_toast("OOOOOOOOOOOOOOOOOOOOOOOOOOPEN", "OOOOOOOOOOOOOOOOOOOOOOOOOOPEN!", icon_path=None, duration=10, threaded=True)
            else:
                print("Application Status: CLOSED")
    except Exception as e:
        print("An error occurred:", e)

# Main loop to continuously check the status
print("Monitoring...")
while True:
    # Call the function to check the status
    check_status()
    # Wait for 10 seconds before checking again
    time.sleep(10)
