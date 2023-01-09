from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QMessageBox, QFormLayout
from PyQt5.QtCore import QDate
import scipy.stats as sps
import numpy as np

def ImpVolUI(page):

    ########################################################################################
    # 隐含波动率
    ########################################################################################

    # 计算方法
    page.impVol.label_model = QLabel()
    # page.impVol.label_model.setFont(page.font_content)
    page.impVol.label_model.setText("计算方法")
    page.impVol.combo_model = QComboBox(page.impVol)
    page.impVol.combo_model.addItem("二分查找法")
    page.impVol.formLayout1.setWidget(0, QFormLayout.LabelRole, page.impVol.label_model)
    page.impVol.formLayout1.setWidget(0, QFormLayout.FieldRole, page.impVol.combo_model)

    # sigma_min
    page.impVol.label_sigma_min = QLabel()
    # page.impVol.label_sigma_min.setFont(page.font_content)
    page.impVol.label_sigma_min.setText("sigma_min")
    page.impVol.sigma_min = QLineEdit(page.impVol)
    page.impVol.sigma_min.setText("0.01")
    page.impVol.formLayout2.setWidget(0, QFormLayout.LabelRole, page.impVol.label_sigma_min)
    page.impVol.formLayout2.setWidget(0, QFormLayout.FieldRole, page.impVol.sigma_min)

    # sigma_max
    page.impVol.label_sigma_max = QLabel()
    # page.impVol.label_sigma_max.setFont(page.font_content)
    page.impVol.label_sigma_max.setText("sigma_max")
    page.impVol.sigma_max = QLineEdit(page.impVol)
    page.impVol.sigma_max.setText("1.00")
    page.impVol.formLayout3.setWidget(0, QFormLayout.LabelRole, page.impVol.label_sigma_max)
    page.impVol.formLayout3.setWidget(0, QFormLayout.FieldRole, page.impVol.sigma_max)

    page.impVol.gridLayout.addLayout(page.impVol.formLayout1, 0, 0, 1, 2)
    page.impVol.gridLayout.addLayout(page.impVol.formLayout2, 0, 2, 1, 2)
    page.impVol.gridLayout.addLayout(page.impVol.formLayout3, 0, 4, 1, 2)

    # 期权现价
    page.impVol.label_v = QLabel()
    # page.impVol.label_v.setFont(page.font_content)
    page.impVol.label_v.setText("期权现价")
    page.impVol.v = QLineEdit(page.impVol)
    page.impVol.v.setText("1")
    page.impVol.formLayout.setWidget(0, QFormLayout.LabelRole, page.impVol.label_v)
    page.impVol.formLayout.setWidget(0, QFormLayout.FieldRole, page.impVol.v)

    # 隐含波动率 (%)
    page.impVol.label_impVol = QLabel()
    # page.impVol.label_sigma_max.setFont(page.font_content)
    page.impVol.label_impVol.setText("隐含波动率 (%)")
    page.impVol.impVol = QLineEdit(page.impVol)
    page.impVol.impVol.setReadOnly(True)
    page.impVol.formLayout.setWidget(1, QFormLayout.LabelRole, page.impVol.label_impVol)
    page.impVol.formLayout.setWidget(1, QFormLayout.FieldRole, page.impVol.impVol)

    page.impVol.gridLayout.addLayout(page.impVol.formLayout, 1, 0, 2, 6)

def BSM(european, kind, s0, k, t, r, sigma):
    if european:
        d1 = (np.log(s0 / k) + (r + .5 * sigma ** 2) * t) / sigma / np.sqrt(t)
        d2 = d1 - sigma * np.sqrt(t)
        return kind * s0 * sps.norm.cdf(kind * d1) - kind * k * np.exp(-r * t) * sps.norm.cdf(kind * d2)
        
def CalImpVol(european, kind, s0, k, t, r, sigma_min, sigma_max, v, page):
    sigma_mid = (sigma_min + sigma_max) / 2
    min = BSM(european, kind, s0, k, t, r, sigma_min)
    max = BSM(european, kind, s0, k, t, r, sigma_max)
    mid = BSM(european, kind, s0, k, t, r, sigma_mid)
    diff = v - mid
    if v < min:
        QMessageBox.about(page.widget,
                "提示",
                "sigma_min过大\n请重新输入更小的sigma_min！")
    elif v > max:
        QMessageBox.about(page.widget,
                "提示",
                "sigma_max过小\n请重新输入更大的sigma_max！")
    else:
        while abs(diff) > 0.000001:
            sigma_mid = (sigma_min + sigma_max) / 2
            diff = v - BSM(european, kind, s0, k, t, r, sigma_mid)
            if diff > 0:
                sigma_min = sigma_mid
            else:
                sigma_max = sigma_mid        
    page.mainwindow.page_input.impVol.impVol.setText(str(sigma_mid * 100))