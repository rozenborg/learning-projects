from person import Person

class Fellow(Person):
	"""A Fellow at Andela

	Attributes:
	level: a string describing which stage of the Fellowship they are in
	wants_residence: a string (y/n) that represents whether or not the Fellow would like to live in Andela housing
	"""

	def __init__(self, wants_residence, level):

		# self.person_name = person_name
		# self.age = age
		# self.gender = gender
		self.wants_residence = wants_residence
		self.level = level