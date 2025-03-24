#TysonBlatter 3/2/25 10.2
# this code stores the employee basic info
class Employee:
    def __init__(self, name, gender, hourly_pay_rate, employee_number):
        self.name = name
        self.gender = gender
        self.hourly_pay_rate = hourly_pay_rate
        self.employee_number = employee_number

#set up the getters and setters
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate

    def get_employee_number(self):
        return self.employee_number

    def set_employee_number(self, employee_number):
        self.employee_number = employee_number

#this is where we add our shift information
class ProductionWorker(Employee):
    def __init__(self, name, gender, hourly_pay_rate, employee_number, shift_number):
        super().__init__(name, gender, hourly_pay_rate, employee_number)
        self.shift_number = shift_number

    def get_shift_number(self):
        return self.shift_number

    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

#this is the main chunk of code that will help display the worker's information
def main():
    employee1 = Employee("Tyson Blatter", "Male", 20.5, 3139505)
    employee2 = Employee("Gary Blatter","Male", 35, 1248559)

    worker1 = ProductionWorker("Lynne Blatter", "Female", 19.2, 100002, 1)
    worker2 = ProductionWorker("Macy Blatter", "Female", 11.2, 100004, 2)

#now this is how we will display employee details
    print ("Employee Details")
    print(f"Name: {employee1.get_name()}, Gender: {employee1.get_gender()}, Hourly Pay: ${employee1.get_hourly_pay_rate()}, Employee Number: {employee1.get_employee_number()}")
    print(f"Name: {employee2.get_name()}, Gender: {employee2.get_gender()}, Hourly Pay: ${employee2.get_hourly_pay_rate()}, Employee Number: {employee2.get_employee_number()}")

    print("Production Worker Details")
    print(f"Name: {worker1.get_name()}, Gender: {worker1.get_gender()}, Pay Rate: ${worker1.get_hourly_pay_rate()}, Employee Number: {worker1.get_employee_number()}, Shift: {worker1.get_shift_number()}")
    print(f"Name: {worker2.get_name()}, Gender: {worker2.get_gender()}, Pay Rate: ${worker2.get_hourly_pay_rate()}, Employee Number: {worker2.get_employee_number()}, Shift: {worker2.get_shift_number()}")

if __name__ == "__main__":
    main()