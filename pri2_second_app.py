# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pandas  as pd 
import analysisPackage
import priNextstep2
import string 
import insideModel
import Custom_analysis
csv_path=''
file_name=''


def online_check(purpose_col,goal_col,generality_col,facts_col,purpose,goal,fact,generality):
    try :
        purpose_col =  [ Custom_analysis.analysis(purpose,  i )  for i in purpose_col ] 
        goal_col = [ Custom_analysis.analysis(goal ,  i )  for i in goal_col ]
        facts_col = [ priNextstep2.Do_all(fact, i) for i in facts_col ]
        generality_col  = [  priNextstep2.Do_all( generality , i) for i in generality_col  ]
    except Exception as e  :
        print(e.args)
        
    return purpose_col,goal_col,generality_col,facts_col

def inbuild_check(purpose_col,goal_col,generality_col,facts_col,purpose,goal,fact,generality):
    purpose_col =  [ insideModel.getscore(purpose, i) for i in purpose_col ] 
    goal_col = [ insideModel.getscore(goal ,  i )  for i in goal_col ]
    facts_col = [ insideModel.getscore(fact, i) for i in facts_col ]
    generality_col  = [  insideModel.getscore( generality , i) for i in generality_col  ]
    return purpose_col,goal_col,generality_col,facts_col      


class Ui_MainWindow(object):
    

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Anglais Marketing")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Goal_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.Goal_textEdit.setGeometry(QtCore.QRect(430, 150, 321, 71))
        self.Goal_textEdit.setObjectName("Goal_textEdit")
        
        self.Purpose_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.Purpose_textEdit.setGeometry(QtCore.QRect(430, 40, 321, 71))
        self.Purpose_textEdit.setObjectName("Purpose_textEdit")
        
        self.Generality_textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.Generality_textEdit_3.setGeometry(QtCore.QRect(430, 260, 321, 71))
        self.Generality_textEdit_3.setObjectName("Generality_textEdit_3")
        
        self.Fact_textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.Fact_textEdit_4.setGeometry(QtCore.QRect(430, 370, 321, 71))
        self.Fact_textEdit_4.setObjectName("Fact_textEdit_4")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 480, 191, 51))
        self.pushButton.setObjectName("pushButton")
        
        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 480, 141, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.purpose = QtWidgets.QLabel(self.centralwidget)
        self.purpose.setGeometry(QtCore.QRect(60, 60, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.purpose.setFont(font)
        self.purpose.setObjectName("purpose")
        self.goal = QtWidgets.QLabel(self.centralwidget)
        self.goal.setGeometry(QtCore.QRect(60, 170, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.goal.setFont(font)
        self.goal.setObjectName("goal")
        self.Generality = QtWidgets.QLabel(self.centralwidget)
        self.Generality.setGeometry(QtCore.QRect(60, 280, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.Generality.setFont(font)
        self.Generality.setObjectName("Generality")
        self.Fact = QtWidgets.QLabel(self.centralwidget)
        self.Fact.setGeometry(QtCore.QRect(60, 390, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.Fact.setFont(font)
        self.Fact.setObjectName("Fact")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton.clicked.connect(self.getpathlink)
        
        self.pushButton_2.clicked.connect(self.start_evaluation)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Select CSV"))
        self.pushButton_2.setText(_translate("MainWindow", "Start Evaluation"))
        self.purpose.setText(_translate("MainWindow", "Enter Purpose "))
        self.goal.setText(_translate("MainWindow", "Enter Goal"))
        self.Generality.setText(_translate("MainWindow", "Enter Generality"))
        self.Fact.setText(_translate("MainWindow", "Enter Facts"))
    
    def getpathlink(self):
        global csv_path
        global file_name

        csv_path = QtWidgets.QFileDialog.getOpenFileName()[0]
        file_name =  "result_" + csv_path.split('/')[-1]
        print(csv_path,file_name)
        
    def start_evaluation(self):
        global csv_path
        global file_name
        
        if  csv_path =='' or self.Purpose_textEdit.toPlainText()=='' or  self.Goal_textEdit.toPlainText()=='' or  self.Fact_textEdit_4.toPlainText()=='' or self.Generality_textEdit_3.toPlainText() =='':
            msg1 = QMessageBox()
            msg1.setWindowTitle("Info")
            msg1.setText("Please do fill all entries as well as uploading the csv file")
            msg1.setIcon(QMessageBox.Information)
            x=msg1.exec_()

            return
        

        
        data = pd.read_csv(csv_path , encoding= 'unicode_escape') 
        purpose_col = data.iloc[:,3]
        goal_col = data.iloc[:,4]
        generality_col = data.iloc[:,5]
        facts_col =  data.iloc[:,6]   

        
        for fx in [online_check,inbuild_check] :
            try :
                purpose_col,goal_col,generality_col,facts_col = fx(purpose_col,goal_col,generality_col,facts_col ,self.Purpose_textEdit.toPlainText(),self.Goal_textEdit.toPlainText(),self.Fact_textEdit_4.toPlainText(),self.Generality_textEdit_3.toPlainText()  )
                break 
            except Exception as e  :
                msg3 = QMessageBox()
                msg3.setWindowTitle("Info")
                msg3.setText("Inbuild Model has been used")
                msg3.setIcon(QMessageBox.Information)
                x=msg3.exec_()
                print(e.args)
                continue         
        
        
        
        data['purpose_result'] = purpose_col
        data['goal_result'] = goal_col
        data['generality_result'] = generality_col
        data['fact_result'] = facts_col    
        data.to_csv( "".join([i+'/' for i in csv_path.split('/')[0:-1] ])+file_name)
        
        msg2 = QMessageBox()
        msg2.setWindowTitle("Info")
        msg2.setText("The csv file has been processed successfully")
        msg2.setIcon(QMessageBox.Information)
        x=msg2.exec_()
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
