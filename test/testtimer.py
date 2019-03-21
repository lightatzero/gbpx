#!/usr/bin/env python

import unittest
import gbpx
from datetime import datetime


class TimeTests(unittest.TestCase):

    def setUp(self):
        self.Scrapper = gbpx.Scrapper()

    def test_five_minute_interval(self):
        """
        Test that five_minute_interval is working
        """
        then = datetime.now()
        self.Scrapper.five_minute_interval()
        now = datetime.now()
        diff = now-then

        self.assertTrue(
                now.minute % 5 == 0,
                "Waited until time 5 minute interval, 0,5,10,15 minutesetc"
                )

        self.assertTrue(
                diff.total_seconds() <= 300,
                "Waited less than 5 minutes"
                )


if __name__ == '__main__':
    unittest.main()
