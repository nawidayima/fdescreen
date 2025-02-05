import unittest
from main import sort

class TestSort(unittest.TestCase):

    def test_standard(self):
        """Test package that's not bulky or heavy."""
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")

    def test_special_bulky_dimension(self):
        """Test package is bulky because of dimension >= 150."""
        self.assertEqual(sort(150, 40, 40, 10), "SPECIAL")

    def test_special_heavy(self):
        """Test package is heavy but not bulky."""
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")

    def test_rejected_bulky_and_heavy(self):
        """Test package is both bulky and heavy."""
        self.assertEqual(sort(150, 150, 150, 25), "REJECTED")

    def test_special_bulky_volume(self):
        """Test package is bulky by volume exactly 1,000,000 cm³."""
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

    def test_zero_dimensions(self):
        """Test package with zero dimensions."""
        self.assertEqual(sort(0, 0, 0, 10), "STANDARD")

    def test_negative_dimension(self):
        """Test package with negative dimension should raise ValueError."""
        with self.assertRaises(ValueError):
            sort(-1, 50, 50, 10)

    def test_negative_mass(self):
        """Test package with negative mass should raise ValueError."""
        with self.assertRaises(ValueError):
            sort(50, 50, 50, -5)

    def test_string_input(self):
        """Test package with string input should raise ValueError."""
        with self.assertRaises(ValueError):
            sort("50", 50, 50, 10)

    def test_none_input(self):
        """Test package with None input should raise ValueError."""
        with self.assertRaises(ValueError):
            sort(None, 50, 50, 10)

    def test_float_input(self):
        """Test package with float input is accepted."""
        self.assertEqual(sort(50.5, 50.5, 50.5, 10.5), "STANDARD")

    def test_boundary_mass(self):
        """Test package exactly at mass boundary (20kg)."""
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")
        self.assertEqual(sort(50, 50, 50, 19.99), "STANDARD")

    def test_boundary_dimension(self):
        """Test package exactly at dimension boundary (150cm)."""
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
        self.assertEqual(sort(149.99, 50, 50, 10), "STANDARD")

    def test_boundary_volume(self):
        """Test package exactly at volume boundary (1,000,000 cm³)."""
        # Exactly 1,000,000 cm³
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
        # Just under 1,000,000 cm³
        self.assertEqual(sort(99.99, 100, 100, 10), "STANDARD")

if __name__ == "__main__":
    unittest.main()
