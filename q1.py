#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：interview -> q1
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/7/10 21:04
@Desc   ：

For a given string that only contains alphabet characters a-z, if 3 or more consecutive
characters are identical, remove them from the string. Repeat this process until
there is no more than 3 identical characters sitting besides each other.
Example:
Input: aabcccbbad
Output:
-> aabbbad
-> aaad
-> d
"""
import re

re_c = re.compile(r'(\w)\1{2,}')


def solve(value: str) -> str:
    ret = re_c.sub('', value, 1)
    if ret != value:
        return solve(ret)
    return ret



if __name__ == '__main__':
    assert solve('aabcccbbad') == 'd', 'fail'