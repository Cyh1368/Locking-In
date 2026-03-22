import tkinter as tk
from tkinter import messagebox
from src.decision_engine import DecisionEngine

class NotificationOverlay:
    def __init__(self, app_name, scenario, on_action):
        self.app_name = app_name
        self.scenario = scenario
        self.on_action = on_action
        self.engine = DecisionEngine()
        self.action_taken = None

    def show_overlay(self):
        action, reason = self.engine.evaluate_action(self.app_name, self.scenario)
        
        root = tk.Toplevel()
        root.title(f"Locking-In: {self.app_name} Access")
        root.geometry("400x200")
        root.attributes("-topmost", True)
        
        tk.Label(root, text=f"Attempting to open {self.app_name}", font=("Arial", 12)).pack(pady=10)
        tk.Label(root, text=f"Decision: {action.upper()}", font=("Arial", 10, "bold")).pack()
        tk.Label(root, text=reason, wraplength=350).pack(pady=10)
        
        frame = tk.Frame(root)
        frame.pack(pady=10)
        
        if action == "allow":
            tk.Button(frame, text="Proceed", command=lambda: self.handle_action("proceed", root)).pack(side=tk.LEFT, padx=5)
        elif action == "nudge":
            tk.Button(frame, text="Proceed", command=lambda: self.handle_action("proceed", root)).pack(side=tk.LEFT, padx=5)
            tk.Button(frame, text="Snooze", command=lambda: self.handle_action("snooze", root)).pack(side=tk.LEFT, padx=5)
        elif action == "soft-block":
            tk.Button(frame, text="Override", command=lambda: self.handle_action("override", root)).pack(side=tk.LEFT, padx=5)
            tk.Button(frame, text="Block (10m)", command=lambda: self.handle_action("block", root)).pack(side=tk.LEFT, padx=5)
        
        root.mainloop()
        return self.action_taken

    def handle_action(self, action, root):
        self.action_taken = action
        if action == "block":
            self.engine.set_cooldown(self.app_name, 10)
        self.on_action(action)
        root.destroy()

# For demo
if __name__ == "__main__":
    def callback(act):
        print(f"User chose: {act}")
    overlay = NotificationOverlay("Instagram", "focus_meeting", callback)
    result = overlay.show_overlay()
    print(f"Overlay result: {result}")