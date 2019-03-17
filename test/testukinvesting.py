#!/usr/bin/env python

import unittest
import gbpx


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.Scrapper = gbpx.Scrapper()
        self.urls = [
                    "https://uk.investing.com/currencies/gbp-eur",
                    "https://uk.investing.com/currencies/gbp-mxn",
                    "https://uk.investing.com/currencies/gbp-usd",
                    "https://uk.investing.com/currencies/gbp-chf",
                    "https://uk.investing.com/currencies/gbp-aud",
                    "https://uk.investing.com/currencies/gbp-cad",
                    "https://uk.investing.com/currencies/gbp-nzd",
                    "https://uk.investing.com/currencies/gbp-cny",
                    "https://uk.investing.com/currencies/gbp-inr",
                    "https://uk.investing.com/currencies/gbp-idr",
                    "https://uk.investing.com/currencies/gbp-brl",
                    "https://uk.investing.com/currencies/gbp-pkr",
                    "https://uk.investing.com/currencies/gbp-ngn",
                    "https://uk.investing.com/currencies/gbp-bdt",
                    "https://uk.investing.com/currencies/gbp-rub",
                    ]

    def test_uk_investing_com_get_html(self):
        """
        Test we parse data from real website
        """
        values = {}
        for url in self.urls:
            data = self.Scrapper.get_html(url)
            values.update(self.Scrapper.data_from_uk_investing_com(data))
        for name, value in values.items():
            self.assertTrue(isinstance(name, str), "Name is valid")
            self.assertTrue(isinstance(value, float), "Value is valid")


if __name__ == '__main__':
    unittest.main()
