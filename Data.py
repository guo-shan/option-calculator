from PyQt5.QtWidgets import QPushButton, QLabel, QRadioButton, QTextEdit
import Frontend.Form as Form
import numpy as np


def DataUI(page):

    ########################################################################################
    # 导入数据并计算历史波动率
    ########################################################################################

    # 统计周期
    page.data.label_period = QLabel()
    # page.data.label_model.setFont(page.font_content)
    page.data.label_period.setText("统计周期")
    page.data.gridLayout.addWidget(page.data.label_period, 0, 0, 1, 1)

    # 7天
    page.data.seven = QRadioButton(page.data)
    page.data.seven.setText("7天")
    page.data.seven.setChecked(True)
    page.data.seven.toggled.connect(page.buttonState)
    page.data.gridLayout.addWidget(page.data.seven, 0, 1, 1, 1)\

    # 30天
    page.data.thirty = QRadioButton(page.data)
    page.data.thirty.setText("30天")
    page.data.thirty.toggled.connect(page.buttonState)
    page.data.gridLayout.addWidget(page.data.thirty, 0, 2, 1, 1)

    # 60天
    page.data.sixty = QRadioButton(page.data)
    page.data.sixty.setText("60天")
    page.data.sixty.toggled.connect(page.buttonState)
    page.data.gridLayout.addWidget(page.data.sixty, 0, 3, 1, 1)

    # 90天
    page.data.ninety = QRadioButton(page.data)
    page.data.ninety.setText("90天")
    page.data.ninety.toggled.connect(page.buttonState)
    page.data.gridLayout.addWidget(page.data.ninety, 0, 4, 1, 1)

    # 计算波动率
    page.data.label_calculate = QLabel()
    # page.data.label_calculate.setFont(page.font_content)
    page.data.label_calculate.setText("计算波动率")
    page.data.gridLayout.addWidget(page.data.label_calculate, 1, 0, 1, 1)

    # 导入excel数据并计算
    page.data.btn_excel = QPushButton("excel导入数据计算")
    page.data.gridLayout.addWidget(page.data.btn_excel, 1, 1, 1, 2)
    page.data.btn_excel.setStyleSheet('''
            QPushButton:hover{color:red}
            QPushButton{font-size:18px;
                        font-weight:200;
            }''')
    page.data.btn_excel.clicked.connect(page.excelData)

    # 重置参数
    page.data.btn_mysql = QPushButton("mysql导入数据计算")
    page.data.gridLayout.addWidget(page.data.btn_mysql, 1, 3, 1, 2)
    page.data.btn_mysql.setStyleSheet('''
            QPushButton:hover{color:red}
            QPushButton{font-size:18px;
                        font-weight:200;
            }''')
    page.data.btn_mysql.clicked.connect(page.mysqlData)

    # 计算公式
    page.data.formula = QTextEdit(page.data)
    page.data.formula.setReadOnly(True)
    str = "<font size = \"4\"><b>历史波动率计算公式：</b></font>" + " \
        <p align = \"center\">R<sub>t</sub> = ln(S<sub>t</sub> / S<sub>t-1</sub>)</p>" + "\
        其中：ln表示自然对数；S<sub>t</sub>表示当日收盘价，S<sub>t-1</sub>表示昨日收盘价；R<sub>t</sub>表示日收益率" + "\n" + "\
        <p align = \"center\">R<sub>avg</sub> = Σ<sub>i=1</sub><sup>n</sup>R<sub>i</sub> / n</p>" + "\
        其中：n表示统计周期，默认为7天；R<sub>avg</sub>表示统计周期内的R<sub>t</sub>平均值" + "\n" + "\
        <p align = \"center\">σ<sup>2</sup> = Σ<sub>i=1</sub><sup>n</sup>(R<sub>i</sub> - R<sub>avg</sub>)<sup>2</sup> / (n - 1)</p>" + "\
        其中：σ<sup>2</sup>表示统计周期内的R<sub>t</sub>方差，σ表示统计周期内的R<sub>t</sub>标准差</p>" + "\n" + "\
        <p align = \"center\">HV<sub>y</sub> = σ * (250)<sup>0.5</sup></p>" + "\
        其中：一年设置为250个交易日；HV<sub>y</sub>表示年化标准差，用此数值表示年度波动率</p>" + "\n" + "\
        "
    page.data.formula.append(str)
    page.data.gridLayout.addWidget(page.data.formula, 2, 0, 1, 5)

def ImportData(page):
    if page.data.importManner == "excel":
        if page.arguments.combo_name.currentText() == "000001 平安银行":
            page.data.filename = "D:\data\K线导出_000001_日线数据-不复权.xls"
        elif page.arguments.combo_name.currentText() == "601211 国泰君安":
            page.data.filename = "D:\data\K线导出_601211_日线数据-不复权.xls"
    elif page.data.importManner == "mysql":
        if page.arguments.combo_name.currentText() == "000001 平安银行":
            page.data.table = "tb_000001"
        elif page.arguments.combo_name.currentText() == "601211 国泰君安":
            page.data.table = "tb_601211"

def calVol(fm, page):
#     log_returns = [np.nan]
#     for index in range(len(fm) - 1):
#         log_returns.append(np.log(fm.loc[index + 1, "收盘价"] / fm.loc[index, "收盘价"]))
#     fm = fm.assign(log_returns=log_returns)

#     sds = [np.nan] * page.data.period
#     volatility = [np.nan] * page.data.period
#     for index in range(1, len(fm) - page.data.period + 1):
#         sd = np.std(fm.loc[index : index + page.data.period, 'log_returns'], ddof=1)
#         sds.append(sd)
#         volatility.append(sd * np.sqrt(page.data.sessions_in_year))
#     fm = fm.assign(standard_deviationt = sds)
#     fm = fm.assign(historical_volatility = volatility)

    log_returns = []
    for index in range(len(fm) - page.data.period - 1, len(fm) - 1):
        log_returns.append(np.log(fm.loc[index + 1, "收盘价"] / fm.loc[index, "收盘价"]))
    sd = np.std(log_returns, ddof=1)
    volatility = sd * np.sqrt(page.data.sessions_in_year)

    page.mainwindow.page_input.arguments.sigma.setText(str(volatility))
    Form.showForm(fm, page)


