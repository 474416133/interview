#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：interview -> q2
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/7/10 21:29
@Desc   ：

Instead of removing the consecutively identical characters, replace them with a
single character that comes before it alphabetically.
ccc -> b
bbb -> a
Input: abcccbad
Output:
-> abbbad, ccc is replaced by b
-> aaad, bbb is replaced by a
-> d

"""

def upgrade(c: 'Char') -> 'Char':
    i_value = ord(c) - 1
    if 64 < i_value < 91 or 96 < i_value < 123:
        return chr(i_value)
    return ''


def solve(value: str) -> str:
    size = len(value)
    if size < 3:
        return value

    start = 0
    for i in range(0, size-1):
        if value[i] == value[i+1]:
            if i == size - 2 and start < i:
                value = value[: start] + upgrade(value[start])
                value = solve(value)
                break
            continue
        elif i + 1 - start > 2:
            value = value[: start] + upgrade(value[start]) + value[i+1: size]
            value = solve(value)
            break
        else:
            start = i + 1

    return value


if __name__ == '__main__':
    assert solve('bbb') == 'a', 'fail'

