class Room(object):
	"""A room...

	Attributes:
	max_occupants: the maximum number of people that can inhabit a room
	room_name: the name given to the room"""
	

	def __init__(self, room_name, max_occupants):
		"""Returns a room object where the maximum number of people that can inhabit the room at a given time is *max_occupants*"""
		
		self.room_name = room_name
		self.max_occupants = max_occupants
		self.occupants = []
		self.number_occupants = 0
		#consider adding occupant id

	def add_occupant(self, person_name):

		# self.occupants = []
		# self.number_occupants = 0
		self.occupants.append(person_name)
		self.number_occupants += 1

	def get_occupant_count(self):
		return self.number_occupants