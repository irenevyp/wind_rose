# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wind_rose_all.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import wind_plot

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, QToolBar, QMessageBox, QToolTip
from PyQt5.QtGui import QPixmap, QFont
import os
import sys


class Ui_ROSA_VETROV(object):
        
    QToolTip.setFont(QFont('TimesNewRoman', 10))
    
    def setupUi(self, ROSA_VETROV):
        ROSA_VETROV.setObjectName("ROSA_VETROV")
        ROSA_VETROV.resize(758, 600)
        ROSA_VETROV.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(ROSA_VETROV)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setToolTip('Данная программа предназначена для формирования' +
                                      ' \n розы ветров для трех метеостанций:\n'
                                      'Мценск, Орел и Верховье\n' +
                                      'Данные для метеостанций взяты с сайта rp5.ru\n' +
                                      'Для запуска программы необходимо:\n' +
                                      '- выбрать метеостанцию\n' +
                                      '- выбрать вид представления розы ветров\n' +
                                      '- наличие снега\n' +
                                      '- наличие ветра более 3 м/с\n' +
                                      '- дату начала и окончания выборки данных')

        self.meteostation = QtWidgets.QComboBox(self.centralwidget)
        self.meteostation.setGeometry(QtCore.QRect(10, 10, 261, 41))
        self.meteostation.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.meteostation.setObjectName("meteostation")
        self.meteostation.addItem("")
        self.meteostation.addItem("")
        self.meteostation.addItem("")
        self.meteostation.addItem("")
        self.meteostation.setToolTip('Выберите метеостанцию')
        self.start_calc = QtWidgets.QPushButton(self.centralwidget)
        self.start_calc.setGeometry(QtCore.QRect(0, 440, 271, 101))
        self.start_calc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.start_calc.setObjectName("start_calc")
        self.start_calc.setToolTip('Будет произведен расчет для выбранных условий')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 440, 191, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 490, 191, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 80, 261, 41))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setToolTip('Выберите представление розы ветров')
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(390, 50, 331, 301))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setToolTip('Здесь будет представлен график розы ветров')

        self.n_data = QtWidgets.QDateEdit(self.centralwidget)

        self.n_data.setGeometry(QtCore.QRect(280, 470, 194, 22))
        self.n_data.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.n_data.setObjectName("n_data")
        # setting minimum date
        self.n_data.setMinimumDate(QtCore.QDate(2006, 9, 1))
        self.n_data.setMaximumDate(QtCore.QDate(2021, 7, 31))
        self.n_data.setToolTip('Начальная дата для расчета (не более 31.07.2021)')
        self.k_data = QtWidgets.QDateEdit(self.centralwidget)
        self.k_data.setGeometry(QtCore.QRect(280, 520, 194, 22))
        self.k_data.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.k_data.setObjectName("k_data")
        self.k_data.setMinimumDate(QtCore.QDate(2010, 8, 31))
        self.k_data.setMaximumDate(QtCore.QDate(2021, 8, 31))
        self.k_data.setToolTip('Конечная дата для расчета (не более 31.08.2021)')
        self.r_cond = QtWidgets.QLabel(self.centralwidget)
        self.r_cond.setGeometry(QtCore.QRect(10, 150, 261, 241))
        self.r_cond.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.r_cond.setObjectName("r_cond")
        self.r_cond.setToolTip('Здесь будут представлены условия расчета')
        self.exit_program = QtWidgets.QPushButton(self.centralwidget)
        self.exit_program.setGeometry(QtCore.QRect(490, 450, 161, 81))
        self.exit_program.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.exit_program.setObjectName("exit_program")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(300, 330, 81, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(300, 370, 141, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.rose_name = QtWidgets.QLabel(self.centralwidget)
        self.rose_name.setGeometry(QtCore.QRect(394, 10, 321, 20))
        self.rose_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rose_name.setObjectName("rose_name")
        self.rose_name.setToolTip('Название метеостанции и вид розы ветров, представленной на графике')
        self.start_calc.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.meteostation.raise_()
        self.comboBox.raise_()
        self.graphicsView.raise_()
        self.n_data.raise_()
        self.k_data.raise_()
        self.r_cond.raise_()
        self.exit_program.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.rose_name.raise_()
        ROSA_VETROV.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ROSA_VETROV)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 26))
        self.menubar.setObjectName("menubar")
        ROSA_VETROV.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ROSA_VETROV)
        self.statusbar.setObjectName("statusbar")
        ROSA_VETROV.setStatusBar(self.statusbar)

        self.retranslateUi(ROSA_VETROV)
        QtCore.QMetaObject.connectSlotsByName(ROSA_VETROV)

    def retranslateUi(self, ROSA_VETROV):
        _translate = QtCore.QCoreApplication.translate
        ROSA_VETROV.setWindowTitle(_translate("ROSA_VETROV", "MainWindow"))
        self.meteostation.setItemText(0, _translate("ROSA_VETROV", "Мценск"))
        self.meteostation.setItemText(1, _translate("ROSA_VETROV", "Орел"))
        self.meteostation.setItemText(2, _translate("ROSA_VETROV", "Верховье"))
