class Employee:
    
    def __init__(self):
        self.id = 1234
        self.salary = 50000
        self.designation = 'Data Scientist'

    def travel(self, destination):
        print(f'Travelling to {destination}')


emp = Employee()


print(emp.designation)
print(emp.salary)

emp.travel('Gujrat')