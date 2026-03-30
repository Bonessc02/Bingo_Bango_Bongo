import csv

def read_grades_file():
    filename = "grades.csv"

    with open(filename, mode="r", newline="") as file:
        reader = csv.reader(file)

        print("\n--- Student Grades ---\n")

        for row in reader:
            print("{:<12} {:<12} {:<8} {:<8} {:<8}".format(*row))

if __name__ == "__main__":
    read_grades_file()