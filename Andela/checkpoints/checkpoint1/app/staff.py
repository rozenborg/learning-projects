class Staff(Person):
	"""A person who is a staff member at Andela

	Attributes:
	department: a string representing the department the staff member belongs to
	
	"""
	def __init__(self, name, age, gender, role, department):

		# self.name = name
		# self.age = age
		# self.gender = gender
		self.role = role
		self.department = department