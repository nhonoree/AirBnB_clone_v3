import unittest
from models.place import Place
from datetime import datetime

class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_init(self):
        """Test initialization of Place."""
        obj = Place()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_ids, [])

    def test_save(self):
        """Test the save method of Place."""
        obj = Place()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of Place."""
        obj = Place()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'Place')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_attributes(self):
        """Test setting and getting attributes of Place."""
        obj = Place()
        obj.city_id = "123"
        obj.user_id = "456"
        obj.name = "Cozy Apartment"
        obj.description = "A cozy place in the city."
        obj.number_rooms = 2
        obj.number_bathrooms = 1
        obj.max_guest = 4
        obj.price_by_night = 100
        obj.latitude = 40.7128
        obj.longitude = -74.0060
        obj.amenity_ids = ["wifi", "pool"]

        self.assertEqual(obj.city_id, "123")
        self.assertEqual(obj.user_id, "456")
        self.assertEqual(obj.name, "Cozy Apartment")
        self.assertEqual(obj.description, "A cozy place in the city.")
        self.assertEqual(obj.number_rooms, 2)
        self.assertEqual(obj.number_bathrooms, 1)
        self.assertEqual(obj.max_guest, 4)
        self.assertEqual(obj.price_by_night, 100)
        self.assertEqual(obj.latitude, 40.7128)
        self.assertEqual(obj.longitude, -74.0060)
        self.assertEqual(obj.amenity_ids, ["wifi", "pool"])

if __name__ == "__main__":
    unittest.main()
