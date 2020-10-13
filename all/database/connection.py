import pymysql.cursors

mydb = pymysql.connect(host='localhost',
							user='root',
							password='',
							db='dbapi',
							charset='utf8mb4',
							cursorclass=pymysql.cursors.DictCursor)
mycursor = mydb.cursor()