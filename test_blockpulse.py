# test_blockpulse.py
"""
Tests for BlockPulse module.
"""

import unittest
from blockpulse import BlockPulse

class TestBlockPulse(unittest.TestCase):
    """Test cases for BlockPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockPulse()
        self.assertIsInstance(instance, BlockPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
