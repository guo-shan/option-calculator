from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QDateEdit, QFormLayout
from PyQt5.QtCore import QDate


def ArgumentsUI(page):

    ########################################################################################
    # 参数设置
    ########################################################################################

    # 标的类型
    page.arguments.label_type = QLabel()
    # page.arguments.label_type.setFont(page.font_content)
    page.arguments.label_type.setText("标的类型")
    page.arguments.combo_type = QComboBox(page.arguments)
    page.arguments.combo_type.addItem("股票")
    page.arguments.formLayout.setWidget(0, QFormLayout.LabelRole, page.arguments.label_type)
    page.arguments.formLayout.setWidget(0, QFormLayout.FieldRole, page.arguments.combo_type)

    # 选择期权
    page.arguments.label_name = QLabel()
    # page.arguments.label_name.setFont(page.font_content)
    page.arguments.label_name.setText("行权方式")
    page.arguments.combo_name = QComboBox(page.arguments)
    page.arguments.combo_name.addItem("000001 平安银行")
    page.arguments.combo_name.addItem("601211 国泰君安")
    page.arguments.formLayout.setWidget(1, QFormLayout.LabelRole, page.arguments.label_name)
    page.arguments.formLayout.setWidget(1, QFormLayout.FieldRole, page.arguments.combo_name)

    # 期权类型 美式欧式
    page.arguments.label_european = QLabel()
    # page.arguments.label_european.setFont(page.font_content)
    page.arguments.label_european.setText("行权方式")
    page.arguments.combo_european = QComboBox(page.arguments)
    page.arguments.combo_european.addItem("欧式期权")
    page.arguments.combo_european.addItem("美式期权")
    page.arguments.formLayout.setWidget(2, QFormLayout.LabelRole, page.arguments.label_european)
    page.arguments.formLayout.setWidget(2, QFormLayout.FieldRole, page.arguments.combo_european)

    # 标的资产现价
    page.arguments.label_s0 = QLabel()
    # page.arguments.label_s0.setFont(page.font_content)
    page.arguments.label_s0.setText("标的价格")
    page.arguments.s0 = QLineEdit(page.arguments)
    page.arguments.s0.setText("100")
    page.arguments.formLayout.setWidget(3, QFormLayout.LabelRole, page.arguments.label_s0)
    page.arguments.formLayout.setWidget(3, QFormLayout.FieldRole, page.arguments.s0)

    # 期权执行价
    page.arguments.label_k = QLabel()
    # page.arguments.label_k.setFont(page.font_content)
    page.arguments.label_k.setText("行权价格")
    page.arguments.k = QLineEdit(page.arguments)
    page.arguments.k.setText("100")
    page.arguments.formLayout.setWidget(4, QFormLayout.LabelRole, page.arguments.label_k)
    page.arguments.formLayout.setWidget(4, QFormLayout.FieldRole, page.arguments.k)

    # 期权类型 看涨看跌
    page.arguments.label_kind = QLabel()
    # page.arguments.label_kind.setFont(page.font_content)
    page.arguments.label_kind.setText("看涨看跌")
    page.arguments.combo_kind = QComboBox(page.arguments)
    page.arguments.combo_kind.addItem("看涨")
    page.arguments.combo_kind.addItem("看跌")
    page.arguments.formLayout.setWidget(5, QFormLayout.LabelRole, page.arguments.label_kind)
    page.arguments.formLayout.setWidget(5, QFormLayout.FieldRole, page.arguments.combo_kind)

    # 选择当前时间
    page.arguments.label_t0 = QLabel()
    # page.arguments.label_t0.setFont(page.font_content)
    page.arguments.label_t0.setText("当前日期")
    page.arguments.t0 = QDateEdit(QDate.currentDate(), page.arguments)
    page.arguments.t0.setDisplayFormat('yyyy-MM-dd')
    page.arguments.t0.setCalendarPopup(True)
    page.arguments.formLayout.setWidget(6, QFormLayout.LabelRole, page.arguments.label_t0)
    page.arguments.formLayout.setWidget(6, QFormLayout.FieldRole, page.arguments.t0)

    # 选择到期时间
    page.arguments.label_t1 = QLabel()
    # page.arguments.label_t1.setFont(page.font_content)
    page.arguments.label_t1.setText("到期日期")
    page.arguments.t1 = QDateEdit(QDate.currentDate().addDays(10), page.arguments)
    page.arguments.t1.setDisplayFormat('yyyy-MM-dd')
    page.arguments.t1.setCalendarPopup(True)
    page.arguments.formLayout.setWidget(7, QFormLayout.LabelRole, page.arguments.label_t1)
    page.arguments.formLayout.setWidget(7, QFormLayout.FieldRole, page.arguments.t1)

    # 适用的波动率
    page.arguments.label_sigma = QLabel()
    # page.arguments.label_sigma.setFont(page.font_content)
    page.arguments.label_sigma.setText("年度波动率 (%)")
    page.arguments.sigma = QLineEdit(page.arguments)
    page.arguments.sigma.setText("1")
    page.arguments.formLayout.setWidget(8, QFormLayout.LabelRole, page.arguments.label_sigma)
    page.arguments.formLayout.setWidget(8, QFormLayout.FieldRole, page.arguments.sigma)

    # 适用的无风险利率
    page.arguments.label_r = QLabel()
    # page.arguments.label_r.setFont(page.font_content)
    page.arguments.label_r.setText("无风险利率 (%)")
    page.arguments.r = QLineEdit(page.arguments)
    page.arguments.r.setText("1")
    page.arguments.formLayout.setWidget(9, QFormLayout.LabelRole, page.arguments.label_r)
    page.arguments.formLayout.setWidget(9, QFormLayout.FieldRole, page.arguments.r)

    page.arguments.gridLayout.addLayout(page.arguments.formLayout, 0, 0, 1, 5)

    # 确定输入按键
    page.arguments.btn_confirm = QPushButton("确定输入")
    page.arguments.gridLayout.addWidget(page.arguments.btn_confirm, 1, 1, 1, 1)
    page.arguments.btn_confirm.setStyleSheet('''
            QPushButton:hover{color:red}
            QPushButton{font-size:18px;
                        font-weight:200;
            }''')
    page.arguments.btn_confirm.clicked.connect(page.confirm)

    # 重置参数
    page.arguments.btn_reset = QPushButton("重置参数")
    page.arguments.gridLayout.addWidget(page.arguments.btn_reset, 1, 3, 1, 1)
    page.arguments.btn_reset.setStyleSheet('''
            QPushButton:hover{color:red}
            QPushButton{font-size:18px;
                        font-weight:200;
            }''')
    page.arguments.btn_reset.clicked.connect(page.reset)
