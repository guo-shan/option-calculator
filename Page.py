# 存放按下每个功能键的主页面
import sys
from threading import Thread

sys.path.append("..")
from PyQt5.QtWidgets import (QWidget, QMessageBox, QGridLayout, QFormLayout, QGroupBox)
from PyQt5.QtGui import QFont
import pandas as pd
from Backend.Option import Option
import Frontend.Data as Data
import Frontend.ImpVol as ImpVol
import pymysql
from pymysql.cursors import DictCursor

class Calculatebs(Thread):

    def __init__(self, option):
        super().__init__()
        self.option = option

    def run(self):
        self.option.bsm()

class page:
    def __init__(self, grid, mainwindow):
        self.mainwindow = mainwindow
        self.widget = QWidget()
        self.grid = QGridLayout()
        self.grid.setSpacing(20)
        self.widget.setLayout(self.grid)
        grid.addWidget(self.widget, 1, 1, 13, 4)

        # 设置文本字体
        self.font_content = QFont()
        self.font_content.setFamily('微软雅黑')
        self.font_content.setPointSize(15)
        self.font_content.setWeight(40)

        self.arguments = QGroupBox(self.widget)
        self.arguments.setTitle("参数设置")
        self.arguments.gridLayout = QGridLayout(self.arguments)
        self.arguments.gridLayout.setObjectName("gridLayout1")
        self.arguments.formLayout = QFormLayout()
        self.arguments.formLayout.setObjectName("formLayout1")
        self.grid.addWidget(self.arguments, 0, 0, 2, 2)

        self.results = QGroupBox(self.widget)
        self.results.setTitle("计算结果")
        self.results.gridLayout = QGridLayout(self.results)
        self.results.gridLayout.setObjectName("gridLayout2")
        self.results.formLayout = QFormLayout()
        self.results.formLayout.setObjectName("formLayout2")
        self.grid.addWidget(self.results, 0, 2, 1, 2)

        self.impVol = QGroupBox(self.widget)
        self.impVol.setTitle("隐含波动率")
        self.impVol.gridLayout = QGridLayout(self.impVol)
        self.impVol.gridLayout.setObjectName("gridLayout3")
        self.impVol.formLayout = QFormLayout()
        self.impVol.formLayout.setObjectName("formLayout3")
        self.impVol.formLayout1 = QFormLayout()
        self.impVol.formLayout1.setObjectName("formLayout4")
        self.impVol.formLayout2 = QFormLayout()
        self.impVol.formLayout2.setObjectName("formLayout5")
        self.impVol.formLayout3 = QFormLayout()
        self.impVol.formLayout3.setObjectName("formLayout6")
        self.grid.addWidget(self.impVol, 1, 2, 1, 2)

        self.data = QGroupBox(self.widget)
        self.data.setTitle("历史波动率计算")
        self.data.gridLayout = QGridLayout(self.data)
        self.data.gridLayout.setObjectName("gridLayout4")
        self.grid.addWidget(self.data, 2, 0, 1, 2)

        self.form = QGroupBox(self.widget)
        self.form.setTitle("历史波动率数据")
        self.form.gridLayout = QGridLayout(self.form)
        self.form.gridLayout.setObjectName("gridLayout5")
        self.grid.addWidget(self.form, 2, 2, 1, 2)

        # 一些期权参数的属性
        self.arguments.combo_european = None
        self.arguments.s0 = None
        self.arguments.k = None
        self.arguments.combo_kind = None
        self.arguments.date_edit_t0 = None
        self.arguments.date_edit_t1 = None
        self.arguments.sigma = None
        self.arguments.r = None

        self.results.price = None
        self.results.delta = None
        self.results.gamma = None
        self.results.theta = None
        self.results.vega = None
        self.results.rho = None

        self.impVol.v = None
        self.impVol.impVol = None

        self.data.period = 6
        self.data.sessions_in_year = 250
        self.data.filename = None
        self.data.table = None
        self.data.importManner = None

        self.connection = pymysql.connect(
            host = "localhost", 
            port = 3306,
            user = "root", 
            password = "123456", 
            db = "mysql")  # 数据库

    #  确认输入
    def confirm(self):
        try:
            if self.arguments.combo_kind.currentText() == "看涨":
                kind = 1
            else:
                kind = -1
            if self.arguments.combo_european.currentText() == "欧式期权":
                european = True
            else:
                european = False
            s0 = float(self.arguments.s0.text())
            k = float(self.arguments.k.text())
            sigma = float(self.arguments.sigma.text()) / 100
            r = float(self.arguments.r.text()) / 100
            t1 = self.arguments.t1.date()
            t0 = self.arguments.t0.date()
            t = t0.daysTo(t1) / 365
            v = float(self.impVol.v.text())
            sigma_min = float(self.impVol.sigma_min.text())
            sigma_max = float(self.impVol.sigma_max.text())
            if s0 <= 0 or k <= 0 or sigma == 0 or t == 0:
                if s0 <= 0:
                    QMessageBox.about(self.widget,
                            "提示",
                            "标的价格不能小于等于0\n请重新输入！")
                if k <= 0:
                    QMessageBox.about(self.widget,
                            "提示",
                            "行权价格不能小于等于0\n请重新输入！")
                if sigma == 0:
                    QMessageBox.about(self.widget,
                            "提示",
                            "波动率不能等于0\n请重新输入！")
                if t == 0:
                    QMessageBox.about(self.widget,
                            "提示",
                            "当前日期和到期日期差值不能为0\n请重新输入！")
            else:
                option = Option(european, kind, s0, k, t, r, sigma, self)
                option.BSM()
                option.Greek()
                ImpVol.CalImpVol(european, kind, s0, k, t, r, sigma_min, sigma_max, v, self)

                # t = Calculatebs(option)
                # t.start()
                # t.join()

                self.mainwindow.page_input.results.price.setText(str(option.bsmprice))
                self.mainwindow.page_input.results.delta.setText(str(option.delta))
                self.mainwindow.page_input.results.gamma.setText(str(option.gamma))
                self.mainwindow.page_input.results.theta.setText(str(option.theta))
                self.mainwindow.page_input.results.vega.setText(str(option.vega))
                self.mainwindow.page_input.results.rho.setText(str(option.rho))
            
        except ValueError:
            QMessageBox.about(self.widget,
                              "提示",
                              "您的输入有误......\n请仔细检查！")

    def reset(self):
        self.arguments.s0.setText("100")
        self.arguments.k.setText("100")
        self.arguments.sigma.setText("1")
        self.arguments.r.setText("1")
    
    def buttonState(self):
        if self.data.seven.isChecked():
            self.data.period = 6
        elif self.data.thirty.isChecked():
            self.data.period = 29
        elif self.data.sixty.isChecked():
            self.data.period = 59
        elif self.data.ninety.isChecked():
            self.data.period = 89  
        else:
            self.data.period = 6         

    def excelData(self):
        self.data.importManner = "excel"
        Data.ImportData(self)
        fm = pd.read_excel(self.data.filename, sheet_name = "Sheet0")
        Data.calVol(fm, self)
    
    def mysqlData(self):
        self.data.importManner = "mysql"
        Data.ImportData(self)
        cursor = self.connection.cursor(DictCursor) # 获取游标
        sql = "select " + "*" + " from " + self.data.table
        cursor.execute(sql) # 执行sql
        data = cursor.fetchall() # 获取所有执行结果
        fm = pd.DataFrame(data)
        cursor.close() #关闭游标
        Data.calVol(fm, self)      