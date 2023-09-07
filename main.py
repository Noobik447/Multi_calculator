from PyQt5 import QtWidgets, QtCore, QtGui
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
            elif self.settings.value("Режимы/Режим") == "weight":
                self.weight()
            elif self.settings.value("Режимы/Режим") == "time":
                self.time()
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
        calcMenu.addAction(self.weightAction)
        calcMenu.addAction(self.timeAction)
        
    def _createActions(self):
        self.calcAction = QtWidgets.QAction("Калькулятор", self)
        self.calcAction.triggered.connect(self.calc)
        self.codeAction = QtWidgets.QAction("Системы счисления", self)
        self.codeAction.triggered.connect(self.code)
        self.tempAction = QtWidgets.QAction("Температура", self)
        self.tempAction.triggered.connect(self.temp)
        self.lengthAction = QtWidgets.QAction("Длина", self)
        self.lengthAction.triggered.connect(self.length)
        self.weightAction = QtWidgets.QAction("Масса", self)
        self.weightAction.triggered.connect(self.weight)
        self.timeAction = QtWidgets.QAction("Время", self)
        self.timeAction.triggered.connect(self.time)
        
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

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Enter"), self)
        self.shortcut.activated.connect(self.translate)

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

    def weight(self):
        self.setWindowTitle("Масса")
        self.vbox = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        
        self.lb = QtWidgets.QLabel("0")
        self.le = QtWidgets.QLineEdit()
        self.btn = QtWidgets.QPushButton("Перевести")
        self.btn.clicked.connect(self.translate_weight)

        self.rb = QtWidgets.QRadioButton("Из миллиграмм")
        self.rb2 = QtWidgets.QRadioButton("Из грамм")
        self.rb3 = QtWidgets.QRadioButton("Из килограмм")

        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.addButton(self.rb)
        self.button_group.addButton(self.rb2)
        self.button_group.addButton(self.rb3)

        self.rbb = QtWidgets.QRadioButton("В миллиграммы")
        self.rbb2 = QtWidgets.QRadioButton("В граммы")
        self.rbb3 = QtWidgets.QRadioButton("В килограммы")

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

        self.mode = "weight"
        
    def time(self):
        self.setWindowTitle("Время")
        self.vbox = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)

        self.lb = QtWidgets.QLabel("0")
        self.le = QtWidgets.QLineEdit()
        self.btn = QtWidgets.QPushButton("Перевести")
        self.btn.clicked.connect(self.translate_time)

        self.rb = QtWidgets.QRadioButton("Из миллисекунд")
        self.rb2 = QtWidgets.QRadioButton("Из секунд")
        self.rb3 = QtWidgets.QRadioButton("Из минут")
        self.rb4 = QtWidgets.QRadioButton("Из часов")
        self.rb5 = QtWidgets.QRadioButton("Из дней")
        self.rb6 = QtWidgets.QRadioButton("Из недель")
        self.rb7 = QtWidgets.QRadioButton("Из месяцев")
        self.rb8 = QtWidgets.QRadioButton("Из лет")

        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.addButton(self.rb)
        self.button_group.addButton(self.rb2)
        self.button_group.addButton(self.rb3)
        self.button_group.addButton(self.rb4)
        self.button_group.addButton(self.rb5)
        self.button_group.addButton(self.rb6)
        self.button_group.addButton(self.rb7)
        self.button_group.addButton(self.rb8)

        self.rbb = QtWidgets.QRadioButton("В миллисекунды")
        self.rbb2 = QtWidgets.QRadioButton("В секунды")
        self.rbb3 = QtWidgets.QRadioButton("В минуты")
        self.rbb4 = QtWidgets.QRadioButton("В часы")
        self.rbb5 = QtWidgets.QRadioButton("В дни")
        self.rbb6 = QtWidgets.QRadioButton("В недели")
        self.rbb7 = QtWidgets.QRadioButton("В месяца")
        self.rbb8 = QtWidgets.QRadioButton("В года")

        self.vbox.addWidget(self.lb)
        self.vbox.addWidget(self.le)

        self.grid.addWidget(self.rb, 0, 0)
        self.grid.addWidget(self.rb2, 1, 0)
        self.grid.addWidget(self.rb3, 2, 0)
        self.grid.addWidget(self.rb4, 3, 0)
        self.grid.addWidget(self.rb5, 4, 0)
        self.grid.addWidget(self.rb6, 5, 0)
        self.grid.addWidget(self.rb7, 6, 0)
        self.grid.addWidget(self.rb8, 7, 0)

        self.grid.addWidget(self.rbb, 0, 1)
        self.grid.addWidget(self.rbb2, 1, 1)
        self.grid.addWidget(self.rbb3, 2, 1)
        self.grid.addWidget(self.rbb4, 3, 1)
        self.grid.addWidget(self.rbb5, 4, 1)
        self.grid.addWidget(self.rbb6, 5, 1)
        self.grid.addWidget(self.rbb7, 6, 1)
        self.grid.addWidget(self.rbb8, 7, 1)

        self.vbox.addLayout(self.grid)
        self.vbox.addWidget(self.btn)
        wid.setLayout(self.vbox)

        self.mode = "time"

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
        #Километры
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
        mil = float(metr) * 1000
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

    def translate_weight(self):
        #Миллиграмм
        if self.rb.isChecked():
            inn = 1
        #Грамм
        elif self.rb2.isChecked():
            inn = 2
        #Килограмм
        elif self.rb3.isChecked():
            inn = 3

        #Миллиграмм
        if self.rbb.isChecked():
            out = 1
        #Грамм
        elif self.rbb2.isChecked():
            out = 2
        #Килограмм
        elif self.rbb3.isChecked():
            out = 3

        if inn == 1:
            if out == 2:
                converted_weight = self.milligram_to_gram(self.le.text())
            elif out == 3:
                converted_weight = self.milligram_to_kilogram(self.le.text())
        elif inn == 2:
            if out == 1:
                converted_weight = self.gram_to_milligram(self.le.text())
            elif out == 3:
                converted_weight = self.gram_to_kilogram(self.le.text())
        elif inn == 3:
            if out == 1:
                converted_weight = self.kilogram_to_milligram(self.le.text())
            elif out == 2:
                converted_weight = self.kilogram_to_gram(self.le.text())

        if inn == out:
            converted_weight = self.le.text()

        self.lb.setText(str(converted_weight))
        
    #Миллиграммы в граммы
    def milligram_to_gram(self, milligram):
        gram = float(milligram) / 1000
        return gram

    #Миллиграммы в килограммы
    def milligram_to_kilogram(self, milligram):
        kilogram = float(milligram) / 1000000
        return kilogram

    #Граммы в миллиграммы
    def gram_to_milligram(self, gram):
        milligram = float(gram) * 1000
        return milligram

    #Граммы в килограммы
    def gram_to_kilogram(self, gram):
        kilogram = float(gram) / 1000
        return kilogram
    
    #Килограмм в миллиграмм
    def kilogram_to_milligram(self, kilogram):
        milligram = float(kilogram) * 1000000
        return milligram
    
    #Килограмм в миллиграмм
    def kilogram_to_gram(self, kilogram):
        gram = float(kilogram) * 1000
        return gram

    def translate_time(self):
        #Миллисекунды
        if self.rb.isChecked():
            inn = 1
        #Секунды
        elif self.rb2.isChecked():
            inn = 2
        #Минуты
        elif self.rb3.isChecked():
            inn = 3
        #Часы
        elif self.rb4.isChecked():
            inn = 4
        #Дни
        elif self.rb5.isChecked():
            inn = 5
        #Недели
        elif self.rb6.isChecked():
            inn = 6
        #Месяцы
        elif self.rb7.isChecked():
            inn = 7
        #Года
        elif self.rb8.isChecked():
            inn = 8


        #Миллисекунды
        if self.rbb.isChecked():
            out = 1
        #секунды
        elif self.rbb2.isChecked():
            out = 2
        #Минуты
        elif self.rbb3.isChecked():
            out = 3
        #Часы
        elif self.rbb4.isChecked():
            out = 4
        #Дни
        elif self.rbb5.isChecked():
            out = 5
        #Недели
        elif self.rbb6.isChecked():
            out = 6
        #Месяцы
        elif self.rbb7.isChecked():
            out = 7
        elif self.rbb8.isChecked():
            out = 8

        if inn == 1:
            if out == 2:
                converted_time = self.milliseconds_to_seconds(self.le.text())
            elif out == 3:
                converted_time = self.milliseconds_to_minutes(self.le.text())
            elif out == 4:
                converted_time = self.milliseconds_to_hours(self.le.text())
            elif out == 5:
                converted_time = self.milliseconds_to_days(self.le.text())
            elif out == 6:
                converted_time = self.milliseconds_to_weeks(self.le.text())
            elif out == 7:
                converted_time = self.milliseconds_to_months(self.le.text())
            elif out == 8:
                converted_time = self.milliseconds_to_years(self.le.text())
        elif inn == 2:
            if out == 1:
                converted_time = self.seconds_to_milliseconds(self.le.text())
            elif out == 3:
                converted_time = self.seconds_to_minutes(self.le.text())
            elif out == 4:
                converted_time = self.seconds_to_hours(self.le.text())
            elif out == 5:
                converted_time = self.seconds_to_days(self.le.text())
            elif out == 6:
                converted_time = self.seconds_to_weeks(self.le.text())
            elif out == 7:
                converted_time = self.seconds_to_months(self.le.text())
            elif out == 8:
                converted_time = self.seconds_to_years(self.le.text())
        elif inn == 3:
            if out == 1:
                converted_time = self.minutes_to_milliseconds(self.le.text())
            elif out == 2:
                converted_time = self.minutes_to_seconds(self.le.text())
            elif out == 4:
                converted_time = self.minutes_to_hours(self.le.text())
            elif out == 5:
                converted_time = self.minutes_to_days(self.le.text())
            elif out == 6:
                converted_time = self.minutes_to_weeks(self.le.text())
            elif out == 7:
                converted_time = self.minutes_to_months(self.le.text())
            elif out == 8:
                converted_time = self.minutes_to_years(self.le.text())
        elif inn == 4:
            if out == 1:
                converted_time = self.hours_to_milliseconds(self.le.text())
            elif out == 2:
                converted_time = self.hours_to_seconds(self.le.text())
            elif out == 3:
                converted_time = self.hours_to_minutes(self.le.text())
            elif out == 5:
                converted_time = self.seconds_to_days(self.le.text())
            elif out == 6:
                converted_time = self.seconds_to_weeks(self.le.text())
            elif out == 7:
                converted_time = self.seconds_to_months(self.le.text())
            elif out == 8:
                converted_time = self.seconds_to_years(self.le.text())
        elif inn == 5:
            if out == 1:
                converted_time = self.days_to_milliseconds(self.le.text())
            elif out == 2:
                converted_time = self.days_to_seconds(self.le.text())
            elif out == 3:
                converted_time = self.days_to_minutes(self.le.text())
            elif out == 4:
                converted_time = self.days_to_hours(self.le.text())
            elif out == 6:
                converted_time = self.days_to_weeks(self.le.text())
            elif out == 7:
                converted_time = self.days_to_months(self.le.text())
            elif out == 8:
                converted_time = self.days_to_years(self.le.text())
        elif inn == 6:
            if out == 1:
                converted_time = self.weeks_to_milliseconds(self.le.text())
            elif out == 2:
                converted_time = self.weeks_to_seconds(self.le.text())
            elif out == 3:
                converted_time = self.weeks_to_minutes(self.le.text())
            elif out == 4:
                converted_time = self.weeks_to_hours(self.le.text())
            elif out == 5:
                converted_time = self.weeks_to_days(self.le.text())
            elif out == 7:
                converted_time = self.weeks_to_months(self.le.text())
            elif out == 8:
                converted_time = self.weeks_to_years(self.le.text())
        elif inn == 7:
            if out == 1:
                converted_time = self.months_to_milliseconds(self.le.text())
            elif out == 2:
                converted_time = self.months_to_seconds(self.le.text())
            elif out == 3:
                converted_time = self.months_to_minutes(self.le.text())
            elif out == 4:
                converted_time = self.months_to_hours(self.le.text())
            elif out == 5:
                converted_time = self.months_to_days(self.le.text())
            elif out == 6:
                converted_time = self.months_to_weeks(self.le.text())
            elif out == 8:
                converted_time = self.months_to_years(self.le.text())
        elif inn == 8:
            if out == 1:
                converted_time = self.years_to_milliseconds(self.le.text())
            elif out == 2:
                converted_time = self.years_to_seconds(self.le.text())
            elif out == 3:
                converted_time = self.years_to_minutes(self.le.text())
            elif out == 4:
                converted_time = self.years_to_hours(self.le.text())
            elif out == 5:
                converted_time = self.years_to_days(self.le.text())
            elif out == 6:
                converted_time = self.years_to_weeks(self.le.text())
            elif out == 7:
                converted_time = self.years_to_months(self.le.text())

        if inn == out:
            converted_time = self.le.text()

        self.lb.setText(str(converted_time))

    def milliseconds_to_seconds(self, milliseconds):
        seconds = float(milliseconds) / 1000
        return seconds

    def milliseconds_to_minutes(self, milliseconds):
        minutes = float(milliseconds) / 60000
        return minutes

    def milliseconds_to_hours(self, milliseconds):
        hours = float(milliseconds) / 3600000
        return hours

    def milliseconds_to_days(self, milliseconds):
        days = float(milliseconds) / 86400000
        return days

    def milliseconds_to_weeks(self, milliseconds):
        weeks = float(milliseconds) / 604800000
        return weeks

    def milliseconds_to_months(self, milliseconds):
        months = float(milliseconds) / 2592000000
        return months

    def milliseconds_to_years(self, milliseconds):
        years = float(milliseconds) / 31536000000
        return years

    def seconds_to_milliseconds(self, seconds):
        milliseconds = float(seconds) * 1000
        return milliseconds 

    def seconds_to_minutes(self, seconds):
        minutes = float(seconds) / 60
        return minutes

    def seconds_to_hours(self, seconds):
        hours = float(seconds) / 3600
        return hours
    
    def seconds_to_days(self, seconds):
        days = float(seconds) / 86400
        return days

    def seconds_to_weeks(self, seconds):
        weeks = float(seconds) / 604800
        return weeks
    
    def seconds_to_months(self, seconds):
        months = float(seconds) / 18144000
        return months

    def seconds_to_years(self, seconds):
        years = float(seconds) / 217728000
        return years

    def minutes_to_milliseconds(self, minutes):
        milliseconds = float(minutes) * 6000
        return milliseconds

    def minutes_to_seconds(self, minutes):
        seconds = float(minutes) * 60
        return seconds

    def minutes_to_hours(self, minutes):
        hours = float(minutes) / 60
        return hours
    
    def minutes_to_days(self, minutes):
        days = float(minutes) / 1440
        return days

    def minutes_to_weeks(self, minutes):
        weeks = float(minutes) / 10080
        return weeks
    
    def minutes_to_months(self, minutes):
        months = float(minutes) / 302400
        return months
    
    def minutes_to_years(self, minutes):
        years = float(minutes) / 3628800
        return years

    def hours_to_milliseconds(self, hours):
        milliseconds = float(hours) * 3600000
        return milliseconds

    def hours_to_seconds(self, hours):
        seconds = float(hours) * 3600
        return seconds

    def hours_to_minutes(self, hours):
        minutes = float(hours) * 60
        return minutes

    def hours_to_days(self, hours):
        days = float(hours) / 24
        return days

    def hours_to_weeks(self, hours):
        weeks = float(hours) / 168
        return weeks

    def hours_to_months(self, hours):
        months = float(hours) / 5040
        return months

    def hours_to_years(self, hours):
        years = float(hours) / 60480
        return years

    def days_to_milliseconds(self, days):
        milliseconds = float(days) * 864000000
        return milliseconds
    
    def days_to_seconds(self, days):
        seconds = float(days) * 86400
        return seconds

    def days_to_minutes(self, days):
        minutes = float(days) * 1440
        return minutes

    def days_to_hours(self, days):
        hours = float(days) * 24
        return hours

    def days_to_weeks(self, days):
        weeks = float(days) / 7
        return weeks

    def days_to_months(self, days):
        months = float(days) / 30
        return months

    def days_to_years(self, days):
        years = float(days) / 365
        return years
    
    def weeks_to_milliseconds(self, weeks):
        milliseconds = float(weeks) * 604800000
        return milliseconds
    
    def weeks_to_seconds(self, weeks):
        seconds = float(weeks) * 604800
        return seconds

    def weeks_to_minutes(self, weeks):
        minutes = float(weeks) * 10080
        return minutes
    
    def weeks_to_hours(self, weeks):
        hours = float(weeks) * 168
        return hours

    def weeks_to_days(self, weeks):
        days = float(weeks) * 7
        return days

    def weeks_to_months(self, weeks):
        months = float(weeks) / 30
        return months

    def weeks_to_years(self, weeks):
        years = float(weeks) / 52.25
        return years

    def months_to_milliseconds(self, months):
        milliseconds = float(months) * 2592000000
        return milliseconds

    def months_to_seconds(self, months):
        seconds = float(months) * 18144000
        return seconds

    def months_to_minutes(self, months):
        minutes = float(months) * 302400
        return minutes

    def months_to_hours(self, months):
        hours = float(months) * 5040
        return hours

    def months_to_days(self, months):
        days = float(months) * 30
        return days

    def months_to_weeks(self, months):
        weeks = float(months) * 4
        return weeks

    def months_to_years(self, months):
        years = float(months) / 12
        return years

    def years_to_milliseconds(self, years):
        milliseconds = float(years) * 31536000000
        return milliseconds

    def years_to_seconds(self, years):
        seconds = float(years) * 217728000
        return seconds

    def years_to_minutes(self, years):
        minutes = float(years) * 3628800
        return minutes

    def years_to_hours(self, years):
        hours = float(years) * 60480
        return hours

    def years_to_days(self, years):
        days = float(years) * 365
        return days

    def years_to_weeks(self, years):
        weeks = float(years) * 52.25
        return weeks
    
    def years_to_months(self, years):
        months = float(years) * 12
        return months


if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
