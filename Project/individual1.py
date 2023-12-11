#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from functools import reduce


if __name__ == '__main__':
    a = list(map(int, input().split()))

    if len(a) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    m = reduce(lambda x, y: x * y, [i for i in a if i > 0])
    print(m)
