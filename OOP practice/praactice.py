class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

class Employee:
    def __init__(self,employee_id,department,name,age,gender):
        super().__init__(name,age,gender) 
        self.employee_id = employee_id
        self.department = department
        self.tasks = []

    def assign_task(self,task):
        if task not in self.tasks:
            self.tasks.append(task)
        else:
            print(f"Task '{task}' is already assigned to {self.name} .")

    def display_employee_info(self):
        print(f"employee name: {self.name}")
        print(f"department {self.department}")    
        print("assigned tasks: ")
        for task in self.tasks:
            print(f"- {task}")     

#creating employee objests
Employee1 = Employee("E001", "finance", "Annet", 23 , "female")
Employee2 = Employee("E002", "Procurement", "John", 28, "Male")   

#assigning tasks
Employee1.assign_task("stock checking")
Employee1.assign_task("salary payment")
Employee1.assign_task("book checking")

Employee2.assign_task("buy cars")
Employee2.assign_task("buy furniture")
Employee2.assign_task("buy laptops")

#displaying info
Employee2.display_employee_info
Employee1.display_employee_info
        
