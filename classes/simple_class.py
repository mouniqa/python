class Employee:

	def __init__(self,name,company,salary):
		self.name = name
		self.company = company
		self.salary = salary
		self.email = name+'@'+company

	def display(self):
		print('Name:',self.name)
		print('Company:',self.company)
		print('Salary:',self.salary)
		print('Email:',self.email)


e1 = Employee('Jagadeesh Varma','google.com','$200k per annum')
e2 = Employee('Mounika Jagadeesh','mahitha.org','$250k per annum')

print()
e1.display()
print()
e2.display()
