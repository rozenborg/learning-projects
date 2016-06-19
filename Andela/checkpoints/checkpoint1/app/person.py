class Person(object):
	"""A human being who can occupy space in a room

	Attributes:
	name: a string representing the person's name
	start_date: a DATATYPE? representing the date the person began working at Andela
	role: a string representing the person's job at Andela
	"""
	def __init__(self, person_name, age, gender):

		self.person_name = person_name
		self.age = age
		self.gender = gender