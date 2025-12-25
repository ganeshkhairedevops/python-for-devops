import psutil


def get_thresholds():
    """Get threshold values from user"""
    try:# Handle invalid input gracefully
        cpu_threshold = int(input("Enter CPU threshold (%): ")) # Get CPU threshold from user
        memory_threshold = int(input("Enter Memory threshold (%): ")) # Get Memory threshold from user
        disk_threshold = int(input("Enter Disk threshold (%): ")) # Get Disk threshold from user
        return cpu_threshold, memory_threshold, disk_threshold
    except ValueError: # Handle invalid input gracefully
        print("Invalid input! Please enter numbers only.")
        return None


def get_system_usage():
    """Fetch current system usage"""
    cpu_usage = psutil.cpu_percent(interval=1) # get current cpu usage
    memory_usage = psutil.virtual_memory().percent # get current memory usage
    disk_usage = psutil.disk_usage('/').percent # get current disk usage
    return cpu_usage, memory_usage, disk_usage 


def check_usage(resource_name, usage, threshold):
    """Compare usage with threshold"""
    print(f"{resource_name} Usage: {usage}%")
    if usage > threshold:
        print(f"{resource_name} alert email sent...")
    else:
        print(f"{resource_name} in safe state")


def check_system_health():
    thresholds = get_thresholds()
    if thresholds is None:
        return

    cpu_threshold, memory_threshold, disk_threshold = thresholds
    cpu_usage, memory_usage, disk_usage = get_system_usage()

    print("\n--- System Health Check ---")
    check_usage("CPU", cpu_usage, cpu_threshold)
    check_usage("Memory", memory_usage, memory_threshold)
    check_usage("Disk", disk_usage, disk_threshold)


if __name__ == "__main__":
    check_system_health()
