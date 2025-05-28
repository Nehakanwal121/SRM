import psutil
def suggest_optimizations(stats):
    suggestions = []

    if stats.get("cpu") > 90:
        suggestions.append("Critical CPU usage (>90%). Close unnecessary programs immediately or restart your system.")
    elif stats.get("cpu") > 80:
        suggestions.append("High CPU usage detected. Close unused applications or check background processes.")

    if stats.get("ram") > 90:
        suggestions.append("Critical RAM usage (>90%). Restart memory-intensive applications or consider upgrading RAM.")
    elif stats.get("ram") > 80:
        suggestions.append("High RAM usage detected. Consider closing some heavy applications.")

    if stats.get("disk") > 95:
        suggestions.append("Disk space critically low (>95%). Free up space immediately to avoid system issues.")
    elif stats.get("disk") > 90:
        suggestions.append("Low disk space. Delete unnecessary files or move data to external storage.")

    if stats.get("battery") is not None:
        if stats["battery"] < 10:
            suggestions.append("Battery critically low (<10%). Plug in immediately to prevent shutdown.")
        elif stats["battery"] < 20:
            suggestions.append("Battery low. Plug in or enable power saver mode.")

    return suggestions

# Define thresholds
MEMORY_THRESHOLD_MB = 500
CPU_THRESHOLD_PERCENT = 1.0
WHITELIST = ['explorer.exe', 'python.exe', 'System Idle Process']

def auto_kill_useless_processes():
    for proc in psutil.process_iter(['pid', 'name', 'memory_info', 'cpu_percent']):
        try:
            name = proc.info['name']
            memory_mb = proc.info['memory_info'].rss / (1024 * 1024)
            cpu = proc.info['cpu_percent']

            if name not in WHITELIST and memory_mb > MEMORY_THRESHOLD_MB and cpu < CPU_THRESHOLD_PERCENT:
                psutil.Process(proc.info['pid']).terminate()
                print(f"Killed: {name} (PID: {proc.info['pid']}) using {memory_mb:.2f}MB and {cpu:.2f}% CPU")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
