#!/usr/bin/python
# -*- coding: utf-8 -*-
from DB import DB

class Dictionary:

	_table = 'dictionary'
	term = 0
	df = 1

	# insert a term into dictionary table group by document id
	@classmethod
	def add_dictionary(self, term):
		con = DB.connect()

		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s WHERE term = %s" % (table, term))

		if cur.rowcount > 0 :
			cur.execute("UPDATE %s SET df = df + 1 WHERE term = %s" % (table, term))
		else :
			cur.execute("INSERT INTO %s VALUES (%s, 1)" % (table, term))

		con.close(con)

	# get dictionary table and transform into array key structure
	# for easier access to df value
	# return dicts array
	@classmethod
	def fetch_all(self):
		df = {}
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s" % table)
		rows = cur.fetchall()

		for row in rows:
			df[row[self.term]] = row[self.df];

		DB.close(con)

		return df