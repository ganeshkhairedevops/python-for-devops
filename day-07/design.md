## Script Selected
**Day-02 – API Data Fetcher**

---

## What problem am I solving?
- Manually checking data from APIs is slow and error-prone
- DevOps tools mostly exchange data through APIs
- The goal of this script is to:
  - Automatically fetch data from an API
  - Understand and parse JSON responses
  - Extract useful information
  - Store the data in a file

---

## What input does my script need?
- A public API URL (example: JSONPlaceholder API)
- No authentication or API key is required to run the script
- The user only needs to run the script

---

## What output should my script give?

### Terminal Output:
- Whether the API call was successful or failed
- Extracted data (ID, title, userId)

### File Output:
- A JSON file (`output.json`)
- Structured and processed API data

---

## What are the main steps?
1. Define the API endpoint
2. Call the API using the `requests` library
3. Convert the response into JSON format
4. Extract the required fields
5. Print the data to the terminal
6. Save the processed data to a JSON file
7. Ensure the script does not crash if an error occurs

---

## Script Selected
**Day-01 & Day-03 – System Health Monitoring Script**

---

## What problem am I solving?
- Day-01 script was working but not safe for real-world usage
- If user entered wrong input, script could crash
- Code was written in a single function and was hard to maintain
- In DevOps, scripts should be:
  - Safe to run
  - Easy to read
  - Easy to modify

The goal of Day-03 is to improve code quality without changing the core logic.

---

## What input does my script need?
- CPU threshold value (percentage)
- Memory threshold value (percentage)
- Disk usage threshold value (percentage)
- All inputs are provided by the user via terminal

---

## What output should my script give?

### Terminal Output:
- Current CPU, Memory, and Disk usage
- Clear status messages:
  - Resource in safe state
  - Alert triggered if threshold is exceeded

---

## What improvements are added in Day-03?
- Code organized into multiple functions
- Proper and meaningful variable names
- Added basic error handling using `try / except`
- Script exits safely if invalid input is provided
- Improved readability following basic Python best practices

---

## What are the main steps?
1. Take threshold values from the user
2. Validate user input (numeric values only)
3. Fetch system metrics using `psutil`
4. Compare current usage with thresholds
5. Print health status to the terminal
6. Exit safely if any error occurs

---

## Final Thought
Day-03 focused on **writing better code, not more code**.  
Improving existing scripts is a critical DevOps skill that makes automation reliable and production-ready.
