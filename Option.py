from PyQt5.QtWidgets import QMessageBox
import scipy.stats as sps
import numpy as np


class Option:

    # european 为 欧式期权 (False 为欧式期权)
    # kind 看涨或看跌（Put 为 -1 , Call 为 1）
    # s0 标的资产现价
    # k 期权执行价
    # t 期权到期时间 - 现在时间,以天计
    # r 适用的无风险利率，连续复利
    # sigma 适用的波动率，
    # dv 股利信息，连续复利
    def __init__(self, european, kind, s0, k, t, r, sigma, page):
        self.european = european
        self.kind = kind
        self.s0 = s0
        self.k = k
        self.t = t
        self.sigma = sigma
        self.r = r
        self.bsmprice = None

        self.page = page

    # B-S-M 计算价格方法
    def BSM(self):
        if self.european:
            d1 = (np.log(self.s0 / self.k) + (
                    self.r + .5 * self.sigma ** 2) * self.t) / self.sigma / np.sqrt(
                self.t)
            d2 = d1 - self.sigma * np.sqrt(self.t)
            self.bsmprice = self.kind * self.s0 * sps.norm.cdf(
                self.kind * d1) - self.kind * self.k * np.exp(-self.r * self.t) * sps.norm.cdf(self.kind * d2)
        else:
            QMessageBox.about(self.page.widget,
                              "提示",
                              "美式看跌期权不适合这种计算方法！")
    
    # 希腊字母计算
    def Greek(self):
        d1 = (np.log(self.s0 / self.k) + (
                    self.r + .5 * self.sigma ** 2) * self.t) / self.sigma / np.sqrt(
                self.t)
        d2 = d1 - self.sigma * np.sqrt(self.t)
        if self.kind == 1:
            self.delta = sps.norm.cdf(d1)
        else:
            self.delta = sps.norm.cdf(d1) - 1
        self.theta = -(self.s0 * self.sigma * np.exp(- .5 * d1 ** 2)) / (2 * np.sqrt(2 * np.pi * self.t)) - self.kind * self.r * self.k * np.exp(-self.r * self.t) * sps.norm.cdf(self.kind * d2)
        self.gamma = np.exp(- .5 * d1 ** 2) / ( self.s0 * self.sigma * np.sqrt(2 * np.pi * self.t))
        self.vega = self.s0 * np.sqrt(self.t) * np.exp(- .5 * d1 ** 2) / np.sqrt(2 * np.pi)
        self.rho = self.kind * self.k * self.t * np.exp(-self.r * self.t) * sps.norm.cdf(self.kind * d2)

   