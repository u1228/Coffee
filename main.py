import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
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


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())