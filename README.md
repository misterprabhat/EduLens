🎓 EduLens - Student Performance Analyzer

A sleek, lightweight desktop application built with Python and Tkinter for managing student records, analyzing academic performance, and visualizing data insights.

📖 Overview

EduLens is an intuitive, desktop-based student performance management system designed for educators and administrators. It provides a clean, modern graphical user interface (GUI) to seamlessly track student marks across multiple subjects, monitor attendance eligibility, compute semester grades automatically, and render rich analytical charts.

✨ Key Features

📊 Interactive Dashboard: Get a quick bird's-eye view of class metrics, including total students, class averages, attendance rates, top-performing students, and subject-wise progress bars.

📋 Comprehensive Student Records: Maintain detailed entries covering student IDs, names, departments, semesters, individual subject marks, and attendance percentages.

⚠️ Smart Academic Reports: Automatically calculates totals, percentages, letter grades ($A+$ to $F$), and attendance eligibility flags ($\ge 75\%$), instantly highlighting short attendances.

📈 Data Visualizations: Built-in charting powered by Matplotlib featuring:

Bar Graphs for subject-wise average marks.

Pie Charts for grade distribution breakdowns.

Histograms for overall percentage spreads.

Line Plots for trend analysis and a complete Dashboard View combining all insights into a $2 \times 2$ grid.

✍️ CRUD Operations: Easily add new students with instant data validation or remove records safely via an interactive data grid.

🛠️ Tech Stack & Dependencies

Language: Python 3.x

GUI Framework: Tkinter (Standard Python library)

Data Manipulation: Pandas

Data Visualization: Matplotlib

🚀 Getting Started

Prerequisites

Make sure you have Python installed on your system. You will also need the pandas and matplotlib packages.

Installation & Setup

Clone the repository:

git clone https://github.com/your-username/edulens.git
cd edulens


Install required dependencies:

pip install pandas matplotlib


Ensure data file is ready:
Verify that a students.csv file with the correct schema is located in the root directory. Expected columns:

StudentID, Name, Department, Semester, Python Programming, Web Programming, ADBMS, ACN, AI Tools, Attendance


Run the application:

python edulens_gui.py


🖥️ Application Preview & Navigation

Home: Summary cards, top students leaderboard, and subject progress indicators.

All Students: Detailed grid of all active student records.

Academic Report: Filtered view highlighting grades, totals, and attendance alerts.

Visualizations: Interactive tabbed charts and multi-chart dashboard.

Add / Remove Student: Forms and selection tools for database updates.

🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check out the issues page.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License

Distributed under the MIT License. See LICENSE for more information.
