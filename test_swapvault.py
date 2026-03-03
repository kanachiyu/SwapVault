# test_swapvault.py
"""
Tests for SwapVault module.
"""

import unittest
from swapvault import SwapVault

class TestSwapVault(unittest.TestCase):
    """Test cases for SwapVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SwapVault()
        self.assertIsInstance(instance, SwapVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SwapVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
