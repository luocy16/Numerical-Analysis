import numpy as np


def cg_method(coeff_list, b):
    """
    :param coeff_list: 参数矩阵
    :param b: Ax = b中的b
    :return:
    """
    x = np.zeros((coeff_list.shape[0],1))
    r = b - np.dot(coeff_list, x)
    p = r.copy()
    # 至多迭代一万步
    for k in range(0, 10000):
        alpha_k = (np.dot(r.T, r) / np.dot(np.dot(p.T, coeff_list), p))[0][0]
        x += alpha_k * p
        r_next = r - np.dot(alpha_k * coeff_list, p)
        beta = (np.dot(r_next.T, r_next) / np.dot(r.T, r))[0][0]
        r = r_next
        p = r + beta * p
        # 设置退出迭代的条件
        if np.sum(np.abs(r)) < 1e-7:
            break

    print("iter_step", k)
    return x
