import psutil

def list_processes(limit=20):
    return [(p.pid, p.name()) for p in psutil.process_iter(['pid', 'name'])][:limit]

def kill_process(pid):
    try:
        p = psutil.Process(pid)
        p.terminate()
        return True
    except Exception:
        return False
