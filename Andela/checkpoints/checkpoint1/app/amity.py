class Amity(object):
	"""The  Andela live work space office

	Attributes:
	small_rooms: An integer with the number of rooms that have a capacity of 4 or 5 inhabitants
	big_rooms: An integer with the number of rooms that have a maximum capacity of 6 or greater"""


	def __init__(self, small_rooms, big_rooms):
		"""Return an Amity object where number of rooms that can hold a 4 or 5 people is *small_rooms*
		and number of rooms that can hold 6 or more people is *big_rooms*"""

		self.small_rooms = small_rooms
		self.big_rooms = big_rooms