import datetime
from src.mock_services import MockCalendar, MockTasks, MockInbox
from src.config import load_config
from src.logger import Logger

class DecisionEngine:
    def __init__(self):
        self.config = load_config()
        self.recency_threshold = self.config.get("recency_threshold", 10)  # minutes
        self.priority_contacts = self.config.get("priority_contacts", ["Boss"])
        self.last_open = {}  # app -> timestamp
        self.cooldowns = {}  # app -> end_time
        self.logger = Logger()

    def record_app_open(self, app_name):
        self.last_open[app_name] = datetime.datetime.now()

    def is_on_cooldown(self, app_name):
        if app_name in self.cooldowns:
            return datetime.datetime.now() < self.cooldowns[app_name]
        return False

    def set_cooldown(self, app_name, minutes=10):
        self.cooldowns[app_name] = datetime.datetime.now() + datetime.timedelta(minutes=minutes)

    def evaluate_action(self, app_name, scenario):
        if self.is_on_cooldown(app_name):
            action, reason = "soft-block", "On cooldown from previous block."
            self.logger.log_decision(app_name, scenario, action, reason, {"cooldown": True})
            return action, reason

        cal = MockCalendar(scenario)
        tasks = MockTasks(scenario)
        inbox = MockInbox(scenario)

        inputs = {
            "cal_events": len(cal.get_upcoming_events()),
            "active_tasks": len(tasks.get_active_tasks()),
            "unread_count": inbox.get_unread_count(),
            "important_msgs": len(inbox.get_important_messages()),
            "last_open": self.last_open.get(app_name)
        }

        # Check recency
        last = self.last_open.get(app_name)
        if last and (datetime.datetime.now() - last).total_seconds() < self.recency_threshold * 60:
            if inbox.get_unread_count() == 0:
                action, reason = "nudge", f"You checked {app_name} recently and have no unread items."
                self.logger.log_decision(app_name, scenario, action, reason, inputs)
                return action, reason

        # Check calendar
        events = cal.get_upcoming_events(30)
        for event in events:
            if event.get("importance") == "high":
                action, reason = "soft-block", f"Upcoming high-importance event: {event['title']}."
                self.logger.log_decision(app_name, scenario, action, reason, inputs)
                return action, reason

        # Check important messages
        important = inbox.get_important_messages()
        if important:
            action, reason = "allow", f"Important message from {important[0]['sender']}: {important[0]['subject']}."
            self.logger.log_decision(app_name, scenario, action, reason, inputs)
            return action, reason

        # Check tasks
        active_tasks = tasks.get_active_tasks()
        if active_tasks:
            action, reason = "nudge", f"You have active tasks like '{active_tasks[0]['title']}' — focus on that?"
            self.logger.log_decision(app_name, scenario, action, reason, inputs)
            return action, reason

        action, reason = "allow", "No issues detected."
        self.logger.log_decision(app_name, scenario, action, reason, inputs)
        return action, reason

# Example usage
if __name__ == "__main__":
    engine = DecisionEngine()
    engine.record_app_open("Instagram")
    action, reason = engine.evaluate_action("Instagram", "no_unread")
    print(f"Action: {action}, Reason: {reason}")