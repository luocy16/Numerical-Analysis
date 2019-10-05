# Numerical-Analysis
## 清华大学数值分析上机作业一 求解线性方程组

分别实现了Gauss消元法，Cheskoley分解法，共轭梯度法和GMRES算法

切换到项目根目录后，
请在命令行执行： python main.py -m [算法名称]  -is_norm [True or False] -r  [数值] 
 
-m / --method: 表示使用什么算法, 
为必选参数 可选的是：Gaussian, CG,GMRES, Cholesky 如果填写错误，程序会报告"找不到方法! method name error!" 
-is_norm: 是否进行正则化，对于 Gauss, Cholesky 必填 
-r: 吉洪诺夫正则化中的参数，对于 Gauss, Cholesky 必填， 建议填写 10000000 / 1e7 
 
 
命令举例： python main.py -m Cholesky -is_norm True -r 1e7   // 表示，用 Cholesky 分解，并作正则化 
