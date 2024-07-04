import time
import psutil


def change_process_priority_if_needed(process_name, desired_priority):
    priority_map = {
        psutil.IDLE_PRIORITY_CLASS: 'low',
        psutil.BELOW_NORMAL_PRIORITY_CLASS: 'below_normal',
        psutil.NORMAL_PRIORITY_CLASS: 'normal',
        psutil.ABOVE_NORMAL_PRIORITY_CLASS: 'above_normal',
        psutil.HIGH_PRIORITY_CLASS: 'high',
        psutil.REALTIME_PRIORITY_CLASS: 'realtime'
    }

    reverse_priority_map = {v: k for k, v in priority_map.items()}

    if desired_priority not in reverse_priority_map:
        raise ValueError(f"Invalid priority level: {desired_priority}")

    desired_priority_value = reverse_priority_map[desired_priority]

    for proc in psutil.process_iter(['pid', 'name', 'nice']):
        try:
            if proc.info['name'] == process_name:
                current_priority = proc.info['nice']
                if current_priority != desired_priority_value:
                    proc.nice(desired_priority_value)
                    print(f"Changed priority of process {process_name} (PID: {proc.info['pid']}) to {desired_priority}")
                else:
                    print(f"Priority of process {process_name} (PID: {proc.info['pid']}) is already {desired_priority}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Could not change priority for process {process_name} (PID: {proc.info['pid']}): {e}")


def monitor_and_adjust_priority(process_name, desired_priority, interval=300):
    while True:
        change_process_priority_if_needed(process_name, desired_priority)
        time.sleep(interval)

def stop_process(process_name):
    """stops the process if found"""
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] == process_name:
                print(f"Stopping process {process_name} (PID: {proc.info['pid']})")
                proc.terminate()  # Attempt a graceful termination
                proc.wait(timeout=5)  # Wait for up to 5 seconds for the process to terminate
                if proc.is_running():
                    print(f"Process {process_name} did not terminate gracefully. Forcing termination...")
                    proc.kill()  # Forcefully terminate the process if it's still running
                print(f"Process {process_name} (PID: {proc.info['pid']}) stopped.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Could not stop process {process_name} (PID: {proc.info['pid']}): {e}")


if __name__ == "__main__":
    process_name_to_search = "discord.exe"
    desired_priority = "high"
    interval_in_seconds = 30  # will check every 59 seconds

    monitor_and_adjust_priority(process_name_to_search, desired_priority, interval_in_seconds)


