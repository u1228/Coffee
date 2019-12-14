import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 301)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 271, 251))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setObjectName("listWidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(290, 40, 251, 251))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.label_11.setFont(font)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_11)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(290, 10, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 10, 21, 23))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ID:"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки:"))
        self.label_3.setText(_translate("MainWindow", "Тип:"))
        self.label_4.setText(_translate("MainWindow", "Объем упаковки:"))
        self.label_5.setText(_translate("MainWindow", "Цена:"))
        self.label_6.setText(_translate("MainWindow", "Описание вкуса:"))
        self.label_12.setText(_translate("MainWindow", "Вид кофе"))
        self.label_13.setText(_translate("MainWindow", "Информация о кофе"))
        self.pushButton.setText(_translate("MainWindow", "🖉"))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(593, 434)
        Form.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 571, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 571, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 370, 571, 54))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setStyleSheet("background-color: rgb(235, 235, 235)")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(235, 235, 235)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">Добавление или редактирование</p></body></html>"))
        self.pushButton.setText(_translate("Form", "Создать новую запись о кофе"))
        self.pushButton_2.setText(_translate("Form", "Сохранить"))


class Window(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		con = sqlite3.connect('data/coffee.sqlite')
		cur = con.cursor()
		result = [e[0] for e in cur.execute('select name from coffee order by id asc').fetchall()]
		for e in result:
			self.listWidget.addItem(e)
		con.close()
		self.listWidget.currentTextChanged.connect(self.updateInfo)
		self.pushButton.clicked.connect(self.openAddEditForm)
		
	def openAddEditForm(self):
		self.form = AddEditCoffeeForm()
		
	def updateInfo(self, name):
		con = sqlite3.connect('data/coffee.sqlite')
		cur = con.cursor()
		result = cur.execute(f"select id, fryDeg, type, packVol, price, description from coffee where name = '{name}'").fetchone()
		self.label_7.setText(str(result[0]))
		self.label_8.setText(str(result[1]))
		self.label_9.setText(result[2])
		self.label_10.setText(str(result[3]))
		self.label_11.setText(str(result[4]))
		self.plainTextEdit.setPlainText(result[5])
		con.close()
		
		
class AddEditCoffeeForm(QWidget, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		con = sqlite3.connect('data/coffee.sqlite')
		cur = con.cursor()
		result = [e[1:] for e in cur.execute('select * from coffee').fetchall()]
		self.tableWidget.setRowCount(len(result))
		self.tableWidget.setColumnCount(len(result[0]))
		for i in range(len(result)):
			for j in range(len(result[i])):
				self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
		con.close()
		self.pushButton.clicked.connect(self.addRow)
		self.pushButton_2.clicked.connect(self.changeDaWorld)
		
	def changeDaWorld(self):
		con = sqlite3.connect('data/coffee.sqlite')
		cur = con.cursor()
		for row in range(self.tableWidget.rowCount()):
			nm = self.tableWidget.item(row, 0).text()
			fd = self.tableWidget.item(row, 1).text()
			tp = self.tableWidget.item(row, 2).text()
			ds = self.tableWidget.item(row, 3).text()
			pr = self.tableWidget.item(row, 4).text()
			pv = self.tableWidget.item(row, 5).text()
			try:
				cur.execute(f"""update coffee set name = '{nm}',
fryDeg = {fd},
type = '{tp}',
description = '{ds}',
price = {pr},
packVol = {pv}
where id = {row + 1}""")
			except:
				print(f"""update coffee set name = '{nm}',
fryDeg = {fd},
type = '{tp}',
description = '{ds}',
price = {pr},
packVol = {pv}
where id = {row + 1}
FAILED""")
		con.commit()
		con.close()
		
	def addRow(self):
		self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
		con = sqlite3.connect('data/coffee.sqlite')
		cur = con.cursor()
		cur.execute("insert into coffee (name) values ('')")
		con.commit()
		con.close()


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())