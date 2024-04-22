import tkinter as tk 

class GradingWindow(tk.Tk):
    def __init__(self, assignment_list):
        super().__init__()
        self.geometry("400x400")                                                                       
        self.title("grading") 
        
        self.create_widgets(self, assignment_list)
    
    
    def create_widgets(self, assignment_list):
        self.net_id_label = tk.Label(self, text="NetID")   
        self.student_netid = tk.Entry(self)
        
        self.assignment = tk.Spinbox(self, from_=, to=10, increment=1)
        
        self.score_label = tk.Label(self, text="Score")  
        self.student_score = tk.Entry(self)
        
        self.assignment.grid(row = 0, column=0,padx=5, pady=5)
        self.net_id_label.grid(row = 1, column=0,padx=5, pady=5)
        self.student_netid.grid(row=1, column=1,padx=5, pady=5)
        self.score_label.grid(row=2, column=0,padx=5, pady=5)
        self.student_score.grid(row=2, column=1,padx=5, pady=5)