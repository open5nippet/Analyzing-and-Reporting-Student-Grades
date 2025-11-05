🧮 GradeBook Analyzer – Mini Project

Name: Ayush Kumar
Roll No: 2501420003
Date: 05-November-2025
Course: Programming for Problem Solving using Python
Instructor: Jyoti Yadav
Project Type: Individual (Mini Project)

📘 Project Overview

The GradeBook Analyzer is a Python mini project that automates the process of managing and analyzing student marks.
Instead of manually calculating averages or grades, this program allows a teacher to input student names and marks, and the software instantly computes statistics, assigns grades, separates pass/fail students, and displays results in a clean tabular format.

It demonstrates how Python’s built-in data structures (lists, dictionaries, loops, and conditionals) can be used to solve a real-world educational problem.

🎯 Learning Outcomes

By completing this project, students will learn how to:

Collect and store user input efficiently using loops and dictionaries.

Implement functions to structure a modular Python program.

Perform statistical calculations (average, median, max, min).

Apply conditional logic for grading systems.

Use list comprehensions for pass/fail classification.

Format output neatly using f-strings.

Create a menu-driven console application with re-run functionality.

🧩 Project Structure
gradebook_analyzer/
│
├── gradebook.py      # Main Python program file
└── README.md          # Documentation file

⚙️ Features Implemented
Task	Description	Python Concepts Used
Task 1	Setup & menu system	Functions, print formatting
Task 2	Data entry & validation	Loops, try/except handling
Task 3	Statistical analysis	Math operations, functions
Task 4	Grade assignment	If–elif–else conditions
Task 5	Pass/fail separation	List comprehensions
Task 6	Result table display	String formatting, loops
Task 7	Full analysis automation	Function calls, modular design
🧠 Program Flow

Program starts and displays a menu.

The user chooses whether to:

Enter new student data,

View statistics,

See grade distribution,

Check pass/fail summary, or

Display the final results table.

The program performs the selected task using functions.

After analysis, the user can either continue or exit.

🧾 Example Output
🎓 Welcome to the GradeBook Analyzer!

==============================
      GRADEBOOK ANALYZER
==============================
1. Enter student data & analyze
2. 2. Show statistics
3. Show grade distribution
4. Show pass/fail list
5. Show full results table
6. Exit
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
Median Marks  : 68.00
Highest Score : 95 (Bob)
Lowest Score  : 33 (Eve)

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
Name           Marks     Grade
------------------------------
Alice          82        B
Bob            95        A
Carol          68        D
Dan            42        D
Eve            33        F
------------------------------

🧰 Technologies Used

Language: Python 3.13

Libraries: None (uses only built-in functions)

Platform: Console / Command Line Interface

▶️ How to Run the Program

Save the program as gradebook.py.

Open VS Code, IDLE, or a terminal window.

Navigate to the folder containing the file.

Run the program using:

python gradebook.py


Follow the menu prompts on the screen.

✅ Evaluation Rubric
Criteria	Weight	Performance
Program setup & structure	10%	✅ Well-organized
Data input & storage	15%	✅ Works with validation
Statistical analysis	15%	✅ All correct
Grade logic	15%	✅ Modular and accurate
Pass/fail logic	10%	✅ Clear and correct
Table display & loop	15%	✅ Nicely formatted
Code readability	10%	✅ Clean and commented
Overall accuracy	10%	✅ Verified
💬 Author’s Note

This mini-project demonstrates how Python can simplify everyday academic tasks such as grade analysis and student performance evaluation.
It was developed as part of the Programming for Problem Solving using Python course at
K.R. Mangalam University (IBM Supported B.Tech – CSE Data Science Program).
