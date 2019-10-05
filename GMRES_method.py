# coding="utf-8"
import numpy as np


def Arnoldi(A, r0, m):
    """
    :param r0: 初始向量
    :param m: 空间维数
    :return: H: hessenberg矩阵 v_list:正交向量组
    """
    norm = lambda x: np.sqrt(np.sum(x**2))
    v_list = list()
    v_list.append(r0 / norm(r0))
    H = np.zeros(shape=(m+1, m))
    for i in range(1, m):
        w = np.dot(A, v_list[i-1])
        for j in range(1, i+1):
            H[j-1][i-1] = np.dot(w.T, v_list[j - 1])[0][0]
            w -= H[j-1][i-1] * v_list[j - 1]
        H[i][i-1] = norm(w)
        if abs(H[i][i-1]) < 1e-7:
            print("中断")
            break
        v_list.append(w/H[i][i-1])

    return H, v_list


def SolveLeastSquareProblem(H, beta, learning_rate):
    y = np.zeros((H.shape[1],1))
    for i in range(0, 100000):
        grad = H[:1, :] * beta * (-1) + np.dot(y.T, np.dot(H.T, H))
        y -= learning_rate * grad.T
        if np.average(np.abs(grad)) < 1e-2:
            print("itertime", i)
            break

    return y


def GMERS(A, b, m = 5):
    """
    :param A: 系数矩阵
    :param b: Ax = b的b
    :param m: 阶数
    :return:解
    实现的是算法3.8
    """
    # 首先执行分解
    r0 = b
    x0 = np.zeros((A.shape[1], 1))
    norm = lambda x: np.sqrt(np.sum(x ** 2))
    for i in range(0, 10):
        H, v_list = Arnoldi(A, r0 / norm(r0), m)
        # 此处，采用最速下降法解决问题
        ym = SolveLeastSquareProblem(H, norm(r0), 0.005)
        v_list = np.asarray([i.reshape(i.shape[0] * i.shape[1]) for i in v_list])
        xm = x0 + np.dot(v_list.T, ym)
        rm = b - np.dot(A, xm)
        r0 = rm
        x0 = xm

    return x0