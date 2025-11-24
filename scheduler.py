import time
import threading
import json
from datetime import datetime

def start_schedule():
    with open("config.json", "r") as f:
        cfg = json.load(f)

    schedule_type = cfg.get("schedule_type", "daily")
    daily_time = cfg.get("daily_time", "10:00")
    days = cfg.get("days", ["Monday", "Wednesday", "Friday"])

    def schedule_loop():
        from main import process_order  # import here to avoid circular import
        while True:
            now = datetime.now()
            today_name = now.strftime("%A")
            now_time = now.strftime("%H:%M")

            if schedule_type == "daily" and now_time == daily_time:
                process_order()
                time.sleep(60)  # wait 1 min after running
            elif schedule_type == "weekly" and today_name in days and now_time == daily_time:
                process_order()
                time.sleep(60)

            time.sleep(1)

    threading.Thread(target=schedule_loop, daemon=True).start()
    print(f"Scheduled {schedule_type} at {daily_time}")
