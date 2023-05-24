from PyQt5 import QtGui, QtWidgets, QtCore
import math
import random

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Калькулятор")
        self.setWindowIcon(QtGui.QIcon("calc.png"))
        self.settings = QtCore.QSettings("Настройки", "Мульти_калькулятор")
        
        self.calc()
        
        if self.settings.contains("Окно/Местоположение"):
            self.setGeometry(self.settings.value("Окно/Местоположение"))
        else:
            self.resize(200, 100)
            
        if self.settings.contains("Режимы/Режим"):
            if self.settings.value("Режимы/Режим") == "calc":
                self.calc()
            elif self.settings.value("Режимы/Режим") == "code":
                self.code()
        
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
        self.btn7 = QtWidgets.QPushButton("Рандомное число")
        
        self.btn1.clicked.connect(self.add)
        self.btn2.clicked.connect(self.sub)
        self.btn3.clicked.connect(self.mul)
        self.btn4.clicked.connect(self.div)
        self.btn5.clicked.connect(self.pow)
        self.btn6.clicked.connect(self.sqrt)
        self.btn7.clicked.connect(self.rand)
        
        self.grid.addWidget(self.btn1, 0, 0)
        self.grid.addWidget(self.btn2, 0, 1)
        self.grid.addWidget(self.btn3, 1, 0)
        self.grid.addWidget(self.btn4, 1, 1)
        self.grid.addWidget(self.btn5, 2, 0)
        self.grid.addWidget(self.btn6, 2, 1)
        self.vbox.addLayout(self.grid)
        
        self.vbox.addWidget(self.btn7)
        wid.setLayout(self.vbox)
        
        self.mode = "calc"
        print(self.mode)
    
    #Перевод в системы счисления
    def code(self):
        self.vbox = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        
        self.lb = QtWidgets.QLabel("0")
        #self.lb.setAlignment(QtCore.Qt.AlignTop)
        self.le = QtWidgets.QLineEdit()
        self.vbox.addWidget(self.lb)
        self.vbox.addWidget(self.le)
        
        self.btn1 = QtWidgets.QPushButton("Двоичная")
        self.btn2 = QtWidgets.QPushButton("Восьмеричная")
        self.btn3 = QtWidgets.QPushButton("Шестнадцатеричная")
        
        self.btn1.clicked.connect(self.bin)
        self.btn2.clicked.connect(self.oct)
        self.btn3.clicked.connect(self.hex)
        
        self.grid.addWidget(self.btn1, 0, 0)
        self.grid.addWidget(self.btn2, 0, 1)
        
        self.vbox.addLayout(self.grid)
        self.vbox.addWidget(self.btn3)
        wid.setLayout(self.vbox)
        
        self.mode = "code"
        print(self.mode)
        
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
    
    def rand(self):
        res = random.randint(int(self.le1.text()), int(self.le2.text()))
        self.lb.setText(str(res))
    
    def bin(self):
        res = bin(int(self.le.text()))
        self.lb.setText(str(res))
        
    def oct(self):
        res = oct(int(self.le.text()))
        self.lb.setText(str(res))
    
    def hex(self):
        res = hex(int(self.le.text()))
        self.lb.setText(str(res))

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    