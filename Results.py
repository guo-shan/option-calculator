from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QDateEdit, QFormLayout
from PyQt5.QtCore import QDate


def ResultsUI(page):
    
    ########################################################################################
    # 计算结果
    ########################################################################################
    
    # 定价模型
    page.results.label_model = QLabel()
    # page.results.label_model.setFont(page.font_content)
    page.results.label_model.setText("定价模型 ")
    page.results.combo_model = QComboBox(page.results)
    page.results.combo_model.addItem("Black Scholes Merton定价模型（BSM定价模型）")
    page.results.formLayout.setWidget(0, QFormLayout.LabelRole, page.results.label_model)
    page.results.formLayout.setWidget(0, QFormLayout.FieldRole, page.results.combo_model)

    # 理论价格
    page.results.label_price = QLabel()
    # page.results.label_price.setFont(page.font_content)
    page.results.label_price.setText("理论价格")
    page.results.price = QLineEdit(page.results)
    page.results.price.setReadOnly(True)
    page.results.formLayout.setWidget(1, QFormLayout.LabelRole, page.results.label_price)
    page.results.formLayout.setWidget(1, QFormLayout.FieldRole, page.results.price)

    # delta
    page.results.label_delta = QLabel()
    # page.results.label_delta.setFont(page.font_content)
    page.results.label_delta.setText("delta")
    page.results.delta = QLineEdit(page.results)
    page.results.delta.setReadOnly(True)
    page.results.formLayout.setWidget(2, QFormLayout.LabelRole, page.results.label_delta)
    page.results.formLayout.setWidget(2, QFormLayout.FieldRole, page.results.delta)

    # gamma
    page.results.label_gamma = QLabel()
    # page.results.label_gamma.setFont(page.font_content)
    page.results.label_gamma.setText("gamma")
    page.results.gamma = QLineEdit(page.results)
    page.results.gamma.setReadOnly(True)
    page.results.formLayout.setWidget(3, QFormLayout.LabelRole, page.results.label_gamma)
    page.results.formLayout.setWidget(3, QFormLayout.FieldRole, page.results.gamma)

    # theta
    page.results.label_theta = QLabel()
    # page.results.label_theta.setFont(page.font_content)
    page.results.label_theta.setText("theta")
    page.results.theta = QLineEdit(page.results)
    page.results.theta.setReadOnly(True)
    page.results.formLayout.setWidget(4, QFormLayout.LabelRole, page.results.label_theta)
    page.results.formLayout.setWidget(4, QFormLayout.FieldRole, page.results.theta)

    # vega (%)
    page.results.label_vega = QLabel()
    # page.results.label_vega.setFont(page.font_content)
    page.results.label_vega.setText("vega (%)")
    page.results.vega = QLineEdit(page.results)
    page.results.vega.setReadOnly(True)
    page.results.formLayout.setWidget(5, QFormLayout.LabelRole, page.results.label_vega)
    page.results.formLayout.setWidget(5, QFormLayout.FieldRole, page.results.vega)

    # rho (%)
    page.results.label_rho = QLabel()
    # page.results.label_rho.setFont(page.font_content)
    page.results.label_rho.setText("rho (%)")
    page.results.rho = QLineEdit(page.results)
    page.results.rho.setReadOnly(True)
    page.results.formLayout.setWidget(6, QFormLayout.LabelRole, page.results.label_rho)
    page.results.formLayout.setWidget(6, QFormLayout.FieldRole, page.results.rho)

    page.results.gridLayout.addLayout(page.results.formLayout, 0, 0, 1, 1)