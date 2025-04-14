import tkinter as tk
from tkinter import messagebox
import csv
def welcome_employee(username, department, colleagues):
    # New window to welcome the employee
    window = tk.Toplevel(root)
    window.title("Welcome Employee")
    window.geometry("400x300")
    
    welcome_label = tk.Label(window, text=f"Welcome {username}!\nDepartment: {department}")
    welcome_label.pack(pady=10)
    
    colleague_label = tk.Label(window, text="Other members in your department:")
    colleague_label.pack()

    for colleague in colleagues:
        if colleague != username:
            name_label = tk.Label(window, text=colleague)
            name_label.pack()

def submit():
    username = username_entry.get().strip()
    department = department_entry.get().strip()
    
    found = False
    colleagues = []

    try:
        with open('GIG-logistics.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'].strip().lower() == username.lower() and row['Department'].strip().lower() == department.lower():
                    found = True
                if row['Department'].strip().lower() == department.lower():
                    colleagues.append(row['Name'].strip())

    except FileNotFoundError:
        messagebox.showerror("Error", "Employee database not found.")
        return

    if found:
        welcome_employee(username, department, colleagues)
    else:
        messagebox.showinfo("Not Found", f"Employee {username} in {department} department does not exist.")

# Create main window
root = tk.Tk()
root.title("GIG Logistics - Employee Verification")
root.geometry("400x250")

# Username label and entry
username_label = tk.Label(root, text="Enter your Name:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Department label and entry
department_label = tk.Label(root, text="Enter your Department:")
department_label.pack(pady=5)
department_entry = tk.Entry(root)
department_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

# Run the application
root.mainloop()