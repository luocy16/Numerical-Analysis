# coding="utf-8"
import numpy as np
import time

def gaussian_method(coeff_matrix, b, is_normalization = False, ratio = 1, is_constrain = True):
    """

    :param coeff_matrix:  系数矩阵:A
    :param b: Ax = b中的b
    :param is_normalization: 是否使用tikhonov正则化
    :param ratio: 正则化的比例
    :return: 返回Ax=b的解
    """
    row, column = coeff_matrix.shape

    if is_normalization:
        coeff_matrix, b = tikhonov_normalization(coeff_matrix, b, ratio, is_constrain = is_constrain)

    for i in range(column):
        # 对于给定的一列
        for j in range(i + 1, row):
            # (i, i) is the main elements
            ratio = coeff_matrix[j][i] / coeff_matrix[i][i]

            for k in range(i, column):
                coeff_matrix[j][k] -= \
                    ratio * coeff_matrix[i][k]

            # 改变系数矩阵
            b[j] -= ratio * b[i]


    # 自底向下求解
    answer = np.zeros(shape=(row, 1))

    for i in range(row - 1, - 1, -1):
        value = np.dot(coeff_matrix[i : i+1, i:row], answer[i : row, :])[0][0]
        answer[i] =(b[i] - value) / coeff_matrix[i][i]


    return answer


def cholesky_method(coeff_matrix, b,  is_normalization = False, ratio = 1,  is_constrain = True):
    """
    :param coeff_matrix:  系数矩阵:A
    :param b: Ax = b中的b
    :param is_normalization: 是否使用tikhonov正则化
    :param ratio: 正则化的比例
    :return: 返回Ax=b的解
    """
    row, column = coeff_matrix.shape

    if is_normalization:
        coeff_matrix, b = tikhonov_normalization(coeff_matrix, b, ratio, is_constrain = is_constrain)

    # 检验矩阵是不是正定
    for i in range(row):
        assert np.linalg.det(coeff_matrix[: i, :i]) > 0

    # 矩阵分解
    L = np.zeros((row, column))
    for j in range(row):
        L[j, j] = np.sqrt(coeff_matrix[j, j] - np.sum([L[j, k] ** 2 for k in range(0, j)]))
        for i in range(j + 1, column):
            L[i, j] = (coeff_matrix[i, j] - np.sum([L[j, k] * L[i, k] for k in range(0, j)])) / L[j, j]

    # 逐次求解两个问题
    y = np.zeros(row)
    x = np.zeros(row)

    for i in range(row):
        y[i] = (b[i] - np.sum([L[i, k] * y[k] for k in range(0, i)])) / L[i, i]

    for i in range(row - 1, -1, -1):
        x[i] = (y[i] - np.sum([L[k, i] * x[k] for k in range(i+1, row)])) / L[i, i]


    return x


def tikhonov_normalization(coeff_matrix, b, ratio, is_constrain = False):
    """返回coeff_matrix * x = b 的等价问题"""
    eig_value_list = np.linalg.eigvals(coeff_matrix) # 矩阵的特征值序列
    alpha = ratio * max(abs(eig_value_list)) * min(abs(eig_value_list))
    if is_constrain:
        alpha = min(alpha, 1e-5 * np.min(coeff_matrix))

    return alpha * np.eye(*coeff_matrix.shape) + np.dot(coeff_matrix.T, coeff_matrix), np.dot(coeff_matrix.T, b)