class Employee:
    def _init_(self, name, punctuality, task_completion, teamwork, innovation):
        self.name = name
        self.punctuality = punctuality      # 1 to 5
        self.task_completion = task_completion  # 1 to 5
        self.teamwork = teamwork            # 1 to 5
        self.innovation = innovation        # 1 to 5
        self.rating = None
        self.remark = None
    def evaluate(self):
        avg_score = (self.punctuality + self.task_completion + self.teamwork + self.innovation) / 4
        if avg_score >= 4.5:
            self.rating = "Excellent"
            self.remark = "Promotion Recommended"
        elif avg_score >= 3.5:
            self.rating = "Good"
            self.remark = "Keep up the good work"
        elif avg_score >= 2.5:
            self.rating = "Average"
            self.remark = "Needs Improvement"
        else:
            self.rating = "Poor"
            self.remark = "Performance Review Required"
    def display_info(self):
        print("\nEmployee Name:", self.name)
        print(f"Punctuality: {self.punctuality}/5")
        print(f"Task Completion: {self.task_completion}/5")
        print(f"Teamwork: {self.teamwork}/5")
        print(f"Innovation: {self.innovation}/5")
        print("Overall Rating:", self.rating)
        print("Manager's Remark:", self.remark)
class PerformanceSystem:
    def _init_(self):
        self.employees = []
    def add_employee(self, employee):
        employee.evaluate()
        self.employees.append(employee)
        print("Employee evaluated and added successfully.")
    def display_all(self):
        if not self.employees:
            print("No employee records found.")
        for emp in self.employees:
            emp.display_info()
def main():
    system = PerformanceSystem()
    while True:
        print("\n==== Employee Performance Evaluation System ====")
        print("1. Add New Employee Evaluation")
        print("2. Display All Employee Evaluations")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter employee name: ")
            
            punctuality = int(input("Punctuality (1-5): "))
            task_completion = int(input("Task Completion (1-5): "))
            teamwork = int(input("Teamwork (1-5): "))
            innovation = int(input("Innovation (1-5): "))
            emp = Employee(name, punctuality, task_completion, teamwork, innovation)
            system.add_employee(emp)
            
        elif choice == '2':
            system.display_all()
        elif choice == '3':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()