class Salary():
    def __init__(self,pay,bonus):
       self.pay= pay
       self.bonus = bonus


    def anuual_salary(self):
       return (self.pay*12)+ self.bonus


class Employee():
       def __init__(self,name ,age, sal):
              self.name = name
              self.age = age
              self.agg_salary = sal

       def Total_sal(self):
              return self.agg_salary.anuual_salary()

salary = Salary(100000,300000)
salary2 = Salary(40000,10000)

emp = Employee("budi", 27, salary2)
emp1 = Employee("sobri",26,salary)
print(f"total salary {emp.name} = {emp.Total_sal()}")
print(f"total salary {emp1.name} = {emp1.Total_sal()}")

   
