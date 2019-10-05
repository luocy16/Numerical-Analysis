import numpy as np
from naive_method import *
from cg_method import *
import matplotlib.pyplot as plt
from GMRES_method import *
import time
import argparse
import naive_method


def hilbert_matrix_generator(n):
    hilbert_matrix = np.asarray([[1/(i+j+1) for i in range(n)] for j in range(n)])
    y = np.dot(hilbert_matrix, np.ones(shape=(n,1)))
    return (hilbert_matrix, y)


def get_efficiency(ans1, n):
    return np.sum(np.abs(ans1 - np.ones((n, 1)))) / n


def Parse():
    parser = argparse.ArgumentParser(description="Solve Linear Equation")
    parser.add_argument("--method", "-m", help="Solve algorithm : you could choose:  Gaussian, CG, GMRES, Cholesky")
    parser.add_argument("--is_normalization", "-is_norm",
                        help="is normalization? only valid for Gaussian Method and Cholesky", default="False")
    parser.add_argument("--ratio", "-r",
                        help="a coefficient for the normalization", default="1")
    method = parser.parse_args().method
    is_normalization = True if parser.parse_args().is_normalization == "True" else False
    ratio = float(parser.parse_args().ratio)
    print(method, is_normalization, ratio)
    return method, is_normalization, ratio


def load_method(method):
    if method == "Gaussian":
        return naive_method.gaussian_method
    if method == "Cholesky":
        return naive_method.cholesky_method
    if method == "CG":
        return cg_method
    if method == "GMRES":
        return GMERS
    print("找不到方法! method name error!")


def main():
    method, is_normalization, ratio = Parse()
    func = load_method(method)
    eff = []
    time_consume = []
    if method == "Cholesky":
        matrix = list(range(2, 10, 1))
    else:
        matrix = list(range(10, 500, 10))
    print("method:",method)

    for n in matrix:
        print("n:", n)
        begin = time.time()
        if method == "Gaussian" or method == "Cholesky":
            ans1 = func(*hilbert_matrix_generator(n), is_normalization = is_normalization, ratio=ratio)
        else:
            ans1 = func(*hilbert_matrix_generator(n))
        end = time.time()
        time_consume.append(end - begin)
        eff.append(get_efficiency(ans1, n) * 100)
        print("relative_error {0} % time consume {1} s".format(eff[-1], time_consume[-1]))

    print("----------------------")
    print(matrix, eff)
    print("----------------------")
    plt.plot(matrix, eff)
    plt.title(method + "_relative error")
    plt.xlabel("size of matrix")
    plt.ylabel("relative error of answer/ %")
    plt.show()
    plt.plot(matrix, time_consume)
    plt.title(method + "_time_consume")
    plt.xlabel("size of matrix")
    plt.ylabel("time_consume/ s")
    plt.show()



main()

