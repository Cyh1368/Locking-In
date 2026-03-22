import tkinter as tk
from tkinter import ttk, messagebox
from src.scenario_selector import ScenarioSelector
from src.notification_overlay import NotificationOverlay
from src.debug_view import DebugView
from src.consent_flow import ConsentFlow
from src.survey import UserSurvey
import os

class VirtualDesktop:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Computer - Locking-In Demo")
        self.root.geometry("800x600")
        
        # Consent
        consent = ConsentFlow()
        if not consent.show_consent(self.root):
            messagebox.showinfo("Consent Required", "Consent declined. Exiting.")
            self.root.quit()
            return
        
        # Scenario selector
        self.scenario_selector = ScenarioSelector(self.root, self.on_scenario_change)
        self.current_scenario = "normal"
        
        # Desktop area
        self.desktop_frame = tk.Frame(self.root, bg="lightblue")
        self.desktop_frame.pack(fill=tk.BOTH, expand=True)
        
        # App icons
        self.create_app_icons()
        
        # Work area
        self.work_text = tk.Text(self.desktop_frame, height=10, width=50)
        self.work_text.insert(tk.END, "Work Area: Type your tasks here...\n")
        self.work_text.pack(pady=20)
        
        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X)
        tk.Button(button_frame, text="Debug View", command=self.show_debug).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Run Survey", command=self.run_survey).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Exit", command=self.root.quit).pack(side=tk.RIGHT, padx=5)
        
        # Gmail mock
        self.gmail_window = None
        
    def create_app_icons(self):
        apps = ["Instagram", "Gmail", "Texts", "Work"]
        self.app_buttons = {}
        
        for i, app in enumerate(apps):
            btn = tk.Button(self.desktop_frame, text=app, width=10, height=3, 
                          command=lambda a=app: self.open_app(a))
            btn.place(x=50 + i*120, y=50)
            self.app_buttons[app] = btn
    
    def on_scenario_change(self, scenario):
        self.current_scenario = scenario
        messagebox.showinfo("Scenario Changed", f"Scenario set to: {scenario}")
    
    def open_app(self, app_name):
        if app_name == "Work":
            self.work_text.focus()
            return
        
        if app_name == "Gmail":
            self.show_gmail()
            return
        
        # For other apps, show notification overlay
        def on_action(action):
            if action == "proceed":
                messagebox.showinfo(f"{app_name} Opened", f"You proceeded to open {app_name}")
            elif action == "snooze":
                messagebox.showinfo("Snoozed", f"{app_name} access snoozed")
            elif action == "block":
                messagebox.showinfo("Blocked", f"{app_name} blocked for 10 minutes")
            elif action == "override":
                messagebox.showinfo(f"{app_name} Opened", f"You overrode and opened {app_name}")
        
        overlay = NotificationOverlay(app_name, self.current_scenario, on_action)
        overlay.show_overlay()
    
    def show_gmail(self):
        if self.gmail_window and self.gmail_window.winfo_exists():
            self.gmail_window.lift()
            return
        
        self.gmail_window = tk.Toplevel(self.root)
        self.gmail_window.title("Gmail - Inbox")
        self.gmail_window.geometry("600x400")
        
        tk.Label(self.gmail_window, text="Inbox", font=("Arial", 14)).pack(pady=10)
        
        # Mock emails
        emails = [
            "Welcome to Gmail",
            "Important: Project Update",
            "Social notification",
            "Newsletter"
        ]
        
        for email in emails:
            tk.Label(self.gmail_window, text=email, anchor="w", width=50).pack(fill=tk.X, padx=10)
    
    def show_debug(self):
        debug_win = tk.Toplevel(self.root)
        debug_win.title("Debug View")
        debug_win.geometry("600x400")
        DebugView(debug_win)
    
    def run_survey(self):
        survey = UserSurvey(self.root)
        responses = survey.show_survey()
        messagebox.showinfo("Survey Complete", f"Thanks! Satisfaction: {responses.get('satisfaction', 'N/A')}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualDesktop(root)
    root.mainloop()