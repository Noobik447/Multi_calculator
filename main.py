from PyQt5 import QtGui, QtWidgets, QtCore
import math
import random

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QtGui.QIcon("calc.png"))
        self.settings = QtCore.QSettings("Настройки", "Мульти_калькулятор")
        
        if self.settings.contains("Окно/Местоположение"):
            self.setGeometry(self.settings.value("Окно/Местоположение"))
        else:
            self.resize(200, 100)
            
        if self.settings.contains("Режимы/Режим"):
            if self.settings.value("Режимы/Режим") == "calc":
                self.calc()
            elif self.settings.value("Режимы/Режим") == "code":
                self.code()
        else:
            self.calc()
        
        self._createActions()
        self._createMenuBar()
        
    def _createMenuBar(self):
        menuBar = self.menuBar()
        calcMenu = QtWidgets.QMenu("Режим", self)
        menuBar.addMenu(calcMenu)
        calcMenu.addAction(self.calcAction)
        calcMenu.addAction(self.codeAction)
        
    def _createActions(self):
        self.calcAction = QtWidgets.QAction("Калькулятор", self)
        self.calcAction.triggered.connect(self.calc)
        self.codeAction = QtWidgets.QAction("Системы счисления", self)
        self.codeAction.triggered.connect(self.code)
        
    def closeEvent(self, event):
        self.settings.beginGroup("Окно")
        self.settings.setValue("Местоположение", self.geometry())
        self.settings.endGroup()
        
        self.settings.beginGroup("Режимы")
        self.settings.setValue("Режим", self.mode)
        self.settings.endGroup()
    
    #калькулятор
    def calc(self):
        self.setWindowTitle("Калькулятор")
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        
        self.vbox = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        
        self.lb = QtWidgets.QLabel("0")
        self.le1 = QtWidgets.QLineEdit()
        self.le2 = QtWidgets.QLineEdit()
        self.vbox.addWidget(self.lb)
        self.vbox.addWidget(self.le1)
        self.vbox.addWidget(self.le2)
        
        self.btn1 = QtWidgets.QPushButton("+")
        self.btn2 = QtWidgets.QPushButton("-")
        self.btn3 = QtWidgets.QPushButton("*")
        self.btn4 = QtWidgets.QPushButton("/")
        self.btn5 = QtWidgets.QPushButton("Степень")
        self.btn6 = QtWidgets.QPushButton("Корень")
        self.btn7 = QtWidgets.QPushButton("Факториал")
        self.btn8 = QtWidgets.QPushButton("Рандомное число")
        
        self.btn1.clicked.connect(self.add)
        self.btn2.clicked.connect(self.sub)
        self.btn3.clicked.connect(self.mul)
        self.btn4.clicked.connect(self.div)
        self.btn5.clicked.connect(self.pow)
        self.btn6.clicked.connect(self.sqrt)
        self.btn7.clicked.connect(self.fact)
        self.btn8.clicked.connect(self.rand)
        
        self.grid.addWidget(self.btn1, 0, 0)
        self.grid.addWidget(self.btn2, 0, 1)
        self.grid.addWidget(self.btn3, 1, 0)
        self.grid.addWidget(self.btn4, 1, 1)
        self.grid.addWidget(self.btn5, 2, 0)
        self.grid.addWidget(self.btn6, 2, 1)
        self.grid.addWidget(self.btn7, 3, 0)
        self.grid.addWidget(self.btn8, 3, 1)
        self.vbox.addLayout(self.grid)
        
        wid.setLayout(self.vbox)
        
        self.mode = "calc"
    
    #Перевод в системы счисления из десятичной
    def code(self):
        self.setWindowTitle("Перевод из десятичной")
        self.vbox = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        
        self.lb = QtWidgets.QLabel("0")
        self.le = QtWidgets.QLineEdit()
        self.btnn = QtWidgets.QPushButton("Перевести")
        self.btnn.clicked.connect(self.translate)

        self.rb = QtWidgets.QRadioButton("Из двоичной")
        self.rb2 = QtWidgets.QRadioButton("Из восьмеричной")
        self.rb3 = QtWidgets.QRadioButton("Из десятичной")
        self.rb4 = QtWidgets.QRadioButton("Из шестнадцатеричной")

        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.addButton(self.rb)
        self.button_group.addButton(self.rb2)
        self.button_group.addButton(self.rb3)
        self.button_group.addButton(self.rb4)

        self.rbb = QtWidgets.QRadioButton("В двоичную")
        self.rbb2 = QtWidgets.QRadioButton("В восьмеричную")
        self.rbb3 = QtWidgets.QRadioButton("В десятичную")
        self.rbb4 = QtWidgets.QRadioButton("В шестнадцатеричную")

        self.vbox.addWidget(self.lb)
        self.vbox.addWidget(self.le)
        self.grid.addWidget(self.rb, 0, 0)
        self.grid.addWidget(self.rb2, 1, 0)
        self.grid.addWidget(self.rb3, 2, 0)
        self.grid.addWidget(self.rb4, 3, 0)
        
        self.grid.addWidget(self.rbb, 0, 1)
        self.grid.addWidget(self.rbb2, 1, 1)
        self.grid.addWidget(self.rbb3, 2, 1)
        self.grid.addWidget(self.rbb4, 3, 1)

        self.vbox.addLayout(self.grid)
        self.vbox.addWidget(self.btnn)
        wid.setLayout(self.vbox)
        
        if self.rb.isChecked:
            self.inn = 2
        elif self.rb2.isChecked:
            self.inn = 8
        elif self.rb3.isChecked:
            self.inn = 10
        elif self.rb4.isChecked:
            self.inn = 16

        if self.rbb.isChecked:
            self.out = 2
        elif self.rbb2.isChecked:
            self.out = 8
        elif self.rbb3.isChecked:
            self.out = 10
        elif self.rbb4.isChecked:
            self.out = 16

        self.mode = "code"
        
    def add(self):
        res = float(self.le1.text()) + float(self.le2.text())
        self.lb.setText(str(res))
    
    def sub(self):
        res = float(self.le1.text()) - float(self.le2.text())
        self.lb.setText(str(res))
    
    def mul(self):
        res = float(self.le1.text()) * float(self.le2.text())
        self.lb.setText(str(res))
    
    def div(self):
        try:
            res = float(self.le1.text()) / float(self.le2.text())
            self.lb.setText(str(res))
        except ZeroDivisionError:
            self.lb.setText("Нельзя делить на ноль")
    
    def pow(self):
        res = pow(float(self.le1.text()), float(self.le2.text()))
        self.lb.setText(str(res))
    
    def sqrt(self):
        res = math.sqrt(float(self.le1.text()))
        self.lb.setText(str(res))
    
    def fact(self):
        res = math.factorial(int(self.le1.text()))
        self.lb.setText(str(res))
    
    def rand(self):
        res = random.randint(int(self.le1.text()), int(self.le2.text()))
        self.lb.setText(str(res))
    
    def trans(self, num, base):
        alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b = alpha[num % base] 
        while num >= base :
            num = num // base
            b += alpha[num % base] 
        return b[::-1] 

    def translate(self):
        if self.rb.isChecked():
            inn = 2
        elif self.rb2.isChecked():
            inn = 8
        elif self.rb3.isChecked():
            inn = 10
        elif self.rb4.isChecked():
            inn = 16

        if self.rbb.isChecked():
            out = 2
        elif self.rbb2.isChecked():
            out = 8
        elif self.rbb3.isChecked():
            out = 10
        elif self.rbb4.isChecked():
            out = 16
        
        number = self.le.text()
        a = int(number, inn)
        a = self.trans(a, out)

        self.lb.setText(str(a))


if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    