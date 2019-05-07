import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from tkinter import messagebox
class Database():
	def check_if_mysql_is_connected_good():
		try:
			db = MySQLdb.connect("mysql.agh.edu.pl" , "binzari" , "zGLhR8NTLL95ZpSk","binzari")
		except Exception:
			messagebox.showinfo('error','error while connection to mysql Database')
	def print_all_from_database():
		db = MySQLdb.connect("mysql.agh.edu.pl" , "binzari" , "zGLhR8NTLL95ZpSk","binzari")
		cursor = db.cursor()
		cursor.execute("SELECT * from students")
		data=cursor.fetchall()
		for row in data :
		    print (row)
		db.close()







