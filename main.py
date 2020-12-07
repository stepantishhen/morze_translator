import winsound  # https://docs.python.org/2/library/winsound.html
import time
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class SenderWindowUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(850, 450))
        MainWindow.setMaximumSize(QtCore.QSize(850, 450))
        MainWindow.setSizeIncrement(QtCore.QSize(850, 450))
        MainWindow.setBaseSize(QtCore.QSize(799, 450))
        MainWindow.setWindowIcon(QIcon('translating.png'))
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(22, 40, 481, 341))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.label)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit.setStyleSheet("background-color: white; border-radius: "
                                    "15px; border: 2px solid rgb(255, 106, "
                                    "106); padding: 10px;")
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole,
                                  self.textEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.label_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_2.setStyleSheet("background-color: white; "
                                      "border-radius: 15px; border: 2px "
                                      "solid rgb(255, 106, 106);  padding: "
                                      "10px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole,
                                  self.textEdit_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.LabelRole,
                                  self.gridLayout)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 751, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 230, 301, 148))
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgb(255, 106, 106) ; "
                                   "border-radius: 15px; padding: 5px;\n "
                                   "color: white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 50, 301, 148))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(
            "background-color:rgb(255, 106, 106) ; border-radius: 15px; "
            "padding: 5px;\n "
            "color: white;")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 390, 141, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 106, 106);\n"
                                      "color: white;")
        self.pushButton.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 390, 141, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 106, 106);\n"
            "color: white;")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Отправитель"))
        self.label.setText(_translate("MainWindow", "Обычный текст:"))
        self.label_2.setText(_translate("MainWindow", "Морзянка:"))
        self.label_7.setText(_translate("MainWindow", "Окно отправителя"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p "
                                        "align=\"center\">Здесь отображенно "
                                        "</p><p "
                                        "align=\"center\">переведённое "
                                        "сообщение</p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p "
                                        "align=\"center\">Вводите любое "
                                        "сообщение с использованием</p><p "
                                        "align=\"center\">цифр и символов "
                                        "русского алфавита</p><p "
                                        "align=\"center\">Можно передавать "
                                        "несколько сообщений</p><p "
                                        "align=\"center\">через перевод "
                                        "строки</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Перевести в звук"))
        self.pushButton_2.setText(_translate("MainWindow", "Транслировать"))


class SenderWindow(QMainWindow, SenderWindowUi):  # Основное окно программы
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Загружаем интерфейс программы
        # Алфавит Азбуки Морзе
        self.alphabet = {'А': '·-', 'Б': '-···', 'В': '·--', 'Г': '--·',
                         'Д': '-··', 'Е': '·', 'Ё': '·', 'Ж': '···-',
                         'З': '--··', 'И': '··', 'Й': '·---', 'К': '-·-',
                         'Л': '·-··', 'М': '--', 'Н': '-·', 'О': '---',
                         'П': '·--·', 'Р': '·-·', 'С': '···', 'Т': '-',
                         'У': '··-', 'Ф': '··-·', 'Х': '····', 'Ц': '-·-·',
                         'Ч': '---·', 'Ш': '----', 'Щ': '--·-', 'Ъ': '--·--',
                         'Ы': '-·--', 'Ь': '-··-', 'Э': '··-··', 'Ю': '··--',
                         'Я': '·-·-',
                         '0': '-----', '1': '·----', '2': '··---',
                         '3': '···--', '4': '····-', '5': '·····',
                         '6': '-····', '7': '--···', '8': '---··',
                         '9': '----·'}
        # Подключаем кнопки
        self.pushButton.clicked.connect(self.signaling)
        self.pushButton_2.clicked.connect(self.conclusion)

    def translate(self, text):  # Перевод текста в морзянку
        messages = ''
        for line in text.split('\n'):
            for s in line:
                if s.isalpha() or s.isnumeric():
                    messages += self.alphabet[s.upper()] + ' '
                if s == ' ':
                    messages += '  '
            messages = messages.rstrip(' ') + '\n'
        messages = messages.rstrip('\n')
        return messages

    def conclusion(self):  # Отображения морзянки во втором TextEdit
        text = self.textEdit.toPlainText()
        self.textEdit_2.clear()
        try:
            self.textEdit_2.insertPlainText(self.translate(text))
        except KeyError:
            self.textEdit_2.insertPlainText('Неверный ввод символов, '
                                            'выполняйте сторого по образцу!')

    def signaling(self):  # Звуковое исполнение морзянки
        try:
            frequency = 1000  # Частота
            for symbol in list(self.translate(self.textEdit.toPlainText())):
                if symbol == '·':
                    winsound.Beep(frequency, 100)  # Частота, громкость
                elif symbol == '-':
                    winsound.Beep(frequency, 700)
                time.sleep(0.2)
            time.sleep(0.4)
        except KeyError:
            self.textEdit_2.insertPlainText('Невозможно озвучить данный '
                                            'фрагмент')


class ReceiverWindowUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(850, 450))
        MainWindow.setMaximumSize(QtCore.QSize(850, 450))
        MainWindow.setSizeIncrement(QtCore.QSize(850, 450))
        MainWindow.setBaseSize(QtCore.QSize(850, 450))
        MainWindow.setWindowIcon(QIcon('translating.png'))
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 230, 321, 141))
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(
            "background-color:rgb(255, 106, 106) ; border-radius: 15px; "
            "padding: 5px;\n "
            "color: white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 60, 321, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(
            "background-color:rgb(255, 106, 106) ; border-radius: 15px; "
            "padding: 5px;\n "
            "color: white;")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 751, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 390, 141, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 106, 106);\n"
            "color: white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(22, 40, 481, 341))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.label)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit.setStyleSheet(
            "background-color: white; border-radius: 15px; border: 2px solid "
            "rgb(255, 106, 106); padding: 10px;")
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole,
                                  self.textEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.label_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_2.setStyleSheet(
            "background-color: white; border-radius: 15px; border: 2px solid "
            "rgb(255, 106, 106);  padding: 10px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole,
                                  self.textEdit_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.LabelRole,
                                  self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Получатель"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p "
                                        "align=\"center\">Здесь отображенно "
                                        "</p><p "
                                        "align=\"center\">переведённое "
                                        "сообщение</p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p "
                                        "align=\"center\">Вводите сообщение "
                                        "на Азбуке Мозре</p><p "
                                        "align=\"center\">Без специальных "
                                        "символов, запятых и т. п.</p><p "
                                        "align=\"center\">Разделение между "
                                        "двумя буквами 1 пробел</p><p "
                                        "align=\"center\">Между словами 3 "
                                        "пробела</p><p "
                                        "align=\"center\">Перевод строки "
                                        "возможен</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Окно получателя"))
        self.pushButton_2.setText(_translate("MainWindow", "Транслировать"))
        self.label.setText(_translate("MainWindow", "Морзянка:"))
        self.label_2.setText(_translate("MainWindow", "Обычный текст:"))


class ReceiverWindow(QMainWindow, ReceiverWindowUi):  # Логика окна получателя
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.alphabet_2 = {'·-': 'А', '-···': 'Б', '·--': 'В', '--·': 'Г',
                           '-··': 'Д', '·': 'Е', '···-': 'Ж', '--··': 'З',
                           '··': 'И', '·---': 'Й', '-·-': 'К', '·-··': 'Л',
                           '--': 'М', '-·': 'Н', '---': 'О', '·--·': 'П',
                           '·-·': 'Р', '···': 'С', '-': 'Т', '··-': 'У',
                           '··-·': 'Ф', '····': 'Х', '-·-·': 'Ц', '---·': 'Ч',
                           '----': 'Ш', '--·-': 'Щ', '--·--': 'Ъ', '-·--': 'Ы',
                           '-··-': 'Ь', '··-··': 'Э', '··--': 'Ю', '·-·-': 'Я',
                           '·----': '1', '··---': '2', '···--': '3',
                           '····-': "4", '·····': '5', '-····': '6',
                           '--···': '7', '---··': '8', '----·': '9',
                           '-----': '0'}
        self.pushButton_2.clicked.connect(self.conclusion)

    def retranslate(self, morse):  # Дешифровка азбуки морзе
        total = ''
        if '\n' in morse:
            for line in morse.split('\n'):
                if '   ' in line:
                    for word in line.split('   '):
                        for s in word.split(' '):
                            total += (self.alphabet_2[s]).lower()
                        total += ' '
                elif '   ' not in line:
                    for s in line.split(' '):
                        total += (self.alphabet_2[s]).lower()
                total += '\n'
        elif '\n' not in morse:
            if '   ' in morse:
                for word in morse.split('   '):
                    for s in word.split(' '):
                        total += (self.alphabet_2[s]).lower()
                    total += ' '
            elif '   ' not in morse:
                for s in morse.split(' '):
                    total += (self.alphabet_2[s]).lower()
        return total

    def conclusion(self):
        text = self.textEdit.toPlainText()
        self.textEdit_2.clear()
        try:
            self.textEdit_2.insertPlainText(self.retranslate(text))
        except KeyError:
            self.textEdit_2.insertPlainText('Введён неправильный код или '
                                            'символ\nТолько символы · и - в '
                                            'соответствии с Азбукой Морзе')


class WelcomeWindowUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        MainWindow.setMinimumSize(QtCore.QSize(600, 300))
        MainWindow.setMaximumSize(QtCore.QSize(600, 300))
        MainWindow.setSizeIncrement(QtCore.QSize(600, 300))
        MainWindow.setBaseSize(QtCore.QSize(600, 300))
        MainWindow.setWindowIcon(QIcon('translating.png'))
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 170, 271, 91))
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(
            "background-color: white; border-radius: 15px; border: 2px solid "
            "rgb(255, 106, 106);  padding: 10px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(
            "background-color: white; border-radius: 15px; border: 2px solid "
            "rgb(255, 106, 106);  padding: 10px;")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 69, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 601, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 20, 601, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 581, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 106, 106);\n"
            "color: white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(
            "background-color: rgb(255, 106, 106);\n"
            "color: white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главная"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p "
                                        "align=\"center\">Можно ввести "
                                        "готовое сообщение</p><p "
                                        "align=\"center\">и расшифровать его "
                                        "</p><p align=\"center\">с помощью "
                                        "программы</p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p "
                                        "align=\"center\">Можно ввести любой "
                                        "текст</p><p align=\"center\">и "
                                        "получить в виде текста, звука</p><p "
                                        "align=\"center\">набор символов "
                                        "Азбуки Морзе</p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p "
                                        "align=\"center\">Выберите свою "
                                        "роль</p></body></html>"))
        self.label_7.setText(_translate("MainWindow",
                                        "<html><head/><body><p "
                                        "align=\"center\">Переводчик Азбуки "
                                        "Морзе</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Отправитель"))
        self.pushButton_3.setText(_translate("MainWindow", "Получатель"))


class WelcomeWindow(QMainWindow, WelcomeWindowUi):  # Логика окна выбора
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.run)

    def run(self):
        if self.sender().text() == 'Отправитель':
            self.window = SenderWindow()
            self.window.show()

        elif self.sender().text() == 'Получатель':
            self.window_2 = ReceiverWindow()
            self.window_2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WelcomeWindow()
    ex.show()
    sys.exit(app.exec_())
