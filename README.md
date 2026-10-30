# 🎓 EduLens — Academic Progress Tracking & Evaluation System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-0D9488?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Charts-Matplotlib-11557C?style=for-the-badge" alt="Matplotlib">
</p>

<p align="center">
  <strong>A smarter way to understand student performance.</strong>
  <br>
  A desktop-based academic analytics application that transforms student records into meaningful insights through automated grade calculations, attendance monitoring, and interactive data visualizations.
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-technology-stack">Tech Stack</a> •
  <a href="#-getting-started">Installation</a> •
  <a href="#-application-overview">Application</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

## 📌 Overview

**EduLens** is a lightweight student performance management system developed using **Python and Tkinter**. It provides educators and administrators with a centralized interface to manage student records, evaluate academic results, monitor attendance eligibility, and explore class-wide performance trends.

Designed with usability and data clarity in mind, EduLens combines essential academic management tools with visual analytics to make student performance easier to track and understand.

### 🎯 Why EduLens?

- 📚 **Organized Records** — Keep student information and subject marks in one place.
- 🧮 **Automated Evaluation** — Calculate totals, percentages, and letter grades instantly.
- 🚦 **Attendance Monitoring** — Identify students who fall below the minimum attendance requirement.
- 📊 **Visual Insights** — Understand academic trends through charts and performance summaries.
- 🖥️ **Simple Desktop Interface** — Access essential academic tools through a graphical interface.

---

## ✨ Features

<table>
  <tr>
    <td width="50%">
      <h3>📊 Interactive Dashboard</h3>
      View total student count, class averages, attendance statistics, top performers, and subject-wise progress indicators.
    </td>
    <td width="50%">
      <h3>📋 Student Management</h3>
      Maintain student IDs, names, departments, semesters, subject marks, and attendance percentages in an organized data grid.
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>🧮 Smart Academic Reports</h3>
      Automatically calculate total marks, percentages, letter grades from A+ to F, and attendance eligibility using a 75% threshold.
    </td>
    <td width="50%">
      <h3>📈 Data Visualizations</h3>
      Explore subject averages, grade distributions, percentage distributions, and performance trends using Matplotlib.
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>✍️ Student Record Operations</h3>
      Add students with data validation and remove existing records through interactive controls.
    </td>
    <td width="50%">
      <h3>🖼️ Combined Analytics View</h3>
      Examine multiple visualizations together in a convenient 2 × 2 dashboard layout.
    </td>
  </tr>
</table>

### 📉 Explore Academic Performance

EduLens includes four types of charts to help interpret academic data:

| Visualization | Purpose |
|:--|:--|
| 📊 Bar Chart | Compare average marks across subjects |
| 🥧 Pie Chart | Analyze the distribution of student grades |
| 📶 Histogram | Understand the spread of overall percentages |
| 📈 Line Plot | Explore performance trends |

The combined dashboard brings multiple analytical views together for convenient comparison.

---

## 🛠️ Technology Stack

| Technology | Role |
|:--|:--|
| 🐍 **Python 3.x** | Core application logic and calculations |
| 🖼️ **Tkinter** | Desktop graphical user interface |
| 🐼 **Pandas** | Student data processing and analysis |
| 📊 **Matplotlib** | Charts and data visualization |
| 📄 **CSV** | Student record storage |

### 📦 Dependencies

- Python 3.x
- Pandas
- Matplotlib
- Tkinter — included with many standard Python installations; availability depends on your Python distribution.

---

## 🚀 Getting Started

Follow these steps to set up EduLens on your local machine.

### 1. Prerequisites

Ensure Python 3.x is installed.

Check your Python installation:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/edulens.git
cd edulens
```

> **Note:** Replace `your-username` with your GitHub username and use the actual repository URL.

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install pandas matplotlib
```

### 4. Prepare the Student Dataset

Place the `students.csv` file in the project's root directory.

The CSV file should contain the following columns in the expected order and format:

```csv
StudentID,Name,Department,Semester,Python Programming,Web Programming,ADBMS,ACN,AI Tools,Attendance
```

Make sure the file contains valid student records and that its column names match those expected by the application.

### 5. Launch EduLens

Run the main application:

```bash
python edulens_gui.py
```

You're ready to explore student records, generate academic reports, and visualize performance data!

---

## 🖥️ Application Overview

Navigate through the application's main sections to access its functionality.

| Section | Description |
|:--|:--|
| 🏠 **Home** | Dashboard summary cards, top-performing students, and subject progress indicators |
| 👥 **All Students** | Organized grid containing student records |
| 📝 **Academic Report** | Calculated grades, totals, percentages, and attendance alerts |
| 📊 **Visualizations** | Individual charts and a combined analytics dashboard |
| ➕ **Add Student** | Form to enter new student details with validation |
| ➖ **Remove Student** | Controls for removing selected student records |

> 💡 **Have screenshots of your application?** Add them to a `screenshots/` folder and embed them here to give visitors an immediate preview of the interface.

Example:

```markdown
<p align="center">
  <img src="screenshots/dashboard.png" width="800"
       alt="EduLens Dashboard">
  <br>
  <em>EduLens dashboard showing academic performance insights.</em>
</p>
```

---

## 📂 Project Structure

A suggested layout for organizing the project:

```text
EduLens/
├── edulens_gui.py       # Main desktop application
├── students.csv         # Student records dataset
├── screenshots/         # Application screenshots (optional)
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies (optional)
└── LICENSE              # License information
```

*Adjust this structure to match your actual repository files.*

To create a `requirements.txt` file, add:

```text
pandas
matplotlib
```

You can then install dependencies using:

```bash
pip install -r requirements.txt
```

---


## 🗺️ Future Enhancements

Potential improvements that could extend EduLens include:

- 🔍 Search and filter student records.
- 📤 Export academic reports to PDF or Excel.
- 🎨 Additional dashboard customization.
- 📅 Semester-wise performance comparisons.
- 💾 Enhanced data backup and recovery options.

*These are possible future improvements, not claims about existing functionality.*

---

## 📄 License

This project is distributed under the **MIT License**. See the [`LICENSE`](LICENSE) file for details.

---

<p align="center">
  <strong>🎓 EduLens — Turning Academic Data into Meaningful Insights.</strong>
  <br>
  <sub>Built with Python • Powered by Data • Designed for Clarity</sub>
</p>
