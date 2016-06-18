import unittest
from app.office import Office
import pdb

class RoomTest(unittest.TestCase):

	def test_add_occupant(self):
		# pdb.set_trace()
		room = Office("Moon", 6)
		person = Fellow("Jerk", 100, "Male", "Y", "D1")
		room.add_occupant(person)
		self.assertEqual(1, room.get_occupant_count())

		person = Staff("Hero", 12, "Female", "Training Warrior", "Training Department")
		room.add_occupant(person)
		self.assertEqual(2, room.get_occupant_count())

if __name__ == '__main__':
	unittest.main()
