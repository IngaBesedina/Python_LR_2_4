#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from functools import reduce

if __name__ == '__main__':
    a = list(map(int, input().split()))

    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    s = sum([i for i in a if i > 0])

    a_min, i_min = min((abs(item), i) for i, item in enumerate(a))
    a_max, i_max = max((abs(item), i) for i, item in enumerate(a))

    if i_min > i_max:
        i_min, i_max = i_max, i_min

    m = reduce(lambda x, y: x * y, [i for i in a[i_min + 1:i_max]])

    print(f"Сумма положительных элементов списка: {s}")
    print("Произведение элементов списка, расположенных между"
          f"максимальным и минимальным элементами: {m}")

    a.sort()
    print(f"Элементы списка по возрастанию: {a}")
