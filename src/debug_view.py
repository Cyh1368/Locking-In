import tkinter as tk
from tkinter import scrolledtext
import json
import os

class DebugView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.text_area = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        
        self.load_logs()
        
        tk.Button(self.frame, text="Refresh", command=self.load_logs).pack()

    def load_logs(self):
        log_file = "logs.json"
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                logs = json.load(f)
            self.text_area.delete(1.0, tk.END)
            for log in logs[-10:]:  # Last 10 entries
                self.text_area.insert(tk.END, json.dumps(log, indent=2, default=str) + "\n---\n")
        else:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, "No logs found.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Locking-In Debug View")
    root.geometry("600x400")
    view = DebugView(root)
    root.mainloop()