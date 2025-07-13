students = []

def load_records():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 7:
                    name = parts[0]
                    roll_number = int(parts[1])
                    marks = list(map(int, parts[2].split(",")))
                    total_marks = int(parts[3])
                    percentage = float(parts[4])
                    grade = parts[5]
                    student = {
                        "name": name,
                        "roll_number": roll_number,
                        "marks": marks,
                        "total_marks": total_marks,
                        "percentage": percentage,
                        "grade": grade
                    }
                    students.append(student)
    except FileNotFoundError:
        pass

def save_record(student):
    with open("students.txt", "a") as file:
        line = f"{student['name']}|{student['roll_number']}|{','.join(map(str, student['marks']))}|{student['total_marks']}|{student['percentage']}|{student['grade']}|\n"
        file.write(line)

def add_record():
    name = input("enter student name: ")
    roll_number = int(input("enter student roll number: "))
    try:
        marks1 = int(input("enter marks of subject1: "))
        marks2 = int(input("enter marks of subject2: "))
        marks3 = int(input("enter marks of subject3: "))
        marks4 = int(input("enter marks of subject4: "))
        marks5 = int(input("enter marks of subject5: "))
    except ValueError:
        print("❌ invalid, please enter marks in numbers")
        return

    total_marks = marks1 + marks2 + marks3 + marks4 + marks5
    percentage = total_marks / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": name,
        "roll_number": roll_number,
        "marks": [marks1, marks2, marks3, marks4, marks5],
        "total_marks": total_marks,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)
    save_record(student)
    print(f"✅ Record added for {name} (Roll No: {roll_number})")

def view_student():
    if not students:
        print("❌ No record is found")
    else:
        print("\n📄 All students record:")
        for i in students:
            print("-" * 40)
            print(f"name: {i['name']}")
            print(f"roll number: {i['roll_number']}")
            print(f"marks: {i['marks']}")
            print("total_marks:", i["total_marks"])
            print(f"percentage: {i['percentage']:.2f}%")
            print(f"grade: {i['grade']}")
            print("-" * 40)

def find_student():
    id = int(input("enter roll number: "))
    for i in students:
        if id == i["roll_number"]:
            print("Name:", i["name"])
            print("Roll number:", i["roll_number"])
            print("Marks:", i["marks"])
            print("Total Marks:", i["total_marks"])
            print("Percentage:", i["percentage"])
            print("Grade:", i["grade"])
            return
    print("❌ student not found")

def main():
    load_records()
    print("🎓 Welcome to Sadia's Student Result Management System 🎓")
    while True:
        print("\n📚 Menu:")
        print("1 - Add student record")
        print("2 - View all student records")
        print("3 - Search by roll number")
        print("4 - Exit")
        choice = input("enter your choice: ")
        if choice == "1":
            add_record()
        elif choice == "2":
            view_student()
        elif choice == "3":
            find_student()
        elif choice == "4":
            print("👋 stay updated")
            break
        else:
            print("❌ invalid input, please enter a valid number")

main()
