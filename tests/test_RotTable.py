import unittest
import os
import json
from dna.RotTable import RotTable

class TestRotTable(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Prepare a sample table for testing
        cls.sample_table = {
            "AA": [35.62, 7.2, -154, 0.06, 0.6, 0],
            "AC": [34.4, 1.1, 143, 1.3, 5, 0],
        }
        cls.sample_file = "test_table.json"
        with open(cls.sample_file, 'w') as f:
            json.dump(cls.sample_table, f)

    @classmethod
    def tearDownClass(cls):
        # Clean up the test file
        if os.path.exists(cls.sample_file):
            os.remove(cls.sample_file)

    def setUp(self):
        self.rot_table = RotTable(self.sample_file)

    def test_initialization(self):
        """Test if the table is loaded correctly."""
        self.assertEqual(self.rot_table.getTable(), self.sample_table)

    def test_setTwist(self):
        """Test setting the twist value."""
        self.rot_table.setTwist("AA", 40.0)
        self.assertEqual(self.rot_table.getTwist("AA"), 40.0)

    def test_setWedge(self):
        """Test setting the wedge value."""
        self.rot_table.setWedge("AC", 2.0)
        self.assertEqual(self.rot_table.getWedge("AC"), 2.0)

    def test_setDirection(self):
        """Test setting the direction value."""
        self.rot_table.setDirection("AA", -100.0)
        self.assertEqual(self.rot_table.getDirection("AA"), -100.0)

    def test_getTwist_invalid_key(self):
        """Test getting twist with an invalid dinucleotide."""
        with self.assertRaises(KeyError):
            self.rot_table.getTwist("ZZ")

    def test_getWedge_invalid_key(self):
        """Test getting wedge with an invalid dinucleotide."""
        with self.assertRaises(KeyError):
            self.rot_table.getWedge("ZZ")

    def test_getDirection_invalid_key(self):
        """Test getting direction with an invalid dinucleotide."""
        with self.assertRaises(KeyError):
            self.rot_table.getDirection("ZZ")

    def test_save(self):
        """Test saving the table to a file."""
        save_file = "saved_table.json"
        self.rot_table.setTwist("AA", 50.0)
        self.rot_table.save(save_file)

        # Verify the saved file
        with open(save_file, 'r') as f:
            saved_data = json.load(f)
        self.assertEqual(saved_data["AA"][0], 50.0)

        # Clean up
        if os.path.exists(save_file):
            os.remove(save_file)

if __name__ == "__main__":
    unittest.main()
