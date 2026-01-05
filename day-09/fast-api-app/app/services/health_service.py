import psutil
import boto3
from pathlib import Path
# Service to check system, log, and AWS health
LOG_FILE = Path(__file__).resolve().parents[2] / "app.log"

def get_system_health():
    return {
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "memory_usage_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage('/').percent
    }

def get_log_health():
    error_count = 0
    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                if "ERROR" in line:
                    error_count += 1
        return {"error_count": error_count, "status": "ok" if error_count == 0 else "errors detected"}
    except FileNotFoundError:
        return {"status": "log file not found"}

def get_aws_health():
    try:
        sts = boto3.client("sts")
        sts.get_caller_identity()
        return {"status": "connected"}
    except Exception:
        return {"status": "not connected"}

def get_full_health():
    return {
        "api_status": "running",
        "system_health": get_system_health(),
        "log_health": get_log_health(),
        "aws_health": get_aws_health()
    }
