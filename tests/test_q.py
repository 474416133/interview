#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：interview -> test_q2
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/7/10 23:29
@Desc   ：
"""
import os
import pytest
import q2
import q1

current_dir = os.path.dirname(__file__)

def load_testcases(filename):
    full_file_name = os.sep.join([current_dir, 'cases', filename])
    with open(full_file_name, 'r') as rf:
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