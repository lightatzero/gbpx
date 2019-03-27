#!/usr/bin/env python

import unittest
import http.server
import socketserver
import threading
import gbpx
from datetime import datetime


def start_test_server():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    Handler.log_message = lambda *args: None
    server = socketserver.TCPServer(
            ("", PORT), Handler, bind_and_activate=False
            )
    server.allow_reuse_address = True
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server.server_bind()
    server.server_activate()
    server_thread.start()
    return server


def stop_test_server(server):
    server.shutdown()
    server.server_close()


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.Scrapper = gbpx.Scrapper()

    def test_version(self):
        """
        Test that the version is correct
        """
        self.assertEqual(
                self.Scrapper.get_version(),
                '1.0',
                "Versions should match"
                )

    def test_get_html(self):
        """
        Test that the get_html function is working
        """
        f = open("test/index.html", "rb")
        expectedhtml = f.read()
        f.close()
        server = start_test_server()
        url = "http://localhost:8000/test/"
        data = self.Scrapper.get_html(url)
        self.assertEqual(
                data[1],
                expectedhtml,
                "Did not get local html")
        stop_test_server(server)

    def test_data_from_uk_investing_com(self):
        """
        Test that the data_from_uk_investing_com function is working
        """
        server = start_test_server()
        url = "http://localhost:8000/test/uk.investing.com.gbp-usd.html"
        data = self.Scrapper.get_html(url)
        values = self.Scrapper.data_from_uk_investing_com(data)
        self.assertEqual(
                values['gbp-usd'],
                1.3299,
                "Did not parse data properly")
        stop_test_server(server)

    def test_data_from_uk_investing_com_parser_fix(self):
        """
        Test that the data_from_uk_investing_com function is working
        """
        server = start_test_server()
        url = "http://localhost:8000/test/uk.investing.com.gbp-idr.html"
        data = self.Scrapper.get_html(url)
        values = self.Scrapper.data_from_uk_investing_com(data)
        self.assertEqual(
                values['gbp-idr'],
                18716.4,
                "Did not parse data properly")
        stop_test_server(server)

    def test_get_timestamp_rfc_3339(self):
        """
        Test that the get_timestamp_rfc_3339 function is working
        """
        then_string = self.Scrapper.get_timestamp_rfc_3339()
        then = datetime.strptime(
                then_string.split("+")[0],
                '%Y-%m-%dT%H:%M:%S.%f')
        now = datetime.now()
        difference = now - then
        self.assertTrue(
                difference.total_seconds() <= 5.00,
                "Did not get time properly")

    def test_tables(self):
        """
        Test that the sql tables are function is working
        """
        self.Scrapper.table_name = "test_table"
        self.assertTrue(
                self.Scrapper.create_table(),
                "Table not created properly"
                )
        self.assertTrue(
                self.Scrapper.check_table(),
                "Table not checked properly."
                )
        self.assertTrue(
                self.Scrapper.put_data_in_table("x", "y", 1.0),
                "Table not populated properly."
                )
        self.assertTrue(
                self.Scrapper.remove_table(),
                "Table not removed properly."
                )
        self.assertFalse(
                self.Scrapper.check_table(),
                "Table not checked properly."
                )


if __name__ == '__main__':
    unittest.main()
