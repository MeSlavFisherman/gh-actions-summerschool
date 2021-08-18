#!/usr/bin/python
# -*- coding: utf-8 -*-
import simple


def test_calc():
    total = simple.calc(4, 5)
    assert total == 9


def test_mult():
    result = simple.mult(10, 3)
    assert result == 30
