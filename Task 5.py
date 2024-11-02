import tkinter as tk
from tkinter import ttk, messagebox

class CGPACalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # self is the main application window of type TK
        self.title("CGPA Calculator")
        
        # Courses and their credit hours
        self.courses = [
            ('OOP', 3),
            ('OOP Lab', 1),
            ('English', 2),
            ('IST', 2)
        ]
        
        # a full window frame to contain all objects
        full_window_frame = ttk.Frame(self)
        full_window_frame.grid(row=0, column=0, padx=10, pady=10)       
        
        # Course labels and entry widgets
        for i, (course, credit_hours) in enumerate(self.courses):
            label = ttk.Label(full_window_frame, text=course)
            label.grid(row=i, column=0, padx=10, pady=10)

            entry_var = tk.DoubleVar()
            entry = ttk.Entry(full_window_frame, justify="right", width=20)
            entry.grid(row=i, column=1, padx=10, pady=10, sticky="w")
            entry["textvariable"] = entry_var

            setattr(self, f"{course.lower()}_var", entry_var)
        
        # Action buttons for CGPA calculation
        self.calculate_cgpa_button = ttk.Button(full_window_frame, text="Calculate CGPA")
        self.calculate_cgpa_button.grid(row=len(self.courses), column=0, columnspan=2, padx=10, pady=10)
        # bind with left mouse button
        self.calculate_cgpa_button.bind('<Button-1>', self.calculate_cgpa)

    def calculate_cgpa(self, event):
        total_credit_hours = sum(credit_hours for _, credit_hours in self.courses)
        total_weighted_marks = sum(self.get_weighted_marks(course, credit_hours) for course, credit_hours in self.courses)
        
        cgpa = total_weighted_marks / total_credit_hours
        messagebox.showinfo(title="CGPA Calculation", message=f"Your CGPA is: {cgpa:.2f}")

    def get_weighted_marks(self, course, credit_hours):
        percentage_marks = getattr(self, f"{course.lower()}_var").get()
        if type(percentage_marks)== str or percentage_marks<0 or percentage_marks>100:
            raise Exception('str objects,negative objects,or marks greater than 100 cannot me operate')
        else:
            if percentage_marks >= 80:
                return 4 * credit_hours
            elif 65 <= percentage_marks < 80:
                return 3 * credit_hours
            elif 50 <= percentage_marks < 65:
                return 1 * credit_hours
            else:
                return 0

def main():
    CGPACalculator().mainloop()

main()
