#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


if __name__ == '__main__':
    a = list(map(int, input().split()))

    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    # Определить индексы минимального и максимального элементов.
    a_min = a_max = a[0]
    for i, item in enumerate(a):
        if abs(item) < abs(a_min):
            a_min = item
        if abs(item) >= abs(a_max):
            a_max = item

    print(a_max, a_min)
