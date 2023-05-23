from PyQt5 import QtGui, QtWidgets, QtCore


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Калькулятор")
        self.settings = QtCore.QSettings("Настройки", "Расположение")
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        
        self.vbox = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        
        self.lb = QtWidgets.QLabel()
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
        
        if self.settings.contains("Окно/Местоположение"):
            self.setGeometry(self.settings.value("Окно/Местоположение"))
        else:
            self.resize(200, 50)
        
        self._createActions()
        self._createMenuBar()
        
    def _createMenuBar(self):
        menuBar = self.menuBar()
        calcMenu = QtWidgets.QMenu("Mode", self)
        menuBar.addMenu(calcMenu)
        calcMenu.addAction(self.calcAction)
        calcMenu.addAction(self.codeAction)
        
        
    def _createActions(self):
        self.calcAction = QtWidgets.QAction("Калькулятор", self)
        self.calcAction.triggered.connect(self.calc)
        self.codeAction = QtWidgets.QAction("Системы счисления", self)
        self.codeAction.triggered.connect(self.code)
        
    def CalcAction(self):
        print(123)
        
    def closeEvent(self, event):
        self.settings.beginGroup("Окно")
        self.settings.setValue("Местоположение", self.geometry())
        self.settings.endGroup()
        
    def calc(self):
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        
        self.vbox = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        
        self.lb = QtWidgets.QLabel()
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
        
        self.grid.addWidget(self.btn1, 0, 0)
        self.grid.addWidget(self.btn2, 0, 1)
        self.grid.addWidget(self.btn3, 1, 0)
        self.grid.addWidget(self.btn4, 1, 1)
        self.grid.addWidget(self.btn5, 2, 0)
        self.grid.addWidget(self.btn6, 2, 1)
        self.vbox.addLayout(self.grid)
        
        self.vbox.addWidget(self.btn7)
        wid.setLayout(self.vbox)
    
    def code(self):
        self.vbox = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        
        self.lb = QtWidgets.QLabel()
        self.le = QtWidgets.QLineEdit()
        self.vbox.addWidget(self.lb)
        self.vbox.addWidget(self.le)
        
        self.btn1 = QtWidgets.QPushButton("Двоичная")
        self.btn2 = QtWidgets.QPushButton("Восьмеричная")
        self.btn3 = QtWidgets.QPushButton("Десятеричная")
        self.btn4 = QtWidgets.QPushButton("Шестнадцатеричная")
        
        self.btn1.clicked.connect(self.bin)
        self.btn2.clicked.connect(self.oct)
        self.btn3.clicked.connect(self.dec)
        self.btn4.clicked.connect(self.hex)
        
        self.grid.addWidget(self.btn1, 0, 0)
        self.grid.addWidget(self.btn2, 0, 1)
        self.grid.addWidget(self.btn3, 1, 0)
        self.grid.addWidget(self.btn4, 1, 1)
        
        self.vbox.addLayout(self.grid)
        wid.setLayout(self.vbox)
        
    def add(self):
        pass
    
    def sub(self):
        pass
    
    def mul(self):
        pass
    
    def div(self):
        pass
    
    def pow(self):
        pass
    
    def sqrt(self):
        pass
    
    def rand(self):
        pass
    
    def bin(self):
        pass
    
    def oct(self):
        pass
    
    def dec(self):
        pass
    
    def hex(self):
        pass

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    