#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：interview -> test_q2
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/7/10 23:29
@Desc   ：
"""
import pytest
import q2
import q1


def load_testcases(filename):
    with open(f'cases/{filename}', 'r') as rf:
        for i in rf:
            yield tuple(map(lambda x: x.strip(), i.split(',')))


@pytest.mark.parametrize('input, expired',
                         load_testcases('q1.txt'))
def test_q1(input, expired):
    value = q1.solve(input)
    assert value == expired, f'fail. expire: {expired}, actually: {value}'


@pytest.mark.parametrize('input, expired',
                         load_testcases('q2.txt'))
def test_q2(input, expired):
    value = q2.solve(input)
    assert value == expired, f'fail. expire: {expired}, actually: {value}'


if __name__ == '__main__':
    pytest.main(["-s", "test_q.py"])