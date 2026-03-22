import json
import datetime
import os

LOG_FILE = "logs.json"

class Logger:
    def __init__(self):
        self.logs = self.load_logs()

    def load_logs(self):
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                return json.load(f)
        return []

    def save_logs(self):
        with open(LOG_FILE, "w") as f:
            json.dump(self.logs, f, indent=2, default=str)

    def log_decision(self, app_name, scenario, action, reason, inputs):
        entry = {
            "timestamp": datetime.datetime.now(),
            "app_name": app_name,
            "scenario": scenario,
            "action": action,
            "reason": reason,
            "inputs": inputs
        }
        self.logs.append(entry)
        self.save_logs()

# Integrate into decision engine
# In decision_engine.py, after evaluate_action:
# logger = Logger()
# logger.log_decision(app_name, scenario, action, reason, {"cal_events": len(cal.get_upcoming_events()), ...})