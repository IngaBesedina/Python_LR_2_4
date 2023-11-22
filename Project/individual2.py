#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(int, input().split()))

    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    s = 0
    for i in a:
        if i > 0:
            s += i

    a_min = a_max = abs(a[0])
    i_min = i_max = 0
    for i, item in enumerate(a):
        if abs(item) < a_min:
            i_min, a_min = i, abs(item)
        if abs(item) >= a_max:
            i_max, a_max = i, abs(item)

    if i_min > i_max:
        i_min, i_max = i_max, i_min

    m = 1
    for item in a[i_min+1:i_max]:
        m *= item

    print(f"Сумма положительных элементов списка: {s}")
    print(
        f"Произведение элементов списка, расположенных между максимальным и минимальным элементами: {m}")

    a.sort()
    print(f"Элементы списка по возрастанию: {a}")
