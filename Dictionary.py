#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json
from DB import DB

class Dictionary:

	_table = 'dictionary'

	# insert a term into dictionary table group by document id
	def add_dictionary(self, term):
		con = DB.connect()

		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s WHERE term = %s" % table, term)

		if cur.rowcount > 0 :
			cur.execute("UPDATE %s SET df = df + 1 WHERE term = %s" % table, term)
		else :
			cur.execute("INSERT INTO %s VALUES (%s, 1)" % table, term)

		con.close(con)

	# get dictionary table and transform into array key structure
	# for easier access to df value
	# return dicts array
	def fetch_all(self):
		df = {}
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s" % table)
		rows = cur.fetchall()

		for row in rows:
			df[row['term']] = row['df'];

		con.close(con)

		return df