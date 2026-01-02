from pathlib import Path
# Service to analyze log files
LOG_FILE = Path(__file__).resolve().parents[2] / "app.log" 

def analyze_logs():
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                if "INFO" in line:
                    counts["INFO"] += 1
                elif "WARNING" in line:
                    counts["WARNING"] += 1
                elif "ERROR" in line:
                    counts["ERROR"] += 1
        return counts
    except FileNotFoundError:
        return {"error": "Log file not found"}
