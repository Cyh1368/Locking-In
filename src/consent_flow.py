import tkinter as tk
from tkinter import messagebox

class ConsentFlow:
    def __init__(self):
        self.consented = False

    def show_consent(self, root):
        consent_win = tk.Toplevel(root)
        consent_win.title("Locking-In Consent")
        consent_win.geometry("500x300")
        consent_win.attributes("-topmost", True)
        
        tk.Label(consent_win, text="Locking-In Privacy Notice", font=("Arial", 14, "bold")).pack(pady=10)
        text = tk.Text(consent_win, wrap=tk.WORD, height=10)
        text.pack(pady=10)
        text.insert(tk.END, """
We collect local usage data to help reduce attention loss:
- App open events and timestamps
- Decision logs for improvement
- Settings and preferences

Data is stored locally only. No data is sent externally.
We respect your privacy and provide opt-out options.

By proceeding, you consent to local data collection.
""")
        text.config(state=tk.DISABLED)
        
        def accept():
            self.consented = True
            consent_win.destroy()
        
        def decline():
            self.consented = False
            consent_win.destroy()
        
        tk.Button(consent_win, text="Accept", command=accept).pack(side=tk.LEFT, padx=20, pady=10)
        tk.Button(consent_win, text="Decline", command=decline).pack(side=tk.RIGHT, padx=20, pady=10)
        
        root.wait_window(consent_win)
        return self.consented

if __name__ == "__main__":
    root = tk.Tk()
    flow = ConsentFlow()
    consented = flow.show_consent(root)
    print(f"Consented: {consented}")
    root.destroy()