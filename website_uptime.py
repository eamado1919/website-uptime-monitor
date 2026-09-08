# Website Uptime Monitor
# Checks multiple websites, records HTTP status codes,
# handles request errors, adds timestamps,
# summarizes uptime results, and saves monitoring history.

# Import requests for website checks
import requests

# Import datetime for timestamps
from datetime import datetime

# -----------------------------
# FUNCTIONS
# -----------------------------

def check_website(url):
    print(f"\nChecking website: {url}")

    try:
        # Added a standard User-Agent header to prevent automated access blocks
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

        response = requests.get(url, headers=headers, timeout=10)

        print(f"HTTP Status Code: {response.status_code}")
        return response.status_code

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")
        return None


def get_status_message(status_code):
    if status_code is None:
        return "Website could not be reached."

    if 200 <= status_code < 300:
        return "Website is UP!"

    elif 300 <= status_code < 400:
        return "Website returned a redirect."

    elif 400 <= status_code < 500:
        return "Website returned a client error."

    elif 500 <= status_code < 600:
        return "Website returned a server error."

    else:
        return "Unexpected HTTP status."


def save_results_to_file(results, up_count, down_count):

    # Name of the file where monitoring history will be saved
    file_name = "website_monitoring_history.txt"

    # Open the file in append mode.
    # "a" means add new information without deleting previous runs.
    with open(file_name, "a", encoding="utf-8") as file:

        # Record when this monitoring run was saved
        run_time = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

        file.write("\nWEBSITE UPTIME MONITOR\n")
        file.write(f"Run Time: {run_time}\n")
        file.write("-" * 40 + "\n")

        # Loop through every website dictionary stored in results
        for result in results:

            file.write(f"Website: {result['website']}\n")
            file.write(f"Status Code: {result['status_code']}\n")
            file.write(f"Status: {result['message']}\n")
            file.write(f"Checked At: {result['checked_at']}\n")
            file.write("\n")

        # Save the overall totals
        file.write("MONITORING TOTALS\n")
        file.write(f"Websites UP: {up_count}\n")
        file.write(f"Websites DOWN or unreachable: {down_count}\n")
        file.write(f"Total websites checked: {len(results)}\n")

    print(f"\nResults saved to {file_name}")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

def main():

    # List of websites that the monitor will check
    websites = [
        "https://google.com",
        "https://microsoft.com",
        "https://github.com"
]
    
    # Initialize an empty list to store the results
    results = []

    # Check each website in the websites list
    for website in websites:

        # Record when this specific website check begins
        checked_at = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

        # Check the website and save the returned status code
        status_code = check_website(website)

        # Convert the HTTP status code into a readable message
        message = get_status_message(status_code)

        print(message)

        # Create one dictionary for this website check
        result = {
            "website": website,
            "status_code": status_code,
            "message": message,
            "checked_at": checked_at,
            "monitor": "Website Uptime Monitor"
        }

        # Add the dictionary to the results list
        results.append(result)


    print("\nMONITORING SUMMARY")

    # Print each website result
    for result in results:
        print(f"\nWebsite: {result['website']}")
        print(f"Status Code: {result['status_code']}")
        print(f"Status: {result['message']}")
        print(f"Checked At: {result['checked_at']}")


    # Start counters at zero
    up_count = 0
    down_count = 0

    # Count all website results
    for result in results:

        if result["status_code"] is not None and 200 <= result["status_code"] < 300:
            up_count += 1
        else:
            down_count += 1


    # Print the totals only once
    print("\nMONITORING TOTALS")

    print(f"Websites UP: {up_count}")
    print(f"Websites DOWN or unreachable: {down_count}")
    print(f"Total websites checked: {len(results)}")

    # Save this monitoring run to the history file
    save_results_to_file(results, up_count, down_count)

# Run the program
if __name__ == "__main__":
    main()