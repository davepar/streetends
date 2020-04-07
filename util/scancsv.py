#!/usr/bin/env python
"""Utility script to scan a CSV file and report on the fields."""

import csv
import sys

def main():
    if len(sys.argv) != 2:
        print('%s csv_file' % sys.argv[0])
        exit()

    values_by_hdr = {}
    with open(sys.argv[1], newline='') as f:
        reader = csv.reader(f)
        hdr = next(reader)
        for line in reader:
            values = dict(zip(hdr, line))
            for key, value in values.items():
                if value:
                    cur_values = values_by_hdr.setdefault(key, set())
                    if len(cur_values) < 10:
                        cur_values.add(values[key])

    for key, value_set in values_by_hdr.items():
        sample = '(sample)' if len(value_set) == 10 else ''
        print('%s%s:' % (key, sample))
        for value in value_set:
            print('  %s' % value)

if __name__ == '__main__':
    main()
