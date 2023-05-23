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
        menuBar = QtWidgets.QMenuBar()
        calcMenu = QtWidgets.QMenu("Mode", self)
        menuBar.addMenu(calcMenu)
        
    def _createActions(self):
        pass
        
    def CalcAction(self):
        print(123)
        
    def closeEvent(self, event):
        self.settings.beginGroup("Окно")
        self.settings.setValue("Местоположение", self.geometry())
        self.settings.endGroup()

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    