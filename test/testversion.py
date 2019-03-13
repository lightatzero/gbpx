#!/usr/bin/env python 

import unittest
import exchangeScraper

class UnitTests(unittest.TestCase):

    def test_version(self):
        """
        Test that the version is correct
        """
        self.assertEqual(   exchangeScraper.getVersion(),
                            '1.0', 
                            "Versions should match")

if __name__ == '__main__':
    unittest.main()
