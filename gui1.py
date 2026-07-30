# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:07:43 2026

@author: User
"""

#pyQt5 introduction

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel
                             ,QWidget,QVBoxLayout,QHBoxLayout,
                             QGridLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my first gui")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("kk2.jpg"))
        self.initUI()
        """
        lable=QLabel("hello",self)
        lable.setFont(QFont("Arial",30))
        lable.setGeometry(0,0,250,250)
        lable.setStyleSheet("color:47, 60, 74;"
                            "background-color:#1170d6;"
                            "font-weight:bold;")
        lable.setAlignment(Qt.AlignTop)
        lable.setAlignment(Qt.AlignRight)
        
        pixmap=QPixmap("kk2.jpg")
        lable.setPixmap(pixmap)
        lable.setScaledContents(True)
        
        lable.setGeometry((self.width()-lable.width()) // 2,
                          (self.height()-lable.height()) // 2,
                          lable.width(),lable.height())
        """
    def initUI(self):
        centeral_widget=QWidget()
        self.setCentralWidget(centeral_widget)
        
        lable1=QLabel("#1",self)
        lable2=QLabel("#2",self)
        lable3=QLabel("#3",self)
        lable4=QLabel("#4",self)
        lable5=QLabel("#5",self)
        
        lable1.setStyleSheet("background-color:red;")
        lable2.setStyleSheet("background-color:yellow;")
        lable3.setStyleSheet("background-color:blue;")
        lable4.setStyleSheet("background-color:green;")
        lable5.setStyleSheet("background-color:purple;")
        
        grid=QGridLayout()
        
        grid.addWidget(lable1, 0,0)
        grid.addWidget(lable2,0,1)
        grid.addWidget(lable3,1,0)
        grid.addWidget(lable4,1,1)
        grid.addWidget(lable5,2,2)
        
        centeral_widget.setLayout(grid)
        
        
         
   
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    