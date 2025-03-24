#Tyson Blatter 2-22-25 8.1
#this is where we keep details about the student
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.total_credits= 0
        self.total_points = 0
#Define each grade letter into it's GPA
    def add_course(self, credits, grade):
        grade_points = {
            "A" : 4.0,
            "B" : 3.0,
            "C" : 2.0,
            "D" : 1.0,
            "F" : 0.0,
        }
        points = credits * grade_points[grade.upper()]
        self.total_credits += credits
        self.total_points += points
#this is how we will calculate their GPA
    def calculate_gpa(self):
        if self.total_credits == 0:
            return 0.0
        return self.total_points / self.total_credits

    #user starts to input their information
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    student = Student(first_name, last_name)
#this is where the user will keep adding grades until they are finished
    while True:
        more_courses = input("Would you like to add more courses? (Y/N): ").upper()
        if more_courses != "Y":
            break

        try:
            credits = int(input("How many credits was your course worth?: "))
            grade = input("Enter your grade: ")
            student.add_course(credits, grade)
        except ValueError:
            print("Oops, please enter a valid number or grade!")
#shows off their GPA to the nearest 2 decimals
    print(f"\n{student.first_name} {student.last_name}'s cumulative GPA is {student.calculate_gpa():.2f}")

main()