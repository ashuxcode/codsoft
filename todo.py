import tkinter as tk
from tkinter import messagebox
import json
import os

# File name to save tasks
FILENAME = "tasks.json"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Function to save tasks to file
def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(task_list, file)

# Add new task
def add_task():
    task = entry.get().strip()
    if task != "":
        task_list.append({"title": task, "done": False})
        entry.delete(0, tk.END)
        refresh_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Empty Task", "Please enter a task first!")

# Delete selected task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        task_list.pop(selected)
        refresh_listbox()
        save_tasks()
    except:
        messagebox.showwarning("No Selection", "Select a task to delete.")

# Mark task as done/undone
def toggle_task():
    try:
        selected = listbox.curselection()[0]
        task_list[selected]["done"] = not task_list[selected]["done"]
        refresh_listbox()
        save_tasks()
    except:
        messagebox.showwarning("No Selection", "Select a task to mark done/undone.")

# Refresh listbox with current tasks
def refresh_listbox():
    listbox.delete(0, tk.END)
    for task in task_list:
        title = task["title"]
        if task["done"]:
            title += " (Done)"
        listbox.insert(tk.END, title)

# ----------------- GUI -----------------
root = tk.Tk()
root.title("To-Do List")
root.geometry("350x350")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=25)
entry.pack(side=tk.LEFT, padx=5)

btn_add = tk.Button(frame, text="Add", width=8, command=add_task)
btn_add.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

btn_delete = tk.Button(btn_frame, text="Delete", width=12, command=delete_task)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_done = tk.Button(btn_frame, text="Mark Done/Undone", width=15, command=toggle_task)
btn_done.pack(side=tk.LEFT, padx=5)

# Load tasks at start
task_list = load_tasks()
refresh_listbox()

root.mainloop()
