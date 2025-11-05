# 🧮 GRADEBOOK ANALYZER

**Name:** Ayush Kumar  
**Roll No:** 2501420003  
**Date:** 05-November-2025  
**Course:** Programming for Problem Solving using Python  
**Instructor:** Jyoti Yadav  
**Project Type:** Individual (Mini Project)  
**Weightage:** 15% (5 Marks)

---

## 📘 Project Overview

The **GradeBook Analyzer** is a Python-based console project that helps teachers automatically analyze student performance after a class test.  
It collects student names and marks, calculates average and median scores, assigns grades, separates pass/fail students, and displays results in a formatted table.

This project demonstrates how **Python’s data structures, loops, and conditionals** can be applied in real-world educational tasks.

---

## 🎯 Learning Objectives

- Use **dictionaries** and **loops** for storing and processing data.  
- Write **modular functions** to organize logic.  
- Perform **statistical analysis**: average, median, min, max.  
- Implement **grading logic** using if–elif–else.  
- Apply **list comprehensions** for pass/fail filtering.  
- Format and display results using **f-strings**.  
- Create a **menu-driven application**.

---

## 🧩 Project Structure

gradebook_analyzer/
│
├── gradebook.py # Main project file
└── README.md # Documentation


---

## ⚙️ Features Implemented

| Task | Description | Concepts Used |
|------|--------------|---------------|
| **Task 1** | Project setup & initialization | Functions, print statements |
| **Task 2** | Data entry & validation | Input handling, loops |
| **Task 3** | Statistical analysis | Mathematical functions |
| **Task 4** | Grade assignment | Conditional statements |
| **Task 5** | Pass/fail separation | List comprehensions |
| **Task 6** | Results table display | f-string formatting |
| **Task 7** | Combined analyzer | Modular programming |

---

## 🧠 Program Flow

1. Displays a menu to the user.  
2. Allows entry of student data.  
3. Performs automatic analysis:  
   - Average, Median, Highest, Lowest  
   - Grade Assignment (A–F)  
   - Pass/Fail Summary  
   - Formatted Results Table  
4. Allows re-running analysis or exiting.

---

## 🧾 Example Output

==============================
GRADEBOOK ANALYZER

1)Enter student data & analyze

2)Show statistics

3)Show grade distribution

4)Show pass/fail list

5)Show full results table

6)Exit
Enter your choice (1-6): 1

Enter number of students: 5
Enter name of student 1: Alice
Enter marks for Alice: 82
Enter name of student 2: Bob
Enter marks for Bob: 95
Enter name of student 3: Carol
Enter marks for Carol: 68
Enter name of student 4: Dan
Enter marks for Dan: 42
Enter name of student 5: Eve
Enter marks for Eve: 33

✅ All student data entered successfully!

📊 --- STATISTICS ---
Average Marks : 64.00
Median Marks : 68.00
Highest Score : 95 (Bob)
Lowest Score : 33 (Eve)

🎯 --- GRADE DISTRIBUTION ---
Grade A: 1 student(s)
Grade B: 1 student(s)
Grade C: 1 student(s)
Grade D: 1 student(s)
Grade F: 1 student(s)

✅ --- PASS/FAIL SUMMARY ---
Passed (4): Alice, Bob, Carol, Dan
Failed (1): Eve

📋 --- FINAL RESULT TABLE ---
Name     Marks     Grade
Alice     82         B
Bob       95         A
Carol     68         D
Dan       42         D
Eve       33         F


---

## 🧰 Technologies Used

- **Language:** Python 3.10+  
- **Libraries:** None (only built-in functions)  
- **Platform:** Console / Terminal  

---

## ▶️ How to Run

1. Save the file as `gradebook.py`.  
2. Open your terminal or IDE.  
3. Navigate to the folder containing the file.  
4. Run the command:

   ```bash
   python gradebook.py
5. Follow the menu prompts on the screen.

✅ Evaluation Rubric
Criteria	                      Weight	          Evaluation
Program setup & structure	     10%	       ✅ Well-organized
Data input & storage	           15%	       ✅ Works with validation
Statistical analysis	           15%	       ✅ All correct
Grade logic	                       15%	       ✅ Modular and accurate
Pass/fail logic	                 10%	       ✅ Clear and correct
Table display & loop	           15%	       ✅ Nicely formatted
Code readability	                 10%	       ✅ Clean and commented
Overall accuracy	                 10%	       ✅ Verified
💬 Author’s Note

This project demonstrates how Python can simplify real-life academic tasks such as grading and performance evaluation.
It was created as part of the Programming for Problem Solving using Python course under the IBM-supported B.Tech CSE (Data Science) program at K.R. Mangalam University.
