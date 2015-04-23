import sqlite3

# How often this save
saveStep = 1
num = 0

# connection
conn = None
c = None

def getFormat(data):
	if type(data) is str:
		return 'TEXT'
	if type(data) is float:
		return 'REAL'
	if type(data) is int:
		return 'INTEGER'
	return 'TEXT'

def insertRecord(data):
	try:
		del data['_id'] # mongo surprise :)
	except Exception as e:
		pass
	columns = ', '.join(data.keys())
	placeholders = ', '.join('?' * len(data))
	insertQuery = 'INSERT INTO data ({}) VALUES ({})'.format(columns, placeholders)
	c.execute(insertQuery, tuple(data.values()))

def createTable(data, name):
	try:
		del data['_id']
	except Exception as e:
		pass
	keys = data.keys()
	dbKeys = [
				"id INTEGER PRIMARY KEY AUTOINCREMENT",
				"created DATETIME DEFAULT CURRENT_TIMESTAMP"
			]
	for key in keys:
		dbKeys.append(key + ' ' + getFormat(data[key]))
	createQuery = 'CREATE TABLE IF NOT EXISTS ' + name + '(' + ' ,'.join(dbKeys) + ')'
	c.execute(createQuery)

def save(data, name):
	global c, conn, num
	conn = sqlite3.connect(name + '.db')
	c = conn.cursor()
	createTable(data, name)
	insertRecord(data)
	num += 1
	if num % saveStep == 0: 
		conn.commit()

def commit():
	conn.commit()
