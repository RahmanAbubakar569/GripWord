import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QApplication
from PyQt5 import QtCore, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(530,750)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("gripword logo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gen_text = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.gen_text.setFont(font)
        self.gen_text.setObjectName("gen_text")
        self.horizontalLayout_4.addWidget(self.gen_text)
        self.display_pass = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.display_pass.setFont(font)
        self.display_pass.setObjectName("display_pass")
        self.horizontalLayout_4.addWidget(self.display_pass)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gen_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.gen_button.setFont(font)
        self.gen_button.setStyleSheet("QPushButton{\n"
"                 \n"
"    \n"
"    \n"
"    background-color: rgb(255, 86, 1);\n"
"    \n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 136, 56);\n"
"}\n"
"\n"
"\n"
"")
        self.gen_button.setObjectName("gen_button")
        self.gen_button.clicked.connect(self.gen_click) # connecting the generate button to the def gen_click function
        self.horizontalLayout_5.addWidget(self.gen_button)
        self.copy_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.copy_button.setFont(font)
        self.copy_button.setStyleSheet("QPushButton{\n"
"     background-color: rgb(255, 86, 1);\n"
"    \n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 136, 56);\n"
"}\n"
"")
        self.copy_button.setObjectName("copy_button")
        self.copy_button.clicked.connect(self.copy_click) # connecting the copy button to the def copy_click function 
        self.horizontalLayout_5.addWidget(self.copy_button)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "GRIPWORD v1"))
        self.gen_text.setText(_translate("mainWindow", "  GENERATED PASSWORD"))
        self.display_pass.setText(_translate("mainWindow", "      "))
        self.gen_button.setText(_translate("mainWindow", "GENERATE"))
        self.copy_button.setText(_translate("mainWindow", "COPY"))
    
    def gen_click(self):
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_class = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789" 
        symbols = "[]{}!@#$%^&*()_-+\|"
        parameter = lower_case + upper_class + numbers + symbols
        length = 8
        Gen_password = "".join(random.sample(parameter,length))
        self.display_pass.setText(Gen_password)


    def copy_click(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.display_pass.text(), mode = cb.Clipboard)



        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
