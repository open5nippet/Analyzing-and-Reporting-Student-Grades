# ------------------------------------------------------------
# Name: Ayush Kumar
# Date: 05-November-2025
# Roll No: 2501420003
# Title: GradeBook Analyzer Mini Project
# Course: Programming for Problem Solving using Python
# ------------------------------------------------------------

# Description: A Python program to collect student marks,
#              analyze grades, compute statistics, and display
#              formatted results in a looped menu interface.

# ------------------------------------------------------------
# Task 1: Project Setup and Initialization
# ------------------------------------------------------------

def show_menu():
    """Displays the main menu options"""
    print("\n==============================")
    print("      GRADEBOOK ANALYZER      ")
    print("==============================")
    print("1. Enter student data")
    print("2. Show statistics")
    print("3. Show grade distribution")
    print("4. Show pass/fail list")
    print("5. Show full results table")
    print("6. Exit")

# ------------------------------------------------------------
# Task 2: Data Entry (Manual Input)
# ------------------------------------------------------------

def get_student_data():
    """Takes student names and marks as input"""
    marks = {}
    try:
        n = int(input("Enter number of students: "))
        if n <= 0:
            print("Please enter a valid number of students.")
            return {}
        
        for i in range(n):
            name = input(f"\nEnter name of student {i+1}: ").strip()
            while True:
                try:
                    score = int(input(f"Enter marks for {name}: "))
                    if 0 <= score <= 100:
                        marks[name] = score
                        break
                    else:
                        print("Marks should be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        print("\nAll student data entered successfully!")
        return marks
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return {}

# ------------------------------------------------------------
# Task 3: Statistical Analysis Functions
# ------------------------------------------------------------

def calculate_average(marks):
    """Calculates the average of all marks"""
    if not marks:
        return 0
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    """Finds the median value from marks"""
    if not marks:
        return 0
    sorted_marks = sorted(marks.values())
    n = len(sorted_marks)
    if n % 2 == 1:
        return sorted_marks[n // 2]
    else:
        return (sorted_marks[n // 2 - 1] + sorted_marks[n // 2]) / 2

def find_max_score(marks):
    """Finds the highest score"""
    if not marks:
        return "N/A", 0
    top_student = max(marks, key=marks.get)
    return top_student, marks[top_student]

def find_min_score(marks):
    """Finds the lowest score"""
    if not marks:
        return "N/A", 0
    low_student = min(marks, key=marks.get)
    return low_student, marks[low_student]

def show_statistics(marks):
    """Displays average, median, max, and min scores"""
    print("\n--- STATISTICS ---")
    print(f"Average Marks : {calculate_average(marks):.2f}")
    print(f"Median Marks  : {calculate_median(marks):.2f}")
    max_name, max_score = find_max_score(marks)
    min_name, min_score = find_min_score(marks)
    print(f"Highest Score : {max_score} ({max_name})")
    print(f"Lowest Score  : {min_score} ({min_name})")

# ------------------------------------------------------------
# Task 4: Grade Assignment and Distribution
# ------------------------------------------------------------

def assign_grades(marks):
    """Assigns grades to each student"""
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades

def show_grade_distribution(grades):
    """Displays how many students got each grade"""
    print("\n--- GRADE DISTRIBUTION ---")
    grade_count = {}
    for g in grades.values():
        grade_count[g] = grade_count.get(g, 0) + 1
    for grade, count in grade_count.items():
        print(f"Grade {grade}: {count} student(s)")

# ------------------------------------------------------------
# Task 5: Pass/Fail Filter with List Comprehension
# ------------------------------------------------------------

def show_pass_fail(marks):
    """Shows list of passed and failed students"""
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]

    print("\n--- PASS/FAIL SUMMARY ---")
    print(f"Passed ({len(passed)}): {', '.join(passed) or 'None'}")
    print(f"Failed ({len(failed)}): {', '.join(failed) or 'None'}")

# ------------------------------------------------------------
# Task 6: Results Table and Menu Loop
# ------------------------------------------------------------

def show_results_table(marks, grades):
    """Displays the final table of students, marks, and grades"""
    print("\n--- FINAL RESULT TABLE ---")
    print(f"{'Name':<15}{'Marks':<10}{'Grade':<5}")
    print("-" * 30)
    for name in marks:
        print(f"{name:<15}{marks[name]:<10}{grades[name]:<5}")
    print("-" * 30)

# ------------------------------------------------------------
# Main Program (User Loop)
# ------------------------------------------------------------

def main():
    """Main function that runs the menu system"""
    print("Welcome to the GradeBook Analyzer!\n")
    marks = {}

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            marks = get_student_data()
        elif choice == '2':
            if marks:
                show_statistics(marks)
            else:
                print("Please enter data first.")
        elif choice == '3':
            if marks:
                grades = assign_grades(marks)
                show_grade_distribution(grades)
            else:
                print("Please enter data first.")
        elif choice == '4':
            if marks:
                show_pass_fail(marks)
            else:
                print("Please enter data first.")
        elif choice == '5':
            if marks:
                grades = assign_grades(marks)
                show_results_table(marks, grades)
            else:
                print("Please enter data first.")
        elif choice == '6':
            print("\nThank you for using GradeBook Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# ------------------------------------------------------------
# Entry Point
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
