import csv


def create_grades_file():
    filename = "grades.csv"

    num_students = int(input("Enter number of students: "))

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write Header
        writer.writerow(["First Name", "Last Name","Exam 1","Exam 2","Exam 3"])


        # Input for Students Data
        for i in range(num_students):
            print(f"\nStudent {i+1}:")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            exam_1 = input("Enter Exam 1: ")
            exam_2 = input("Enter Exam 2: ")
            exam_3 = input("Enter Exam 3: ")


            writer.writerow([first_name,last_name,exam_1,exam_2,exam_3])

    print("\nData Successfully Written Onto grades.csv")

if __name__ == "__main__":
    create_grades_file()