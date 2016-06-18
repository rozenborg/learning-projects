class Room(object):
	"""A room...

	Attributes:
	max_inhabitants: the maximum number of people that can inhabit a room
	room_name: the name given to the room"""

	def __init__(self, max_inhabitants):
		"""Returns a room object where the maximum number of people that can inhabit the room at a given time is *max_inhabitants*"""

		self.max_inhabitants = max_inhabitants
		self.name = room_name

	def designate_space(self):
		"""Designates the room for a specific purpose, such as office space or living quarters."""