from PyQt5 import QtCore, QtGui, QtWidgets
from studentDemoProject import Ui_Strudentdata
from mysqlExample import Database
import MySQLdb
from tkinter import messagebox
import sys
#create application
app = QtWidgets.QApplication(sys.argv)

#create form and init ui
Strudentdata = QtWidgets.QDialog()
ui = Ui_Strudentdata()
ui.setupUi(Strudentdata)
Strudentdata.show()
var=str(None)
#Hook logic
#our code
def buttonADD():
	try:
		global var
		Name=ui.textEdit.toPlainText()
		Surname=ui.textEdit_2.toPlainText()
		Marks=ui.textEdit_3.toPlainText()
		Sex=var
		Age=ui.spinBox.value()
		con = MySQLdb.connect("mysql.agh.edu.pl" , "binzari" , "zGLhR8NTLL95ZpSk","binzari",False)
		with con:
			cur=con.cursor()
			cur.execute("insert into students values('"+Name+"','"+Surname+"','"+Marks+"','"+Sex+"','"+str(Age)+"')")
			cur.close()
			ui.studentText.setText("Added successfully")
	except Exception:
		messagebox.showinfo('error','error while using buttonADD')

def buttonSHOW():
	try:
		db = MySQLdb.connect("mysql.agh.edu.pl" , "binzari" , "zGLhR8NTLL95ZpSk","binzari",False)
		cursor = db.cursor()
		cursor.execute("SELECT * from students")
		data=cursor.fetchall()
		ui.studentText.setText("")
		for row in data :
		    ui.studentText.append(str(row)+"\n")
		db.close()
	except Exception:
		messagebox.showinfo('error','error while using buttonSHOW')
def buttonMale():
	global var 
	var= "Male"
def buttonFemale():
	global var 
	var= "Famale"
def buttonDELETE():
	try:
		Name=ui.textEdit.toPlainText()
		Surname=Surname=ui.textEdit_2.toPlainText()
		con = MySQLdb.connect("mysql.agh.edu.pl" , "binzari" , "zGLhR8NTLL95ZpSk","binzari",False)
		with con:
			cur=con.cursor()
			cur.execute("delete from students where Name=+'"+Name+"'and Surname='"+Surname+"'")
			cur.close()
			ui.studentText.setText("Deleted successfully??????????????????????")
	except Exception:
		messagebox.showinfo('error','error while using buttonDELETE')

def buttonMODIFY():
	try:
		Name=ui.textEdit.toPlainText()
		Surname=ui.textEdit_2.toPlainText()
		Marks=ui.textEdit_3.toPlainText()
		Sex=var
		Age=ui.spinBox.value()
		con = MySQLdb.connect("mysql.agh.edu.pl" , "binzari" , "zGLhR8NTLL95ZpSk","binzari",False)
		with con:
			cur=con.cursor()
			cur.execute("delete from students where Name=+'"+Name+"'and Surname='"+Surname+"'")
			cur.execute("insert into students values('"+Name+"','"+Surname+"','"+Marks+"','"+Sex+"','"+str(Age)+"')")

			cur.close()
			ui.studentText.setText("mod")
	except Exception:
		messagebox.showinfo('error','error while using buttonMODIFY')



ui.buttonAdd.clicked.connect(buttonADD)
ui.buttonShow.clicked.connect(buttonSHOW)
ui.buttonDelete.clicked.connect(buttonDELETE)
ui.radioButton.clicked.connect(buttonMale)
ui.radioButton_2.clicked.connect(buttonFemale)
ui.buttonModify.clicked.connect(buttonMODIFY)
#run main loop
sys.exit(app.exec_())

