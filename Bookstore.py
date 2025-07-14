# Book Club Points Calculator

# student log - empty dictionary to store the values 
student_log = {}

#student name and number of books purchased to store in the dictionary
while True:
    name = input("Enter student name (or type 'quit' to stop): ")
    if name.lower() == 'quit':
        break

    books = int(input("How many books did you purchase this month? "))

# Determine points based on number of books using range logic
    if books < 2:
        points = 0
    elif books < 4:
        points = 5
    elif books < 6:
        points = 15
    elif books < 8:
     points = 30
    else:
     points = 60

# add points to "student account" (student log) 
    if name in student_log:
        student_log[name]["books"] += books
        student_log[name]["points"] += points
    else:
        student_log[name] = {"books": books, "points": points}

    print(f"\n{name} earned {points} points for purchasing {books} book(s) this month.")
    print(f"Total points earned so far: {student_log[name]['points']} points.\n")

# Display final student log

print("\nFinal student log:")
for student, data in student_log.items():
    print(f"{student.title()}: {data['books']} books, {data['points']} points")

choice = input("\nWould you like to print the entire student log? (y/n): ").strip().lower()
if choice == 'y':
    print("\nStudent Log:")
    for student, data in student_log.items():
        print(f"{student.title()}: {data['books']} books, {data['points']} points")
else:
    print("\nOkay, student log not displayed.")

