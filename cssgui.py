# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:35:29 2026

@author: User
"""


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
        self.button1=QPushButton("#1")
        self.button2=QPushButton("#2")
        self.button3=QPushButton("#3")
   
        
        self.initUI()
        
        
    def initUI(self):
        centeral_widget=QWidget()
        self.setCentralWidget(centeral_widget)
        
        hbox=QHBoxLayout()
        hbox.addWidget( self.button1)
        hbox.addWidget( self.button2)
        hbox.addWidget( self.button3)
        
        centeral_widget.setLayout(hbox)
        
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        
        self.setStyleSheet("""
                   QPushButton{
                       font-size:40px;
                       font-family: Arial;
                       padding:15px 75px;
                      
                       margin:25px;
                       border:3px solid;
                       border-radius:15px;
                       } 
                  QPushButton#button1{
                  background-color:red;
                  
                  }
                 QPushButton#button2{
                 background-color:yellow;
                           
                           }
                 QPushButton#button3{
                 background-color:blue;
                  
                  }  
               QPushButton#button1:hover{
               background-color:blue;
                           
                           }
              QPushButton#button2:hover{
              background-color:green;
                                    
                                    }
             QPushButton#button3:hover{
             background-color:red;
                           
                           }
                           
                           
               """)
        
           
           



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())