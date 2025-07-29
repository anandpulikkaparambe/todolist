import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Calendar widget
from datetime import datetime

# Main application window
root = tk.Tk()
root.title("Advanced To-Do App")
root.geometry("800x500")

# List to store tasks
todo_list = []
task_id = 1  # for serial number

# Function to update the Treeview display
def update_treeview():
    for row in task_tree.get_children():
        task_tree.delete(row)
    for task in todo_list:
        task_tree.insert("", tk.END, values=task)

# Add task function
def add_task():
    global task_id
    task = task_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    priority = priority_entry.get()
    reason = reason_entry.get()
    finished = "✔️" if finished_var.get() else "❌"

    if not task:
        messagebox.showwarning("Input Error", "Please enter a task.")
        return

    todo_list.append((task_id, task, date, time, priority, finished, reason))
    task_id += 1
    update_treeview()

    # Clear entries
    task_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)
    reason_entry.delete(0, tk.END)
    finished_var.set(0)

# Remove selected task
def remove_task():
    selected_item = task_tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")
        return
    item = selected_item[0]
    values = task_tree.item(item, 'values')
    serial = int(values[0])

    # Remove from list
    global todo_list
    todo_list = [t for t in todo_list if t[0] != serial]
    update_treeview()
    messagebox.showinfo("Removed", f"Task {serial} removed.")

# Entry Fields and Labels
tk.Label(root, text="Task:").grid(row=0, column=0, sticky="w")
task_entry = tk.Entry(root, width=30)
task_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Select Date:").grid(row=1, column=0, sticky="w")
date_entry = DateEntry(root, width=27, background='darkblue',
                       foreground='white', date_pattern='yyyy-mm-dd')
date_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Time (HH:MM):").grid(row=2, column=0, sticky="w")
time_entry = tk.Entry(root, width=30)
time_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Priority (High/Med/Low):").grid(row=3, column=0, sticky="w")
priority_entry = tk.Entry(root, width=30)
priority_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Reason (if unfinished):").grid(row=4, column=0, sticky="w")
reason_entry = tk.Entry(root, width=30)
reason_entry.grid(row=4, column=1, padx=5, pady=5)

finished_var = tk.IntVar()
finished_check = tk.Checkbutton(root, text="Finished", variable=finished_var)
finished_check.grid(row=5, column=1, sticky="w", padx=5, pady=5)

# Buttons
add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.grid(row=6, column=0, padx=5, pady=10)

remove_btn = tk.Button(root, text="Remove Selected Task", width=20, command=remove_task)
remove_btn.grid(row=6, column=1, padx=5, pady=10)

# Treeview to display tasks
columns = ("Serial", "Task", "Date", "Time", "Priority", "Finished", "Reason")
task_tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    task_tree.heading(col, text=col)
    task_tree.column(col, width=100)
task_tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Start the app
root.mainloop()
