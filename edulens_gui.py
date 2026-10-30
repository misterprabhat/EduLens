# EduLens - Student Performance Analyzer (Tkinter Version)
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

FILE_NAME = "students.csv"
SUBJECTS = ["Python Programming", "Web Programming", "ADBMS", "ACN", "AI Tools"]
FIELDS = ["StudentID", "Name", "Department", "Semester"] + SUBJECTS + ["Attendance"]
CHARTS = ["Bar Graph", "Pie Chart", "Histogram", "Line Plot"]
NAVY, YELLOW, GREY, RED, GREEN, BLUE = "#1E2A44", "#F4C430", "#F3F5F9", "#C0392B", "#2E8B57", "#4C72B0"
FONT, BOLD, BIG = ("Arial", 11), ("Arial", 11, "bold"), ("Arial", 20, "bold")
content = None     # The area where each page is shown (created in main)
menu_buttons = {}  # The menu buttons (created in main)

# Convert percentage into a grade
def get_grade(percentage):
    for limit, grade in [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D")]:
        if percentage >= limit:
            return grade
    return "F"

# Read the CSV and add calculated columns (returns None on error)
def load_data():
    try:
        data = pd.read_csv(FILE_NAME)
    except FileNotFoundError:
        data = None
    if data is None or list(data.columns) != FIELDS:
        messagebox.showerror("Error", "The file students.csv was not found or has wrong columns.")
        return None
    data[SUBJECTS + ["Attendance"]] = data[SUBJECTS + ["Attendance"]].apply(pd.to_numeric)
    data["Total"] = data[SUBJECTS].sum(axis=1)
    data["Percentage"] = data["Total"] / len(SUBJECTS)
    data["Grade"] = data["Percentage"].apply(get_grade)
    data["Status"] = data["Attendance"].apply(lambda a: "Eligible" if a >= 75 else "Short Attendance")
    return data

# Shortcuts for making a label, a white box and a flat button
def label(parent, message, font=FONT, colour=NAVY, bg="white"):
    return tk.Label(parent, text=message, font=font, fg=colour, bg=bg)
def card(parent):
    return tk.Frame(parent, bg="white", highlightbackground="#D9DFEA", highlightthickness=1)
def button(parent, message, command, colour=YELLOW, text_colour=NAVY):
    return tk.Button(parent, text=message, font=BOLD, bg=colour, fg=text_colour, relief="flat",
                     activebackground=colour, activeforeground=text_colour, padx=14, pady=5,
                     cursor="hand2", command=command)

# Clear the page, show a heading, return the data
def new_page(heading):
    for widget in content.winfo_children():
        widget.destroy()
    label(content, heading, BIG, bg=GREY).pack(anchor="w", padx=30, pady=(20, 4))
    tk.Frame(content, bg=YELLOW, height=3, width=50).pack(anchor="w", padx=30, pady=(0, 12))
    return load_data()

# Show a pandas table (striped rows; short attendance rows turn red)
def show_table(data, columns, highlight=False):
    box = card(content)
    box.pack(fill="both", expand=True, padx=30, pady=(0, 12))
    table = ttk.Treeview(box, columns=columns, show="headings")
    for column in columns:
        table.heading(column, text=column.split()[0])  # "Python Programming" -> "Python"
        table.column(column, anchor="center", minwidth=50, width=120 if column in ("Name", "Department") else 75)
    table.tag_configure("even", background="#EEF2F9")
    table.tag_configure("short", background="#FDE2E0", foreground=RED)
    for number, (_, row) in enumerate(data[columns].iterrows()):
        values = [f"{round(v, 2):g}" if isinstance(v, float) else v for v in row]
        short = highlight and row["Status"] == "Short Attendance"
        table.insert("", "end", values=values, tags=("short" if short else "even" if number % 2 else "",))
    table.pack(fill="both", expand=True)
    return table

def show_home():
    data = new_page("Welcome to EduLens")
    if data is None:
        return
    short = int((data["Status"] == "Short Attendance").sum())
    summary = [("Total Students", len(data), NAVY),
               ("Class Average", f"{data['Percentage'].mean():.1f}%", NAVY),
               ("Average Attendance", f"{data['Attendance'].mean():.1f}%", NAVY),
               ("Short Attendance", short, RED if short else GREEN)]
    row = tk.Frame(content, bg=GREY)
    row.pack(fill="x", padx=26)
    for number, (title, value, colour) in enumerate(summary):
        row.columnconfigure(number, weight=1, uniform="cards")
        box = card(row)
        box.grid(row=0, column=number, sticky="ew", padx=4)
        label(box, title, colour="#6B7690").pack(pady=(12, 0))
        label(box, value, BIG, colour).pack(pady=(0, 12))
    bottom = tk.Frame(content, bg=GREY)
    bottom.pack(fill="x", padx=26, pady=10)
    left, right = card(bottom), card(bottom)
    for box in (left, right):
        box.pack(side="left", fill="both", expand=True, padx=4)
    label(left, "Top 5 Students", BOLD).pack(anchor="w", padx=15, pady=(12, 6))
    for rank, (_, student) in enumerate(data.nlargest(5, "Percentage").iterrows(), start=1):
        label(left, f"{rank}.  {student['Name']}  -  {student['Percentage']:.2f}%").pack(anchor="w", padx=15, pady=3)
    label(right, "Average Marks by Subject", BOLD).pack(anchor="w", padx=15, pady=(12, 6))
    for subject in SUBJECTS:
        line = tk.Frame(right, bg="white")
        line.pack(anchor="w", padx=15, pady=3)
        label(line, subject.split()[0], BOLD).pack(side="left")
        ttk.Progressbar(line, length=170, maximum=100, value=data[subject].mean()).pack(side="left", padx=8)
        label(line, f"{data[subject].mean():.1f}").pack(side="left")

def show_students():
    data = new_page("All Students")
    if data is not None:
        show_table(data, FIELDS)

def show_report():
    data = new_page("Academic Report")
    if data is None:
        return
    show_table(data, ["StudentID", "Name", "Total", "Percentage", "Grade", "Status"], True)
    names = data[data["Status"] == "Short Attendance"]["Name"]
    if not names.empty:  # Warning for students who are short on attendance
        label(content, "Warning: Short Attendance - " + ", ".join(names), BOLD, RED, GREY).pack(anchor="w", padx=30, pady=(0, 14))

def show_add_student():
    data = new_page("Add New Student")
    if data is None:
        return
    box = card(content)
    box.pack(anchor="w", padx=30, pady=(0, 10))
    entries = []
    for number, title in enumerate(FIELDS):  # One label and one entry box per field
        label(box, title).grid(row=number, column=0, sticky="w", padx=(20, 25), pady=3)
        entries.append(tk.Entry(box, font=FONT, width=26))
        entries[-1].grid(row=number, column=1, padx=(0, 20), pady=3)

    # Check the details, then save the new student to the CSV file
    def save():
        v = [entry.get().strip() for entry in entries]
        try:
            row = [int(v[0]), v[1], v[2], int(v[3])] + [float(x) for x in v[4:]]
        except ValueError:
            messagebox.showerror("Error", "Student ID and Semester must be whole numbers, and marks and attendance must be numbers.")
            return
        checks = [(row[0] in data["StudentID"].values, "This Student ID already exists."),
                  (not v[1] or not v[2], "Name and Department cannot be empty."),
                  (row[3] < 1 or not all(0 <= x <= 100 for x in row[4:]),
                   "Semester must be 1 or more, and marks and attendance must be between 0 and 100.")]
        for failed, message in checks:
            if failed:
                messagebox.showerror("Error", message)
                return
        pd.DataFrame([row], columns=FIELDS).to_csv(FILE_NAME, mode="a", header=False, index=False)  # Append one row
        messagebox.showinfo("Success", "The student was added successfully.")
        show_add_student()
    button(content, "Save Student", save).pack(anchor="w", padx=30, pady=8)

def show_remove_student():
    data = new_page("Remove Student - Select One")
    if data is None:
        return
    table = show_table(data, ["StudentID", "Name", "Department", "Semester"])

    def remove():
        if not table.selection():
            messagebox.showwarning("Warning", "Please select a student first.")
            return
        student_id, name = table.item(table.selection()[0])["values"][:2]
        if messagebox.askyesno("Confirm", f"Are you sure you want to remove {name}?"):
            # Keep every student except the selected one, then save the file again
            data[data["StudentID"].astype(str) != str(student_id)][FIELDS].to_csv(FILE_NAME, index=False)
            messagebox.showinfo("Success", f"{name} was removed successfully.")
            show_remove_student()
    button(content, "Remove Selected Student", remove, RED, "white").pack(anchor="w", padx=30, pady=(0, 14))

# Draw one chart on "ax" (a plotting area), so it works alone or in the dashboard
def draw_chart(ax, kind, data):
    if kind == "Bar Graph":
        data[SUBJECTS].mean().plot(kind="bar", ax=ax, rot=20, edgecolor="black")
    elif kind == "Pie Chart":
        data["Grade"].value_counts().plot(kind="pie", ax=ax, autopct="%1.1f%%", ylabel="")
    elif kind == "Histogram":
        ax.hist(data["Percentage"], bins=10, color=BLUE, edgecolor="black")
    else:
        ax.plot(SUBJECTS, data[SUBJECTS].mean(), marker="o", color=RED)
        ax.tick_params(axis="x", rotation=20)
    ax.set_title(kind)

def show_charts():
    data = new_page("Visualizations")
    if data is None:
        return
    buttons = tk.Frame(content, bg=GREY)
    buttons.pack(anchor="w", padx=30, pady=(0, 10))
    area = card(content)
    area.pack(fill="both", expand=True, padx=30, pady=(0, 14))

    def draw(name):
        for widget in area.winfo_children():
            widget.destroy()
        figure = Figure(figsize=(8, 5))
        kinds = CHARTS if name == "Dashboard" else [name]
        size = 2 if name == "Dashboard" else 1  # A 2x2 grid of charts, or a single chart
        for number, kind in enumerate(kinds, start=1):
            draw_chart(figure.add_subplot(size, size, number), kind, data)
        figure.tight_layout()
        canvas = FigureCanvasTkAgg(figure, master=area)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    for name in CHARTS + ["Dashboard"]:
        button(buttons, name, lambda n=name: draw(n)).pack(side="left", padx=(0, 8))
    draw("Bar Graph")

# Highlight the chosen menu button, then show its page
def go(name, page):
    for button_name, menu_button in menu_buttons.items():
        menu_button.configure(bg=YELLOW if button_name == name else NAVY, fg=NAVY if button_name == name else "white")
    page()

def main():
    global content
    root = tk.Tk()
    root.title("EduLens - Student Performance Analyzer")
    root.geometry("1100x650")
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", rowheight=28, font=("Arial", 10), borderwidth=0)
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background=NAVY, foreground="white")
    style.map("Treeview", background=[("selected", YELLOW)], foreground=[("selected", NAVY)])

    sidebar = tk.Frame(root, bg=NAVY, width=210)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)
    label(sidebar, "EduLens", ("Arial", 24, "bold"), YELLOW, NAVY).pack(pady=(28, 24))
    pages = [("Home", show_home), ("All Students", show_students), ("Academic Report", show_report),
             ("Visualizations", show_charts),
             ("Add New Student", show_add_student), ("Remove Student", show_remove_student),
             ("Exit", root.destroy)]
    for name, page in pages:
        menu_buttons[name] = tk.Button(
            sidebar, text=name, font=FONT, bg=NAVY, fg="white", relief="flat", anchor="w",
            activebackground=YELLOW, activeforeground=NAVY, padx=24, pady=9, cursor="hand2",
            command=lambda n=name, p=page: go(n, p))
        menu_buttons[name].pack(fill="x", pady=1)

    content = tk.Frame(root, bg=GREY)
    content.pack(side="right", fill="both", expand=True)
    go("Home", show_home)
    root.mainloop()

if __name__ == "__main__":
    main()
