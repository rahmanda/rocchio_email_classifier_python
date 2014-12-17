from DB import DB

DB.set_config('localhost', 'imail', 'imail', 'imail')
con = DB.connect()

if con :
	cur = con.cursor()

	cur.execute("SELECT * FROM users WHERE account = 'jarvis@mail.com'")

	account = cur.fetchone()

	print("id: %ld; account: %s; name: %s; password: %s" % (account[0], account[1], account[2], account[3]))

	DB.close(con)