from PyQt5.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt
def FormUI(page):

    ########################################################################################
    # 历史波动率计算用的数据
    ########################################################################################

    # 数据
    page.form.tableWidget = QTableWidget(0, 4, page.form)
    titles = ["证券代码", "证券名称", "交易时间", "收盘价"]
    page.form.tableWidget.setHorizontalHeaderLabels(titles)
    # 隐藏垂直表头
    page.form.tableWidget.verticalHeader().hide()
    # 宽度适应
    page.form.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    page.form.gridLayout.addWidget(page.form.tableWidget, 0, 0, 1, 1)

def showForm(fm, page):
    page.form.tableWidget.setRowCount(page.data.period + 1)
    for i in range(page.data.period + 1):
        if page.arguments.combo_type.currentText() == "股票":
            item = QTableWidgetItem(str(fm.loc[len(fm) - page.data.period - 1 + i, "证券代码"]).zfill(6))
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        page.form.tableWidget.setItem(i, 0, item)

        item = QTableWidgetItem(str(fm.loc[len(fm) - page.data.period - 1 + i, "证券名称"]))
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        page.form.tableWidget.setItem(i, 1, item)
        
        if page.data.importManner == "excel":
            item = QTableWidgetItem(str(fm.loc[len(fm) - page.data.period - 1 + i, "交易时间"])[:-9])
        elif page.data.importManner == "mysql":
            item = QTableWidgetItem(str(fm.loc[len(fm) - page.data.period - 1 + i, "交易时间"]))
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        page.form.tableWidget.setItem(i, 2, item)

        item = QTableWidgetItem(format(fm.loc[len(fm) - page.data.period - 1 + i, "收盘价"], ".4f"))
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        page.form.tableWidget.setItem(i, 3, item)