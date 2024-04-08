# -*- coding: utf-8 -*-
"""
Created on 2024-04-08 12:27
@author: k-takeuchi
@note: 
"""
from PyQt6 import uic
from PyQt6.QtWidgets import *

# UIファイルのパス
ui_file_path = "src/views/todol.ui"

# UIファイルからロード
Ui_MainWindow, QtBaseClass = uic.loadUiType(ui_file_path)


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)  # UIのセットアップ

        prevPageBtn:QPushButton = self.prevPageBtn
        prevPageBtn.clicked.connect(self.changeCurrentPage)

        nextPageBtn:QPushButton = self.nextPageBtn
        nextPageBtn.clicked.connect(self.changeCurrentPage)

        self.changeCurrentPage()

    def changeCurrentPage(self):
        prevPageBtn:QPushButton = self.prevPageBtn
        nextPageBtn:QPushButton = self.nextPageBtn
        pageStacked: QStackedWidget = self.pageStacked
        
        page_idx = pageStacked.currentIndex()

        if page_idx - 1 > 0:
            page_idx -= 1
            pageStacked.setCurrentIndex(page_idx)

        elif page_idx + 1 < pageStacked.count():
            page_idx += 1
            pageStacked.setCurrentIndex(page_idx)

        if page_idx == 0:
            prevPageBtn.setDisabled(True)
        else:
            prevPageBtn.setDisabled(False)

        if page_idx == pageStacked.count():
            nextPageBtn.setDisabled(True)
        else:
            nextPageBtn.setDisabled(False)


if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()
