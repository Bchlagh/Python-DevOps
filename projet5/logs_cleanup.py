import subprocess

def check_server_health():
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()

def check_cpu_usage(threshold_percent=80):
    result = subprocess.run(["ps", "aux", "--sort=-%cpu", "|", "head", "-n", "2"], capture_output=True, text=True)
    print("CPU Usage:")
    print(result.stdout)

def check_memory_usage(threshold_percent=80):
    result = subprocess.run(["free", "-h"], capture_output=True, text=True)
    print("Memory Usage:")
    print(result.stdout)

def check_disk_space(threshold_percent=80):
    result = subprocess.run(["df", "-h"], capture_output=True, text=True)
    print("Disk Space Usage:")
    print(result.stdout)

if __name__ == "__main__":
    check_server_health()
