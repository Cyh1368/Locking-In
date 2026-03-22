import json
import datetime

class MockCalendar:
    def __init__(self, scenario="normal"):
        self.scenario = scenario
        self.events = self._load_events()

    def _load_events(self):
        if self.scenario == "focus_meeting":
            return [{"title": "Focus Session", "start": datetime.datetime.now() + datetime.timedelta(minutes=5), "importance": "high"}]
        return []  # Normal: no events

    def get_upcoming_events(self, minutes_ahead=60):
        now = datetime.datetime.now()
        return [e for e in self.events if e["start"] <= now + datetime.timedelta(minutes=minutes_ahead)]

class MockTasks:
    def __init__(self, scenario="normal"):
        self.scenario = scenario
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        if self.scenario == "busy":
            return [{"title": "Finish report", "priority": "high"}]
        return []  # Normal: no tasks

    def get_active_tasks(self):
        return self.tasks

class MockInbox:
    def __init__(self, scenario="normal"):
        self.scenario = scenario
        self.unread_count = self._load_count()
        self.important_messages = self._load_important()

    def _load_count(self):
        if self.scenario == "no_unread":
            return 0
        elif self.scenario == "urgent_message":
            return 1
        return 5  # Default

    def _load_important(self):
        if self.scenario == "urgent_message":
            return [{"sender": "Boss", "subject": "Urgent: Review needed", "priority": "high"}]
        return []

    def get_unread_count(self):
        return self.unread_count

    def get_important_messages(self):
        return self.important_messages

# Example usage
if __name__ == "__main__":
    cal = MockCalendar("focus_meeting")
    tasks = MockTasks("busy")
    inbox = MockInbox("urgent_message")
    print("Calendar events:", cal.get_upcoming_events())
    print("Active tasks:", tasks.get_active_tasks())
    print("Unread count:", inbox.get_unread_count())
    print("Important messages:", inbox.get_important_messages())