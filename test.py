import pytest
import naive_method
import numpy as np
from cg_method import *


def test_0():
    while True:
        A = np.asarray([[3,1],[1,2]])
        if np.linalg.det(A) > 1:
            break

    b = np.asarray([[5],[5]])
    print("ans", np.linalg.solve(A, b))
    assert np.sum(np.abs(np.linalg.solve(A, b) - cg_method(A, b))) < 1e-5

def test_1():
    while True:
        A = np.random.uniform(0, 5, (3,3))
        if np.linalg.det(A) > 1:
            break

    b = np.random.uniform(0, 5, (3,1))
    print("ans", np.linalg.solve(A, b))

    assert np.sum(np.abs(np.linalg.solve(A, b)-cg_method(A, b))) < 1e-5

def test_2():
    while True:
        A = np.random.uniform(0, 10, (10 , 10))
        if np.linalg.det(A) > 1:
            break

    b = np.random.uniform(0, 5, (10 ,1))
    assert np.sum(np.abs(np.linalg.solve(A, b)-cg_method(A, b))) < 1e-5


def test_3():
    while True:
        A = np.random.uniform(0, 100, (100 , 100))
        if np.linalg.det(A) > 1:
            break

    b = np.random.uniform(0, 5, (100 ,1))
    assert np.sum(np.abs(np.linalg.solve(A, b) - cg_method(A, b))) < 1e-5