"""
Created on Thu Jul 30 12:49:37 2026

@author: User
"""
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel
                             ,QWidget,QVBoxLayout,QHBoxLayout,
                             QGridLayout,QPushButton,QCheckBox,
                             QRadioButton,QButtonGroup,QLineEdit 
                             )
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my first gui")
        self.setGeometry(700,300,500,500)
        self.button=QPushButton("click me",self)
        
        
        self.checkbox=QCheckBox("Do you like food",self)
        self.lable=QLabel("Hello",self)
        
        
        self.radio1=QRadioButton("visa",self)
        self.radio2=QRadioButton("master card",self)
        self.radio3=QRadioButton("gift card",self)
        self.radio4=QRadioButton("in-store",self)
        self.radio5=QRadioButton("online",self)
        
        self.button_group1=QButtonGroup(self)
        self.button_group2=QButtonGroup(self)
        
        self.line_edit=QLineEdit(self)
        self.butt=QPushButton("Submit",self)
        
        self.initUI()
        
        
    def initUI(self):
           
           self.button.setGeometry(100,200,200,100)
           self.button.setStyleSheet("font-size:30px;")
           self.button.clicked.connect(self.on_clik)
           self.lable.setGeometry(150,300,200,100)
           self.lable.setStyleSheet("font-size:30px;")
           
           
           self.checkbox.setStyleSheet("font-size:26px;"
                                       "font-family:Arial;")
           self.checkbox.setGeometry(0,10,500,100)
           self.checkbox.setLayoutDirection(Qt.RightToLeft)
           
           
           self.radio1.setGeometry(0,50,300,50)
           self.radio2.setGeometry(0,100,300,50)
           self.radio3.setGeometry(0,150,300,50)
           self.radio4.setGeometry(0,200,300,50)
           self.radio5.setGeometry(0,250,300,50)
           
           
           self.setStyleSheet("QRadioButton{"
                              "font-size:26px;"
                              "font-family:Arial;"
                              "padding:10px;"
                              "}")
           
           self.button_group1.addButton(self.radio1)
           self.button_group1.addButton(self.radio2)
           self.button_group1.addButton(self.radio3)
           self.button_group2.addButton(self.radio4)
           self.button_group2.addButton(self.radio5)
           
           
           self.line_edit.setGeometry(10,10,200,40)
           self.line_edit.setStyleSheet("font-size:25px;")
           self.butt.setGeometry(210,10,100,40)
           self.butt.setStyleSheet("font-size:25px;")
           self.butt.clicked.connect(self.submit)
           
           self.line_edit.setPlaceholderText("Enter your name")
           
    def on_clik(self):
        print("button cliked")
        self.lable.setText("Good bay!") 
    def submit(self):
      text=self.line_edit.text()
      print(f"hello {text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
   