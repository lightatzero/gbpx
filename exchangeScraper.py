#!/usr/bin/env python 

from time import sleep
from pathlib import Path
from threading import Thread
import datetime
import subprocess
import re

gbpToCurrency = [
"eur",
"mxn",
"usd",
"chf",
"aud",
"cad",
"nzd",
"cny",
"inr",
"idr",
"brl",
"pkr",
"ngn",
"bdt",
"rub",
]

def getVersion():
    return '1.0'

def getTimeStampString():
    ret =   datetime.datetime.now(\
            datetime.timezone.utc).strftime(\
            "%Z %Y-%m-%d %H:%M:%S")
    return ret

def writeCsv(exchange,value):
    my_filename = "gbp-"+exchange+".csv"
    my_file = Path(my_filename)
    my_data = str(getTimeStampString()) + ','+str(value) + '\n'
    if my_file.is_file():
        csv_file = open(my_filename,"a")
        csv_file.write(my_data)
        csv_file.close()
    else:
        csv_file = open(my_filename,"w")
        csv_file.write("time,value\n")
        csv_file.write(my_data)
        csv_file.close()

def getValueFromInvestingDotCom(exchange):
    subprocess.check_output([
            "wget",
            "-q",
            "https://uk.investing.com/currencies/gbp-"+exchange,
            "-O",
            "data/gbp-"+exchange])
    ret = str(subprocess.check_output([
            "grep",
            "last_last",
            "data/gbp-"+exchange]))
    ret = ret.split('last_last')[-1].replace(",","")
    ret = float(re.findall("\d+\.\d+",ret)[0])
    writeCsv(exchange,ret)

if __name__ == "__main__":
    while True:
        threads = []
        for exchange in gbpToCurrency:
            t = Thread(target=getValueFromInvestingDotCom,args=(exchange,))
            threads.append(t)
        for x in threads:
            x.start()
        for x in threads:
            x.join()
        sleep(60*5)
