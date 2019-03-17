#!/usr/bin/env python

import unittest
import http.server
import socketserver
import threading
import gbpx


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


if __name__ == '__main__':
    unittest.main()
