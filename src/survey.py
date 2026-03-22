import tkinter as tk
from tkinter import simpledialog

class UserSurvey:
    def __init__(self, root):
        self.responses = {}

    def show_survey(self):
        survey_win = tk.Toplevel(root)
        survey_win.title("Locking-In User Survey")
        survey_win.geometry("400x300")
        survey_win.attributes("-topmost", True)
        
        tk.Label(survey_win, text="How satisfied are you with the attention assistant?", font=("Arial", 12)).pack(pady=10)
        
        scale = tk.Scale(survey_win, from_=1, to=5, orient=tk.HORIZONTAL, label="1 (Not satisfied) to 5 (Very satisfied)")
        scale.pack(pady=10)
        
        tk.Label(survey_win, text="Any feedback?").pack()
        feedback = tk.Text(survey_win, height=5, width=40)
        feedback.pack(pady=10)
        
        def submit():
            self.responses["satisfaction"] = scale.get()
            self.responses["feedback"] = feedback.get(1.0, tk.END).strip()
            survey_win.destroy()
        
        tk.Button(survey_win, text="Submit", command=submit).pack(pady=10)
        
        root.wait_window(survey_win)
        return self.responses

if __name__ == "__main__":
    root = tk.Tk()
    survey = UserSurvey(root)
    responses = survey.show_survey()
    print("Survey responses:", responses)
    root.destroy()