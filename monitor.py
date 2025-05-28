import psutil
import platform
import time

def get_system_stats():
    stats = {
        'cpu': psutil.cpu_percent(interval=1),
        'ram': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent,
        'battery': psutil.sensors_battery().percent if psutil.sensors_battery() else None,
        'uptime': time.time() - psutil.boot_time(),
        'process_count': len(psutil.pids()),
        'os': platform.system()
    }
    return stats
