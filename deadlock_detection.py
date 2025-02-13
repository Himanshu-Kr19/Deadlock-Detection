import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

num_processes = 0
num_resources = 0

def detect_deadlock():
    global num_processes, num_resources

    allocated = []
    max_need = []
    available = []

    for i in range(num_processes):
        allocated_resources = list(map(int, entry_allocated[i].get().split()))
        allocated.append(allocated_resources)

    for i in range(num_processes):
        max_resources = list(map(int, entry_max[i].get().split()))
        max_need.append(max_resources)

    available = list(map(int, entry_available.get().split()))

    work = available[:]
    finish = [False] * num_processes

    while True:
        for i in range(num_processes):
            if not finish[i] and all(allocated[i][j] + work[j] >= max_need[i][j] for j in range(num_resources)):
                work = [work[j] + allocated[i][j] for j in range(num_resources)]
                finish[i] = True

        if all(finish):
            messagebox.showinfo("Result", "No deadlock detected")
            return

        if not any(finish):
            messagebox.showinfo("Result", "Deadlock detected")
            return

app = tk.Tk()
app.title("Deadlock Detection")

num_processes = simpledialog.askinteger("Input", "Enter the number of processes: ")
num_resources = simpledialog.askinteger("Input", "Enter the number of resources: ")

allocated_label = ttk.Label(app, text="Allocated Resources")
allocated_label.grid(row=0, column=0)
max_label = ttk.Label(app, text="Maximum Need")
max_label.grid(row=0, column=1)

entry_allocated = []
entry_max = []

for i in range(num_processes):
    entry_allocated_row = ttk.Entry(app)
    entry_allocated_row.grid(row=i + 1, column=0)
    entry_allocated.append(entry_allocated_row)

    entry_max_row = ttk.Entry(app)
    entry_max_row.grid(row=i + 1, column=1)
    entry_max.append(entry_max_row)

available_label = ttk.Label(app, text="Available Resources")
available_label.grid(row=num_processes + 1, column=0)
entry_available = ttk.Entry(app)
entry_available.grid(row=num_processes + 1, column=1)

detect_button = ttk.Button(app, text="Detect Deadlock", command=detect_deadlock)
detect_button.grid(row=num_processes + 2, columnspan=2)

app.mainloop()
