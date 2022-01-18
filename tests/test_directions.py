from context import src

from src import directions
import unittest, os

path = os.environ.get('PARENT_DIR')

class DirectionsTestSuite(unittest.TestCase):

    def test_json(self):
        file = open("json_example.json", "r")
        controller = directions.DirectionController("Disneyland", "Hollywood")
        self.assertIsNotNone(str(controller.getDirections()))


if __name__ == '__main__':
    unittest.main()