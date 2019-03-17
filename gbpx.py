#!/usr/bin/env python

from urllib.request import urlopen, Request
import re


class Scrapper():

    def __init__(self,):
        self.headers = {'User-Agent': 'Wget/1.17.1 (linux-gnu)'}

    def get_version(self,):
        return '1.0'

    def get_html(self, url=""):
        request = Request(url=url, headers=self.headers)
        url_response = urlopen(request).read()
        return [url, url_response]

    def data_from_uk_investing_com(self, data):
        url = data[0]
        raw = data[1]
        name = re.findall("gbp-[A-Za-z]+", url)[0]
        sub_string = str(re.findall(b"last_last.*>", raw)[0])
        value = float(re.findall(r"\d+\.\d+", sub_string)[0])
        return {name: value}