#        self.meteostation.setItemText(3, _translate("ROSA_VETROV", "Все для сравнения"))
        self.start_calc.setWhatsThis(_translate("ROSA_VETROV", "Расчет и построение розы ветров при заданных условиях"))
        self.start_calc.setText(_translate("ROSA_VETROV", "Расчет"))
        self.label.setText(_translate("ROSA_VETROV", "Выберите начальную дату"))
        self.label_2.setText(_translate("ROSA_VETROV", "Выберите конечную дату"))
        self.comboBox.setWhatsThis(_translate("ROSA_VETROV", "Выбор вида розы ветров - цветная, черно белая или три контура для сравнения по трем направлениям"))
        self.comboBox.setItemText(0, _translate("ROSA_VETROV",
                                                "Роза ветров цветная"))
        self.comboBox.setItemText(1, _translate("ROSA_VETROV",
                                                "Роза ветров черно-белая"))
        self.comboBox.setItemText(2, _translate("ROSA_VETROV",
                                                "Роза ветров контур"))
        self.r_cond.setText(_translate("ROSA_VETROV", ""))
        self.exit_program.setText(_translate("ROSA_VETROV",
                                             "Окончание работы"))
        self.checkBox.setText(_translate("ROSA_VETROV", "Снег"))
        self.checkBox_2.setText(_translate("ROSA_VETROV",
                                           "Ветер 3 м/с и более"))
        self.rose_name.setText(_translate("ROSA_VETROV", ""))
        self.set()

    def set(self):
        self.start_calc.clicked.connect(self.equal)
        self.exit_program.clicked.connect(app.quit)
       
    def equal(self):
        dict = {'Мценск': 'archiv_mcensk_05_21.csv',
                'Верховье': 'archiv_verh_05_21.csv',
                'Орел': 'archiv_orel_05_21.csv'}
        di = {"Роза ветров цветная": 0, "Роза ветров черно-белая": 1,
              "Роза ветров контур": 2}
        s = ui.meteostation.currentText() + ': ' + ui.comboBox.currentText()
        self.rose_name.setText(s)

        a = self.checkBox.isChecked()
        b = self.checkBox_2.isChecked()
        if self.n_data.date().toString('yyyy.MM.dd') > self.k_data.date().toString('yyyy.MM.dd'):
            s_r = 'Конечная дата расчетов меньше начальной'
            self.r_cond.setText(s_r)
        else:
            date_n = self.n_data.date().toString('dd.MM.yyyy')
            date_k = self.k_data.date().toString('dd.MM.yyyy') 
            s_r = 'Расчеты проводятся для: \n' + 'метеостанция : ' + \
                  ui.meteostation.currentText() + '\n'
            s_r = s_r + 'c ' + date_n + ' по ' + date_k + ' \n'
            if a:
                s_1 = ' при наличии осадков в виде снега ' + '\n'
            else:
                s_1 = ' независимо от осадков' + '\n'
            if b:
                s_1 = s_1 + ' и при ветре 3 и более м/с' + '\n'
            else:
                s_1 = s_1 + ' независимо от скорости ветра' + '\n'
            s_r = s_r + s_1
            file_name = wind_plot.obr_file(dict[ui.meteostation.currentText()],
                                           date_n, date_k, a, b,
                                           di[ui.comboBox.currentText()])
            s_r = s_r + 'Роза ветров и таблица сохранены в файле : \n' \
                  + file_name
            self.r_cond.setText(s_r)

            # вставить название рисунка в зависимости от выбранного направления

            pix = QPixmap('wrose '+ui.meteostation.currentText()+'.jpg')
            pixmap4 = pix.scaled(290, 290, QtCore.Qt.KeepAspectRatio)
            item = QtWidgets.QGraphicsPixmapItem(pixmap4)

            scene = QtWidgets.QGraphicsScene()

            scene.addItem(item)
            self.graphicsView.setScene(scene)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ROSA_VETROV = QtWidgets.QMainWindow()
    ui = Ui_ROSA_VETROV()
    ui.setupUi(ROSA_VETROV)
    ROSA_VETROV.show()
    sys.exit(app.exec_())
