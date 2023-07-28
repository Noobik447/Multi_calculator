from PyQt5 import QtWidgets, QtCore
import math
import random

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
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
            elif self.settings.value("Режимы/Режим") == "temp":
                self.temp()
            elif self.settings.value("Режимы/Режим") == "length":
                self.length()
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
        calcMenu.addAction(self.tempAction)
        calcMenu.addAction(self.lengthAction)
        
    def _createActions(self):
        self.calcAction = QtWidgets.QAction("Калькулятор", self)
        self.calcAction.triggered.connect(self.calc)
        self.codeAction = QtWidgets.QAction("Системы счисления", self)
        self.codeAction.triggered.connect(self.code)
        self.tempAction = QtWidgets.QAction("Температура", self)
        self.tempAction.triggered.connect(self.temp)
        self.lengthAction = QtWidgets.QAction("Длина", self)
        self.lengthAction.triggered.connect(self.length)
        
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
        self.setWindowTitle("Перевод в системы счисления")
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
    
    def temp(self):
        self.setWindowTitle("Температура")
        self.vbox = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        
        self.lb = QtWidgets.QLabel("0")
        self.le = QtWidgets.QLineEdit()
        self.btn = QtWidgets.QPushButton("Перевести")
        self.btn.clicked.connect(self.translate_temp)

        self.rb = QtWidgets.QRadioButton("Из Цельсия")
        self.rb2 = QtWidgets.QRadioButton("Из Фарангейта")
        self.rb3 = QtWidgets.QRadioButton("Из Кельвинов")

        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.addButton(self.rb)
        self.button_group.addButton(self.rb2)
        self.button_group.addButton(self.rb3)

        self.rbb = QtWidgets.QRadioButton("В Цельсии")
        self.rbb2 = QtWidgets.QRadioButton("В Фарангейты")
        self.rbb3 = QtWidgets.QRadioButton("В Кельвины")

        self.vbox.addWidget(self.lb)
        self.vbox.addWidget(self.le)
        self.grid.addWidget(self.rb, 0, 0)
        self.grid.addWidget(self.rb2, 1, 0)
        self.grid.addWidget(self.rb3, 2, 0)
        
        self.grid.addWidget(self.rbb, 0, 1)
        self.grid.addWidget(self.rbb2, 1, 1)
        self.grid.addWidget(self.rbb3, 2, 1)

        self.vbox.addLayout(self.grid)
        self.vbox.addWidget(self.btn)
        wid.setLayout(self.vbox)

        self.mode = "temp"

    def length(self):
        self.setWindowTitle("Длина")
        self.vbox = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        
        self.lb = QtWidgets.QLabel("0")
        self.le = QtWidgets.QLineEdit()
        self.btn = QtWidgets.QPushButton("Перевести")
        self.btn.clicked.connect(self.translate_length)

        self.rb = QtWidgets.QRadioButton("Из миллиметров")
        self.rb2 = QtWidgets.QRadioButton("Из сантиметров")
        self.rb3 = QtWidgets.QRadioButton("Из метров")
        self.rb4 = QtWidgets.QRadioButton("Из километров")

        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.addButton(self.rb)
        self.button_group.addButton(self.rb2)
        self.button_group.addButton(self.rb3)
        self.button_group.addButton(self.rb4)

        self.rbb = QtWidgets.QRadioButton("В миллиметры")
        self.rbb2 = QtWidgets.QRadioButton("В сантиметры")
        self.rbb3 = QtWidgets.QRadioButton("В метры")
        self.rbb4 = QtWidgets.QRadioButton("В километры")

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
        self.vbox.addWidget(self.btn)
        wid.setLayout(self.vbox)

        self.mode = "length"
        
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
        #Двоичная
        if self.rb.isChecked():
            inn = 2
        #Восьмеричная
        elif self.rb2.isChecked():
            inn = 8
        #Десятичная
        elif self.rb3.isChecked():
            inn = 10
        #Шестнадцатеричная
        elif self.rb4.isChecked():
            inn = 16

        #Двоичная
        if self.rbb.isChecked():
            out = 2
        #Восьмеричная
        elif self.rbb2.isChecked():
            out = 8
        #Десятичная
        elif self.rbb3.isChecked():
            out = 10
        #Шестнадцатеричная
        elif self.rbb4.isChecked():
            out = 16
        
        number = self.le.text()
        a = int(number, inn)
        a = self.trans(a, out)

        self.lb.setText(str(a))

    def translate_temp(self):
        #Цельсии
        if self.rb.isChecked():
            inn = 1
        #Фарангейты
        elif self.rb2.isChecked():
            inn = 2
        #Кельвины
        elif self.rb3.isChecked():
            inn = 3

        #Цельсии
        if self.rbb.isChecked():
            out = 1
        #Фарангейты
        elif self.rbb2.isChecked():
            out = 2
        #Кельвины
        elif self.rbb3.isChecked():
            out = 3

        temp = self.le.text()

        if inn == 1:
            if out == 2:
                converted_temp = self.celsius_to_fahrenheit(temp)
            elif out == 3:
                converted_temp = self.celsius_to_kelvin(temp)
        elif inn == 2:
            if out == 1:
                converted_temp = self.fahrenheit_to_celsius(temp)
            elif out == 3:
                converted_temp = self.fahrenheit_to_kelvin(temp)
        elif inn == 3:
            if out == 1:
                converted_temp = self.kelvin_to_celsius(temp)
            elif out == 2:
                converted_temp = self.kelvin_to_fahrenheit(temp)  

        if inn == out:
            converted_temp = self.le.text()

        self.lb.setText(str(converted_temp))

    def celsius_to_fahrenheit(self, celsius):
        fahrenheit = (float(celsius) * 9/5) + 32
        return fahrenheit

    def celsius_to_kelvin(self, celsius):
        kelvin = float(celsius) + 273.15
        return kelvin

    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (float(fahrenheit) - 32) * 5/9
        return celsius

    def fahrenheit_to_kelvin(self, fahrenheit):
        kelvin = (float(fahrenheit) - 32) * 5/9 + 273.15
        return kelvin

    def kelvin_to_celsius(self, kelvin):
        celsius = float(kelvin) - 273.15
        return celsius

    def kelvin_to_fahrenheit(self, kelvin):
        fahrenheit = (float(kelvin) - 273.15) * 9/5 + 32
        return fahrenheit

    def translate_length(self):
        #Миллиметры
        if self.rb.isChecked():
            inn = 1
        #Сантиметры
        elif self.rb2.isChecked():
            inn = 2
        #Метры
        elif self.rb3.isChecked():
            inn = 3
        elif self.rb4.isChecked():
            inn = 4

        #Милиметры
        if self.rbb.isChecked():
            out = 1
        #Сантиметры
        elif self.rbb2.isChecked():
            out = 2
        #Метры
        elif self.rbb3.isChecked():
            out = 3
        #Километры
        elif self.rbb4.isChecked():
            out = 4

        if inn == 1:
            if out == 2:
                converted_length = self.mil_to_san(self.le.text())
            elif out == 3:
                converted_length = self.mil_to_metr(self.le.text())
            elif out == 4:
                converted_length = self.mil_to_kil(self.le.text())
        elif inn == 2:
            if out == 1:
                converted_length = self.san_to_mil(self.le.text())
            elif out == 3:
                converted_length = self.san_to_metr(self.le.text())
            elif out == 4:
                converted_length = self.san_to_kil(self.le.text())
        elif inn == 3:
            if out == 1:
                converted_length = self.metr_to_mil(self.le.text())
            elif out == 2:
                converted_length = self.metr_to_san(self.le.text())
            elif out == 4:
                converted_length = self.metr_to_kil(self.le.text())
        elif inn == 4:
            if out == 1:
                converted_length = self.kil_to_mil(self.le.text())
            elif out == 2:
                converted_length = self.kil_to_san(self.le.text())
            elif out == 3:
                converted_length = self.kil_to_metr(self.le.text())

        if inn == out:
            converted_length = self.le.text()

        self.lb.setText(str(converted_length))

    #миллиметры в сантиметры   
    def mil_to_san(self, mil):
        san = float(mil) / 10
        return san
    
    #миллиметры в метры
    def mil_to_metr(self, mil):
        metr = float(mil) / 1000
        return metr
    
    #миллиметры в километры
    def mil_to_kil(self, mil):
        kil = float(mil) / 1000000
        return kil
    
    #Сантиметры в миллиметры
    def san_to_mil(self, san):
        mil = float(san) * 10
        return mil
    
    #Сантиметры в метры
    def san_to_metr(self, san):
        metr = float(san) / 100
        return metr
    
    #Сантиметры в километры
    def san_to_kil(self, san):
        kil = float(san) / 100000
        return kil

    #Метры в миллиметры
    def metr_to_mil(self, metr):
        mil = float(metr) / 1000
        return mil
    
    #Метры в сантиметры
    def metr_to_san(self, metr):
        san = float(metr) * 100
        return san
    
    #Метры в километры
    def metr_to_kil(self, metr):
        kil = float(metr) / 1000
        return kil

    #Километры в миллиметры
    def kil_to_mil(self, kil):
        mil = float(kil) * 1000000
        return mil
    
    #Километры в сантиметры
    def kil_to_san(self, kil):
        san = float(kil) * 100000
        return san
    
    #Километры в метры
    def kil_to_metr(self, kil):
        metr = float(kil) * 1000
        return metr


if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
