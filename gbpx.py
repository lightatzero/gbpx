#!/usr/bin/env python

from urllib.request import urlopen, Request
from datetime import datetime, timezone
from time import time, sleep
import re
import sqlite3


class Scrapper():

    def __init__(self,):
        self.headers = {'User-Agent': 'Wget/1.17.1 (linux-gnu)'}
        self.db_name = 'database.db'
        self.table_name = 'ukinvesting'

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

    def get_timestamp_rfc_3339(self,):
        return datetime.now(timezone.utc).isoformat()

    def five_minute_interval(self,):
        sleep(300 - (time() % 300))
        return True

    def create_table(self,):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute(
                '''CREATE TABLE {}
                (datetime text,
                symbol text,
                value real)'''.format(self.table_name))
        conn.commit()
        conn.close()
        return True

    def remove_table(self,):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''DROP TABLE {}'''.format(self.table_name))
        conn.commit()
        conn.close()
        return True

    def put_data_in_table(self, datetime, symbol, value):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute(
                '''INSERT INTO {}
                VALUES (?,?,?)'''.format(self.table_name),
                (datetime, symbol, value, ))
        conn.commit()
        conn.close()
        return True

    def check_table(self,):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        fetched = c.execute('''SELECT name
                FROM sqlite_master
                WHERE type='table'
                AND name='{}';'''.format((self.table_name))).fetchall()
        if fetched:
            table_there = True
        else:
            table_there = False
        conn.commit()
        conn.close()
        return table_there
