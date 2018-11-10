
import sqlite3

def insertDB(grid_sz, grid_str, action_str):
	grid_nw = []
	for x in grid_str.split("\n"):
		tmp = []
		for y in x.strip().split(" "):
			tmp += [float(y)]
		grid_nw += [tmp]
	actions = [int(x) for x in action_str.strip().split(" ")]
	conn = sqlite3.connect('/home/alphago/mysite/database.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO GRIDS (GRIDSZ ,PATH ,MATRIX) VALUES (?,?,?)",(grid_sz, str(actions), str(grid_nw)) )
	conn.commit()
	return


def getGridDB(grid_sz):
	conn = sqlite3.connect('/home/alphago/mysite/database.db')
	cur = conn.cursor()
	cmd = "SELECT * FROM GRIDS WHERE GRIDSZ=" + str(grid_sz)
	cur.execute(cmd)
	row = cur.fetchone()
	return row

def insertSurvey(gridsz, actions, reward, time):
	conn = sqlite3.connect('/home/alphago/mysite/database.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO survey_resp (gridsz ,action ,reward, time) VALUES (?,?,?, ?)",(gridsz, actions, reward, time) )
	conn.commit()
	return

def showSurvey(grid_sz):
	conn = sqlite3.connect('/home/alphago/mysite/database.db')
	cur = conn.cursor()
	cmd = "SELECT * FROM survey_resp WHERE gridsz=" + str(grid_sz)
	cur.execute(cmd)
	row = cur.fetchall()
	return row
# CREATE TABLE GRIDS (GRIDSZ PRIMARY INT , PATH TEXT, MATRIX TEXT)

'''

4, """6.13876 5.6374 6.30629 17.9616
6.79385 9.71925 0.768178 2.39541
3.73161 1.9446 10.9779 17.1131 """, "2 2 2 1 3 3 1 3 1 2 2 2 "

'''
