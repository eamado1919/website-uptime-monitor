# Website Uptime Monitor

A Python-based monitoring tool that checks the availability of multiple websites, records HTTP status codes, handles request errors, adds timestamps, summarizes uptime results, and saves monitoring history to a text file.

## Business Purpose

This project demonstrates how Python can be used to automate a basic operational monitoring process.

Instead of manually checking whether websites are available, the program sends HTTP requests to multiple websites, evaluates the responses, records the results, and saves a monitoring history for future review.

## Features

* Checks multiple websites automatically
* Uses HTTP status codes to determine website availability
* Handles connection errors and failed requests
* Records timestamps for each website check
* Stores results using Python dictionaries and lists
* Calculates total websites up and down
* Saves monitoring history to a text file
* Preserves prior monitoring runs using append mode

## Technologies Used

* Python
* requests library
* datetime module
* File handling

## Python Concepts Demonstrated

* Variables
* Functions
* Parameters and return values
* Loops
* Lists
* Dictionaries
* Conditional logic
* try/except error handling
* f-strings
* HTTP requests
* datetime and timestamps
* File writing
* Append mode
* main() program structure

## Example Output

```text
Checking website: https://google.com
HTTP Status Code: 200
Website is UP!

Checking website: https://microsoft.com
HTTP Status Code: 200
Website is UP!

MONITORING TOTALS
Websites UP: 3
Websites DOWN or unreachable: 0
Total websites checked: 3

Results saved to website_monitoring_history.txt
```

## Files

`website_uptime.py`
Main Python program that performs the website checks and records monitoring results.

`website_monitoring_history.txt`
Stores the historical monitoring results from each program run.

## How to Run

Install the requests library:

```bash
pip install requests
```

Run the program:

```bash
python website_uptime.py
```

## Future Enhancements

Possible future improvements include:

* Email or Teams alerts when a website is unavailable
* Scheduled monitoring
* CSV or database storage
* Dashboard reporting
* Response-time tracking
* Cloud deployment
* Automated notifications for repeated failures

## What I Learned

This project helped reinforce practical Python concepts by applying them to a real monitoring use case. I practiced working with APIs and HTTP requests, handling errors, structuring data using lists and dictionaries, using timestamps, organizing code into functions, and saving results for historical tracking.
