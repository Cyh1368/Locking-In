import tkinter as tk
from tkinter import ttk

class ScenarioSelector:
    def __init__(self, root, on_scenario_change):
        self.frame = ttk.LabelFrame(root, text="Scenario Selector")
        self.frame.pack(pady=10, padx=10, fill="x")
        
        self.scenarios = ["normal", "no_unread", "urgent_message", "focus_meeting", "busy"]
        self.var = tk.StringVar(value="normal")
        
        ttk.Label(self.frame, text="Select Scenario:").pack(side=tk.LEFT, padx=5)
        self.combo = ttk.Combobox(self.frame, textvariable=self.var, values=self.scenarios, state="readonly")
        self.combo.pack(side=tk.LEFT, padx=5)
        self.combo.bind("<<ComboboxSelected>>", lambda e: on_scenario_change(self.var.get()))

if __name__ == "__main__":
    root = tk.Tk()
    selector = ScenarioSelector(root, lambda s: print(f"Scenario changed to: {s}"))
    root.mainloop()