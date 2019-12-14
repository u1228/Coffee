import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
import sqlite3


class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('main.ui', self)
		con = sqlite3.connect('coffee.sqlite')
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
		con = sqlite3.connect('coffee.sqlite')
		cur = con.cursor()
		result = cur.execute(f"select id, fryDeg, type, packVol, price, description from coffee where name = '{name}'").fetchone()
		self.label_7.setText(str(result[0]))
		self.label_8.setText(str(result[1]))
		self.label_9.setText(result[2])
		self.label_10.setText(str(result[3]))
		self.label_11.setText(str(result[4]))
		self.plainTextEdit.setPlainText(result[5])
		con.close()
		
		
class AddEditCoffeeForm(QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi('addEditCoffeeForm.ui', self)
		self.show()
		con = sqlite3.connect('coffee.sqlite')
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
		con = sqlite3.connect('coffee.sqlite')
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
		con = sqlite3.connect('coffee.sqlite')
		cur = con.cursor()
		cur.execute("insert into coffee (name) values ('')")
		con.commit()
		con.close()


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())