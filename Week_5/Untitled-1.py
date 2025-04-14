import tkinter as tk
from tkinter import messagebox as msgbox

#Handling button click event
def button_click():
    #print("Button clicked")

    #Show an information message box
    msgbox.showinfo("Info", "Welcome to COS102 GUI App!\n")

    #Ask for user confirmation
    result = msgbox.askyesno("Confirmation", "Do you want to continue")

#Create the main Window
root = tk.Tk()
root.title("Home page")
root.geometry("300x100")

#Add a label widget
label = tk.Label(root, text="Hello Friend \n")
label. pack()

#Add a button widget
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

#Styiling the button widget
button.config(fg="red", bg="yellow")

#Start the evnt loop
root.mainloop()
