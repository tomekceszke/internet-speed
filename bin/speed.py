#!/usr/bin/python
import os
import subprocess
import re
import rrdtool
import sys

import thingspeak

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from conf.settings import *
from conf.private_settings import *


__author__ = 'Tomasz Ceszke'


def run_test():
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    # proc.terminate()
    if err:
        sys.stderr.write("Error occured: " + err)
        sys.exit(1)
        # print("raw output:", out)
    return out


def parse_output(output):
    numbers = re.findall(r'\b\d+.\d+\b', output)

    if not numbers:
        sys.stderr.write("Can't parse raw output: " + output)
        sys.exit(0)

    numbers.pop(0)
    # print("numbers", numbers)
    return numbers


def update_rrd_db(download, upload):
    data = 'N:' + str(download) + ':' + str(upload)
    # print(data)
    rrdtool.update(db_path, data)


def update_thingspeak_db(download, upload):
    ch = thingspeak.Channel(thingspeak_channel)
    ch.update({'api_key': thingspeak_write_api_key, 'field1': download, 'field2': upload})


def main():
    raw = run_test()
    numbers = parse_output(raw)
    # print("numbers", numbers)
    update_thingspeak_db(numbers[0], numbers[1])


if __name__ == '__main__':
    main()
